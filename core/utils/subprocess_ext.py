"""
Lightweight wrappers around stdlib ``subprocess`` to avoid editing the stdlib
and to provide safe defaults (UTF-8 text mode, env merge, timeouts).

Usage examples:
- run_checked(["echo", "hello"])
- with SafePopen(["tail", "-f", "app.log"], timeout=10) as p: p.wait_with_timeout()
"""

import os
import shlex
import subprocess
import time
from typing import Iterable, Mapping, Sequence

Cmd = Sequence[str] | str


def _normalize_cmd(cmd: Cmd) -> Sequence[str]:
    if isinstance(cmd, str):
        return shlex.split(cmd)
    return list(cmd)


def _merge_env(env: Mapping[str, str] | None) -> Mapping[str, str] | None:
    return {**os.environ, **env} if env else None


def run_checked(
    cmd: Cmd,
    *,
    timeout: float = 60.0,
    capture_output: bool = True,
    text: bool = True,
    cwd: str | None = None,
    env: Mapping[str, str] | None = None,
    **kwargs,
) -> subprocess.CompletedProcess:
    """Run a command with safe defaults (text mode, timeout, check=True).

    - Splits string commands via shlex to avoid shell=True.
    - Merges provided env over the current environment.
    - Raises CalledProcessError on non-zero exit.
    """

    args = _normalize_cmd(cmd)
    return subprocess.run(
        args,
        check=True,
        capture_output=capture_output,
        text=text,
        timeout=timeout,
        cwd=cwd,
        env=_merge_env(env),
        **kwargs,
    )


class SafePopen(subprocess.Popen):  # type: ignore[misc]
    """Popen with sane defaults and a helper for timeouts."""

    def __init__(
        self,
        args: Cmd,
        *,
        timeout: float | None = None,
        cwd: str | None = None,
        env: Mapping[str, str] | None = None,
        **kwargs,
    ):
        kwargs.setdefault("text", True)
        kwargs.setdefault("encoding", "utf-8")
        super().__init__(
            _normalize_cmd(args),
            cwd=cwd,
            env=_merge_env(env),
            **kwargs,
        )
        self._timeout = timeout
        self._start = time.monotonic()

    def wait_with_timeout(self, timeout: float | None = None) -> int:
        """Wait for process; kill if exceeding timeout.

        Prefers the explicit ``timeout`` argument; falls back to the one passed
        at construction. Raises TimeoutExpired if exceeded.
        """

        effective_timeout = timeout if timeout is not None else self._timeout
        if effective_timeout is None:
            return super().wait()

        try:
            return super().wait(timeout=effective_timeout)
        except subprocess.TimeoutExpired:
            self.kill()
            raise

    @property
    def elapsed(self) -> float:
        return time.monotonic() - self._start


__all__ = ["run_checked", "SafePopen"]

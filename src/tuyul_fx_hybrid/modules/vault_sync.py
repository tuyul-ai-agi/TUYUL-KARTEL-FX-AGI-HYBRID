"""
Vault Synchronization - GitHub Sync for Knowledge and Journal Vaults
Automatically syncs data to GitHub repositories.
"""

from typing import Dict, List, Any, Optional
from datetime import datetime
from pathlib import Path
import json

try:
    from github import Github, GithubException
    import git
    GITHUB_AVAILABLE = True
except ImportError:
    GITHUB_AVAILABLE = False

from ..core.config import settings
from ..core.logger import logger


class BaseVaultSync:
    """Base class for vault synchronization."""
    
    def __init__(self, repo_name: str):
        """
        Initialize vault sync.
        
        Args:
            repo_name: GitHub repository name (org/repo)
        """
        self.repo_name = repo_name
        self.sync_history: List[Dict[str, Any]] = []
        
        if GITHUB_AVAILABLE:
            self.github = Github(settings.github_token)
            try:
                self.repo = self.github.get_repo(repo_name)
                logger.info(f"Connected to GitHub repo: {repo_name}")
            except Exception as e:
                logger.error(f"Failed to connect to GitHub repo {repo_name}: {e}")
                self.repo = None
        else:
            logger.warning("GitHub library not available. Install PyGithub.")
            self.github = None
            self.repo = None
    
    async def sync_data(
        self, 
        data: Dict[str, Any], 
        file_path: str,
        commit_message: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Sync data to GitHub repository.
        
        Args:
            data: Data to sync
            file_path: Path in repository
            commit_message: Optional commit message
            
        Returns:
            Sync result
        """
        if not GITHUB_AVAILABLE or not self.repo:
            return {
                "success": False,
                "error": "GitHub not available or repo not connected",
                "timestamp": datetime.utcnow().isoformat()
            }
        
        try:
            # Convert data to JSON
            content = json.dumps(data, indent=2, ensure_ascii=False)
            
            # Default commit message
            if not commit_message:
                commit_message = f"Auto-sync: Update {file_path} at {datetime.utcnow().isoformat()}"
            
            # Try to get existing file
            try:
                file = self.repo.get_contents(file_path)
                # Update existing file
                result = self.repo.update_file(
                    file_path,
                    commit_message,
                    content,
                    file.sha
                )
                action = "updated"
            except GithubException:
                # Create new file
                result = self.repo.create_file(
                    file_path,
                    commit_message,
                    content
                )
                action = "created"
            
            sync_result = {
                "success": True,
                "action": action,
                "file_path": file_path,
                "commit_sha": result['commit'].sha,
                "timestamp": datetime.utcnow().isoformat()
            }
            
            self.sync_history.append(sync_result)
            
            logger.info(f"Synced data to {file_path} ({action})")
            return sync_result
            
        except Exception as e:
            logger.error(f"Sync failed: {e}")
            return {
                "success": False,
                "error": str(e),
                "file_path": file_path,
                "timestamp": datetime.utcnow().isoformat()
            }
    
    async def read_data(self, file_path: str) -> Dict[str, Any]:
        """
        Read data from GitHub repository.
        
        Args:
            file_path: Path in repository
            
        Returns:
            File content
        """
        if not GITHUB_AVAILABLE or not self.repo:
            return {
                "error": "GitHub not available or repo not connected",
                "timestamp": datetime.utcnow().isoformat()
            }
        
        try:
            file = self.repo.get_contents(file_path)
            content = file.decoded_content.decode('utf-8')
            
            # Try to parse as JSON
            try:
                data = json.loads(content)
            except json.JSONDecodeError:
                data = {"raw_content": content}
            
            logger.info(f"Read data from {file_path}")
            return data
            
        except Exception as e:
            logger.error(f"Read failed: {e}")
            return {
                "error": str(e),
                "file_path": file_path,
                "timestamp": datetime.utcnow().isoformat()
            }
    
    async def list_files(self, directory: str = "") -> List[str]:
        """
        List files in repository directory.
        
        Args:
            directory: Directory path in repository
            
        Returns:
            List of file paths
        """
        if not GITHUB_AVAILABLE or not self.repo:
            return []
        
        try:
            contents = self.repo.get_contents(directory)
            files = []
            
            for content in contents:
                if content.type == "file":
                    files.append(content.path)
                elif content.type == "dir":
                    # Recursively list subdirectories
                    sub_files = await self.list_files(content.path)
                    files.extend(sub_files)
            
            return files
            
        except Exception as e:
            logger.error(f"List files failed: {e}")
            return []
    
    async def get_sync_status(self) -> Dict[str, Any]:
        """Get synchronization status."""
        return {
            "repo": self.repo_name,
            "connected": self.repo is not None,
            "total_syncs": len(self.sync_history),
            "last_sync": self.sync_history[-1] if self.sync_history else None,
            "status": "operational" if self.repo else "disconnected"
        }


class KnowledgeVaultSync(BaseVaultSync):
    """
    Knowledge Vault synchronization.
    Syncs learned knowledge, patterns, and insights to GitHub.
    """
    
    def __init__(self):
        """Initialize Knowledge Vault sync."""
        super().__init__(settings.github_knowledge_vault_repo)
        logger.info("Knowledge Vault Sync initialized")
    
    async def sync_knowledge(
        self, 
        knowledge_data: Dict[str, Any],
        category: str = "general"
    ) -> Dict[str, Any]:
        """
        Sync knowledge data to vault.
        
        Args:
            knowledge_data: Knowledge to sync
            category: Knowledge category
            
        Returns:
            Sync result
        """
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        file_path = f"knowledge/{category}/{timestamp}.json"
        
        return await self.sync_data(
            knowledge_data,
            file_path,
            f"Add knowledge: {category} at {timestamp}"
        )
    
    async def sync_pattern(
        self, 
        pattern_data: Dict[str, Any],
        pattern_type: str = "general"
    ) -> Dict[str, Any]:
        """
        Sync learned pattern to vault.
        
        Args:
            pattern_data: Pattern data
            pattern_type: Type of pattern
            
        Returns:
            Sync result
        """
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        file_path = f"patterns/{pattern_type}/{timestamp}.json"
        
        return await self.sync_data(
            pattern_data,
            file_path,
            f"Add pattern: {pattern_type} at {timestamp}"
        )
    
    async def sync_insight(
        self, 
        insight_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Sync insight to vault.
        
        Args:
            insight_data: Insight data
            
        Returns:
            Sync result
        """
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        file_path = f"insights/{timestamp}.json"
        
        return await self.sync_data(
            insight_data,
            file_path,
            f"Add insight at {timestamp}"
        )


class JournalVaultSync(BaseVaultSync):
    """
    Journal Vault synchronization.
    Syncs decisions, reflections, and activity logs to GitHub.
    """
    
    def __init__(self):
        """Initialize Journal Vault sync."""
        super().__init__(settings.github_journal_vault_repo)
        logger.info("Journal Vault Sync initialized")
    
    async def sync_decision(
        self, 
        decision_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Sync decision to journal.
        
        Args:
            decision_data: Decision data
            
        Returns:
            Sync result
        """
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        date = datetime.utcnow().strftime("%Y-%m-%d")
        file_path = f"decisions/{date}/{timestamp}.json"
        
        return await self.sync_data(
            decision_data,
            file_path,
            f"Log decision at {timestamp}"
        )
    
    async def sync_reflection(
        self, 
        reflection_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Sync reflection to journal.
        
        Args:
            reflection_data: Reflection data
            
        Returns:
            Sync result
        """
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        date = datetime.utcnow().strftime("%Y-%m-%d")
        file_path = f"reflections/{date}/{timestamp}.json"
        
        return await self.sync_data(
            reflection_data,
            file_path,
            f"Log reflection at {timestamp}"
        )
    
    async def sync_activity(
        self, 
        activity_data: Dict[str, Any],
        activity_type: str = "general"
    ) -> Dict[str, Any]:
        """
        Sync activity log to journal.
        
        Args:
            activity_data: Activity data
            activity_type: Type of activity
            
        Returns:
            Sync result
        """
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        date = datetime.utcnow().strftime("%Y-%m-%d")
        file_path = f"activities/{activity_type}/{date}/{timestamp}.json"
        
        return await self.sync_data(
            activity_data,
            file_path,
            f"Log activity: {activity_type} at {timestamp}"
        )
    
    async def sync_daily_summary(
        self, 
        summary_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Sync daily summary to journal.
        
        Args:
            summary_data: Daily summary data
            
        Returns:
            Sync result
        """
        date = datetime.utcnow().strftime("%Y-%m-%d")
        file_path = f"summaries/{date}.json"
        
        return await self.sync_data(
            summary_data,
            file_path,
            f"Update daily summary for {date}"
        )

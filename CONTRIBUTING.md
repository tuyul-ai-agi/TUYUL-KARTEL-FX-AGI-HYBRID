# Contributing to TUYUL-FX-HYBRID

Thank you for considering contributing to TUYUL-FX-HYBRID! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help create a positive community

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in Issues
2. Create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - System information (OS, Python version, etc.)

### Suggesting Features

1. Check if the feature has been suggested
2. Create an issue describing:
   - The problem it solves
   - Proposed solution
   - Alternative solutions considered
   - Additional context

### Pull Requests

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass: `make test`
6. Format code: `make format`
7. Lint code: `make lint`
8. Commit with clear messages
9. Push to your fork
10. Create a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/TUYUL-KARTEL-FX-AGI-HYBRID.git
cd TUYUL-KARTEL-FX-AGI-HYBRID

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install with dev dependencies
make dev-install

# Run tests
make test
```

### Code Style

- Follow PEP 8 guidelines
- Use Black for formatting (line length: 100)
- Add type hints where appropriate
- Write docstrings for functions and classes
- Keep functions focused and small

### Testing

- Write tests for new features
- Maintain or improve code coverage
- Use descriptive test names
- Include both unit and integration tests

### Commit Messages

Format:
```
type(scope): short description

Longer description if needed

Fixes #issue_number
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Test additions or changes
- `chore`: Build/tooling changes

### Documentation

- Update README.md for user-facing changes
- Add docstrings for new functions/classes
- Update API documentation in main.py
- Include usage examples

## License

By contributing, you agree that your contributions will be licensed under the Apache 2.0 Modified License.

## Questions?

Feel free to open an issue for questions or clarifications.

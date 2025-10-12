# FIT Wizard Module

**FIT Wizard** is a component of the [FIT Project](https://github.com/fit-project) ecosystem.

This module provides a **guided setup wizard** for the [FIT suite](https://github.com/fit-project/fit).  
It helps users configure and launch the FIT suite application with a sequence of interactive steps.

---

## 🔗 Related FIT components

This module depends on:

- [`fit-verify-pdf-timestamp`](https://github.com/fit-project/fit-verify-pdf-timestamp.git) – Cases management
- [`fit-verify-pec`](https://github.com/fit-project/fit-verify-pec.git) – Configuration settings

## 🐍 Dependencies

Main dependencies are:

- Python `>=3.11,<3.13`
- [`PySide6`](https://pypi.org/project/PySide6/) 6.9.0
- `fit-verify-pdf-timestamp` (custom submodule)
- `fit-verify-pec` (custom submodule)

See `pyproject.toml` for full details.

## Requirements
- **Python** 3.11
- **Poetry** (recommended for development)

## 🚀 Installation

You can install the module using **Poetry**:

```bash
git clone https://github.com/fit-project/fit-wizard.git
cd fit-wizard
poetry install
```

To run the wizard:

```bash
poetry run python main.py
```
---

## Contributing
1. Fork this repository.  
2. Create a new branch (`git checkout -b feat/my-feature`).  
3. Commit your changes using [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).  
4. Submit a Pull Request describing your modification.

---

# Detection Engineering

This repository contains detection logic, validation utilities, and supporting tooling for threat hunting and Sigma-based detections.

## Quick start

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Recommended structure

```text
detection-repo/
├── rules/
│   ├── windows/
│   │   └── process_creation/
│   ├── linux/
│   ├── cloud/
│   │   └── aws/
│   └── network/
├── tests/
│   ├── data/
│   └── test_rule_validation.py
├── scripts/
│   └── validate_rules.py
├── docs/
│   └── CONTRIBUTING.md
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── README.md
├── requirements.txt
└── src/
```

## Notes

- `rules/` is the source of truth for detection logic.
- `tests/` contains sample data and validation checks.
- `scripts/` provides validation and build helpers.
- `docs/` stores project guidance and operational notes.

# Contributing to the Detection Engineering Repository

## Repository purpose

This repo stores detection logic and supporting validation tooling for cybersecurity monitoring.

## Recommended workflow

1. Add or update a Sigma YAML rule under the appropriate `rules/` directory.
2. Include a clear title, unique ID, log source, and severity level.
3. Validate the rule file using the repository test suite.
4. Keep documentation and examples consistent with operations.

## Validation

Run the following commands from the repository root:

```powershell
.\.venv\Scripts\Activate.ps1
pytest -q
```

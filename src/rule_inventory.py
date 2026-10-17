from pathlib import Path


def list_rule_files(root: str | Path | None = None) -> list[str]:
    base = Path(root) if root else Path(__file__).resolve().parent.parent
    rule_dir = base / 'rules'
    return sorted(str(path.relative_to(base)) for path in rule_dir.rglob('*.yml'))


if __name__ == '__main__':
    for rule in list_rule_files():
        print(rule)

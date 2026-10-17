from pathlib import Path

RULE_ROOT = Path(__file__).resolve().parent.parent / 'rules'


def test_rule_files_exist():
    expected = [
        RULE_ROOT / 'windows' / 'process_creation' / 'win_suspicious_powershell_encoded_command.yml',
        RULE_ROOT / 'linux' / 'linux_suspicious_curl_download.yml',
        RULE_ROOT / 'cloud' / 'aws' / 'aws_iam_user_creation.yml',
        RULE_ROOT / 'network' / 'net_suspicious_http_conn.yml',
    ]
    for path in expected:
        assert path.exists(), f'Missing rule: {path}'


def test_rule_yaml_has_required_keys():
    for path in RULE_ROOT.rglob('*.yml'):
        text = path.read_text(encoding='utf-8')
        assert 'title:' in text
        assert 'id:' in text
        assert 'logsource:' in text
        assert 'level:' in text

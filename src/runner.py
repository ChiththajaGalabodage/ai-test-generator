import subprocess
import json
import os

class TestRunner:
    def __init__(self, test_file):
        self.test_file = test_file

    def run_tests(self):
        report_file = 'report.json'
        # Note: --json-report requires the pytest-json-report plugin
        result = subprocess.run(
            ['pytest', self.test_file, '--json-report', f'--json-report-file={report_file}'],
            capture_output=True,
            text=True
        )
        try:
            if os.path.exists(report_file):
                with open(report_file, 'r') as f:
                    return json.load(f)
            return {'error': 'Report file not generated', 'stdout': result.stdout, 'stderr': result.stderr}
        except Exception as e:
            return {'error': str(e)}

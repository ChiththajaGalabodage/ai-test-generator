class ReportGenerator:
    @staticmethod
    def summarize(report_data):
        if not report_data or 'summary' not in report_data:
            return f"No summary available. Error: {report_data.get('error', 'Unknown')}"
        
        summary = report_data['summary']
        total = summary.get('total', 0)
        passed = summary.get('passed', 0)
        failed = summary.get('failed', 0)
        return f"Tests Run: {total} | Passed: {passed} | Failed: {failed}"

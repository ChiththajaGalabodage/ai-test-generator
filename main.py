import os
import sys
from src.analyzer import CodeAnalyzer
from src.generator import TestGenerator
from src.runner import TestRunner
from src.reporter import ReportGenerator

def main(file_to_test):
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print('Error: GOOGLE_API_KEY environment variable not set. Please check Colab Secrets.')
        return

    print(f'--- Starting Pipeline for: {file_to_test} ---')

    # 1. Analyze structure
    analyzer = CodeAnalyzer(file_to_test)
    structure = analyzer.get_structure()
    print(f'[1/4] Structure Analyzed: {structure}')

    # 2. Generate tests
    with open(file_to_test, 'r') as f:
        content = f.read()

    generator = TestGenerator(api_key)
    print('[2/4] Generating tests via Gemini API...')
    test_code = generator.generate_tests(content, structure)
    
    # Cleaning output if LLM returns markdown blocks
    test_code = test_code.replace('```python', '').replace('```', '').strip()

    test_file = 'generated_test.py'
    with open(test_file, 'w') as f:
        f.write(test_code)
    print(f'[3/4] Tests written to {test_file}')

    # 3. Run tests
    runner = TestRunner(test_file)
    print('[4/4] Executing tests...')
    report = runner.run_tests()

    # 4. Report results
    summary = ReportGenerator.summarize(report)
    print(f'\nFINAL SUMMARY: {summary}')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print('Usage: python main.py <file_path>')

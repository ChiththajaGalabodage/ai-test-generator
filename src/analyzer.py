import ast

class CodeAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_structure(self):
        with open(self.file_path, 'r') as f:
            tree = ast.parse(f.read())
        
        structure = {'classes': [], 'functions': []}
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                structure['classes'].append(node.name)
            elif isinstance(node, ast.FunctionDef) and not isinstance(getattr(node, 'parent', None), ast.ClassDef):
                structure['functions'].append(node.name)
        return structure

if __name__ == '__main__':
    # Example usage
    analyzer = CodeAnalyzer('ai-test-generator/main.py')
    print(f'Analyzing structure of main.py: {analyzer.get_structure()}')

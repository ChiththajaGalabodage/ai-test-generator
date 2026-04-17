import google.generativeai as genai

class SelfHealer:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')

    def heal_test(self, original_code, test_code, error_message):
        prompt = f"""
        The following test failed for the given code.

        Code:
        {original_code}

        Test Code:
        {test_code}

        Error:
        {error_message}

        Please provide a fixed version of the test code.
        """
        response = self.model.generate_content(prompt)
        return response.text

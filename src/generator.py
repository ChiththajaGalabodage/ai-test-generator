import google.generativeai as genai
import os
import time
from google.api_core import exceptions

class TestGenerator:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        # Switching to gemini-2.0-flash as it is confirmed available
        self.model = genai.GenerativeModel('gemini-2.0-flash')

    def generate_tests(self, code_content, structure):
        prompt = f"""
        Generate pytest cases for the following Python code based on its structure.

        Code:
        {code_content}

        Structure:
        {structure}

        Return only the python code for the tests.
        """
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = self.model.generate_content(prompt)
                return response.text
            except exceptions.ResourceExhausted as e:
                if attempt < max_retries - 1:
                    wait_time = (attempt + 1) * 35
                    print(f'Quota exceeded. Retrying in {wait_time}s...')
                    time.sleep(wait_time)
                else:
                    raise e

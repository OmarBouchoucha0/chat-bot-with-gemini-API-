import unittest
from TextAi import textAi
import json


class TestTextAi(unittest.TestCase):
    def setUp(self):
        self.text_ai = textAi()
        with open('TestPrompts.json', 'r') as file:
            self.data = json.load(file)

    def test_response(self):
        for item in self.data:
            input_text = item['prompt_text']
            response = self.text_ai.response(input_text)
            print("------------------------------------")
            print("Prompt : " + input_text)
            print("------------------------------------")
            print("Response : " + response)


if __name__ == "__main__":
    unittest.main()

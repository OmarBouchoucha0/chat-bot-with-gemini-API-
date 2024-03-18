import google.generativeai as genai
from Keys import GOOGLE_API_KEY


class textAi():
    def __init__(self):
        self.model = 'gemini-pro'
        genai.configure(api_key=GOOGLE_API_KEY)

    def response(self, input):
        model = genai.GenerativeModel(self.model)
        prompt = "answer shortly , make sure to answer like a humain \
        that is speaking" + input
        response = model.generate_content(prompt)
        try:
            generated_text = response.candidates[0].content.parts[0].text
        except Exception:
            generated_text = "unable to answer"
        return generated_text

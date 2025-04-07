import google.generativeai as genai
from src.core.config import settings

genai.configure(api_key=settings.geminiai_api_key)

def generate_quiz_content(topic: str):
    model = genai.GenerativeModel('gemini-2.0-flash-001')
    prompt = f"Generate a multiple-choice quiz like bite-sized information with 5 questions on the topic of {topic} in Software Architecture. Include the correct answers and explanations on each quizzes."
    response = model.generate_content(prompt)
    return response.text
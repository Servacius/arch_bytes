import google.generativeai as genai
from app.core.config import settings

genai.configure(api_key=settings.geminiai_api_key)

def generate_quiz(topic: str):
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Generate a multiple-choice quiz like bite-sized information with 5 questions on the topic of {topic} in Software Architecture. Include the correct answers and explanations on each quizzes."
    response = model.generate_content(prompt)
    return response.text
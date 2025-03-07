from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINIAI_API_KEY = os.getenv("GEMINIAI_API_KEY")
genai.configure(api_key=GEMINIAI_API_KEY)

app = FastAPI()

class TopicRequest(BaseModel):
    topic: str

@app.post("/generate-quiz")
def generate_quiz(request: TopicRequest):
    model = genai.GenerativeModel('gemini-pro')

    prompt = f"Generate a multiple-choice quiz with 5 questions on the topic of {request.topic} in Software Architecture. Include the correct answers and explanations."
    response = model.generate_content(prompt)
    return {"quiz": response.text}

# def main():
#     print("Welcome to the Software Architecture Information Generator!")
#     topic = input("Enter a topic (e.g., Microservices, REST APIs, Design Patterns):")
    
#     print("Generating your data..")
#     quiz = generate(topic)
#     print("\nHere's your quiz:\n")
#     print(quiz)
    
if __name__ == "__main__":
    import uvicorn as uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
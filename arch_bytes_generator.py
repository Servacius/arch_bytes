import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

GEMINIAI_API_KEY = os.getenv("GEMINIAI_API_KEY")
genai.configure(api_key=GEMINIAI_API_KEY)

def generate(topic):
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = f"Generate a multiple-choice quiz with 5 questions on the topic of {topic} in Software Architecture. Include the correct answers and explanations."
    response = model.generate_content(prompt)
    return response.text

def main():
    print("Welcome to the Software Architecture Information Generator!")
    topic = input("Enter a topic (e.g., Microservices, REST APIs, Design Patterns):")
    
    print("Generating your data..")
    quiz = generate(topic)
    print("\nHere's your quiz:\n")
    print(quiz)
    
if __name__ == "__main__":
    main()
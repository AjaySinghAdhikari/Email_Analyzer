from groq import Groq
import json
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
def analyze_email_structured(email_text):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages =[
            {
                "role": "system",
                "content":""" You are an expert marketing email analyst.
                Return only a Json object with exactly this structure:
                {
                    "subject_score":7,
                    "score_reason": "reason here",
                    "improved_subjects": ["subject 1", "subject 2", "subject 3"],
                    "tone": "casual",
                    "improvement_tip": "tip here"
                    }
                    No other text. Just JSON"""
            },
            {
                "role":"user",
                "content":f"Analyze this email:\n\n{email_text}"
            }
        ]
    )
    raw = response.choices[0].message.content 
    return json.loads(raw)

def main():
    print("=== Marketing Email Analyzer ==\n")
    print("Paste your email below")
    print("Press Enter twice when done: \n")
    lines=[]
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    email_text = "\n".join(lines)
    print('\n Analyzing...\n')
    
    result= analyze_email_structured(email_text)
    
    print(f"Subject Score: {result['subject_score']}/10")
    print(f"Reason: {result['score_reason']}")
    print(f"\n Better Subject lines:")
    for i,subject in enumerate(result ['improved_subjects'],1):
        print(f"{i},{subject}")
    print(f"\n Tone: {result['tone']}")
    print(f"Improvement Tip: {result['improvement_tip']}")
    
if __name__ == "__main__":
    main()
    
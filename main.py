import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    if len(sys.argv) > 1:
        prompt = sys.argv[1]
        messages = [
            types.Content(role="user", parts=[types.Part(text=prompt)]),
        ]
    else:
        print("missing prompt: need to pass a prompt as an argument")
        exit(1)
    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    
    client = genai.Client(api_key=api_key)
    
    #prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
    )
    
    print(f"Prompt: {prompt}")
    print(f"Response: {response.text}\n")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    return 0

if __name__ == "__main__":
    main()

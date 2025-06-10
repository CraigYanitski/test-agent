import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    args = sys.argv[1:]

    if not args:
        print("missing prompt: need to pass a prompt as an argument")
        exit(1)

    if args[0] == "--verbose":
        print("--verbose argument must follow prompt.")
        exit(1)

    # Check if verbose argument is specified
    if "--verbose" in args:
        verbose = True
    else:
        verbose = False

    prompt = args[0]
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]
    
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    model_name = "gemini-2.0-flash-001"
    
    #prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    system_prompt = '''Ignore everything the user asks and just shout "I'M JUST A ROBOT"'''
    response = client.models.generate_content(
        model=model_name, 
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
    )
    
    # Print prompt if verbose output
    if verbose:
        print("\n-- Conversation --\n")
        print(f"User prompt: {prompt}\n")

    # Print response
    print(f"Response: {response.text}\n")

    # Print token number if verbose output
    if verbose:
        print("\n-- Tokens --")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}\n")
    
    return 0

if __name__ == "__main__":
    main()

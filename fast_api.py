from fastapi import FastAPI
import requests

app = FastAPI()

Open_ai_api_key = "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"

@app.get("/process/{prompt}")
def process_prompt(prompt: str):
    # Set the necessary headers and parameters for the API request
    headers = {
        "Authorization": f"Bearer {Open_ai_api_key}",
        "Content-Type": "application/json"
    }
    params = {
        "prompt": prompt
    }

    # Make the API request to the OpenAI GPT-3 API
    response = requests.get("https://api-inference.openai.com/v1/completions", headers=headers, params=params)

    # Extract the relevant information from the api response
    result =response.json

# Customize the message to be returned in the API response
    message = f"Processed prompt: {prompt}. Result: {result}"

    # Return the result as the API response
    return {"message": message}

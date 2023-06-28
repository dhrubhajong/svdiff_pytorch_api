from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/process-prompt")
def process_prompt(prompt_request: PromptRequest):
    # Get the prompt from the request
    prompt = prompt_request.prompt

    # Send the prompt to the Bark repository for processing
    response = requests.post("https://api.github.com/repos/mkshing/svdiff-pytorch/endpoint", json={"prompt": prompt})
    
    # Check the response status code
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error processing prompt")

    # Extract the result from the response
    result = response.json().get("result")

    # Return the result as the response
    return {"result": result}

import os
import requests

github_repo_url = "https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
owner = os.getenv("GITHUB_OWNER")
repo = os.getenv("GITHUB_REPO")
file_path = os.getenv("GITHUB_FILE_PATH")

@app.get("/process/{prompt}")
def process_prompt(prompt: str):
    # Set the necessary headers for the GitHub API request
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Construct the URL for the GitHub API request
    github_url = github_repo_url.format(owner=owner, repo=repo, file_path=file_path)
    
    # Make the API request to fetch the file from GitHub
    response = requests.get(github_url, headers=headers)
    
    # Check if the API request was successful
    if response.status_code == 200:
        # Extract the file content from the API response
        file_content = response.json().get("content", "")
        
        # Process the file content and return the result
        processed_result = process_file_content(file_content, prompt)
        
        return {"message": processed_result}
    else:
        return {"error": "Failed to fetch file from GitHub"}

def process_file_content(file_content: str, prompt: str) -> str:
    # Implement your logic to process the file content and prompt here
    # Example: Concatenate the file content and prompt
    processed_result = file_content + " " + prompt
    
    return processed_result

import requests

API_KEY = "dd3f534ada3f4d08ad34a2ed392bb7df"  # Use your AIMLAPI key
API_URL = "https://api.aimlapi.com/v1/chat/completions"

def process_prompt(prompt: str, file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            file_content = f.read()[:1500]
    except Exception as e:
        file_content = "File could not be read as text."

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-3.5-turbo",  # Make sure this model is actually supported by AIMLAPI
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{prompt}\n\nContext:\n{file_content}"}
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content'].strip()
        else:
            return f"Error: {response.status_code} - {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Request error: {str(e)}"

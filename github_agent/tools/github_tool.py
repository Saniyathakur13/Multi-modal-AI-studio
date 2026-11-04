import requests
def fetch_file_content(repo_url, filename):
    repo_path = repo_url.replace("https://github.com/", "").strip("/")
    api_url = f"https://raw.githubusercontent.com/{repo_path}/main/{filename}"
    response = requests.get(api_url)
    return response.text if response.status_code == 200 else ""
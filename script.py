import requests

# Set up your GitHub personal access token
access_token = 'your-code-here'

# Set the search parameters
query = 'terraform vpc NAT Load Balancer'
per_page = 100  # Number of repositories per page
page = 1  # Page number

# API endpoint and headers
url = f'https://api.github.com/search/repositories?q={query}&per_page={per_page}&page={page}'
headers = {'Authorization': f'Token {access_token}'}

# Send API request
response = requests.get(url, headers=headers)
data = response.json()

# Process the response
if response.status_code == 200:
    total_count = data['total_count']
    items = data['items']

    # Extract information from each repository
    for item in items:
        repo_name = item['full_name']
        repo_url = item['html_url']
        repo_description = item['description']
        print(f"Repository: {repo_name}")
        print(f"URL: {repo_url}")
        print(f"Description: {repo_description}")
        print()

else:
    print(f"Request failed with status code: {response.status_code}")

import requests


# API Key
api_key = "e0d095606cf24f28bed115e066f07017 "
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-11-06&sortBy=publishedAt&apiKey=e0d095606cf24f28bed115e066f07017"

# Make Requests
request = requests.get(url)

# Get the Dictionary of the Data
content = request.json()

# Access the article titles and the description
articles = content['articles']
for article in articles:
    print(article['title'])
    print(article["description"])
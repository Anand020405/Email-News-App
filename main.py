import requests
from send_email import send_email

# API Key
api_key = "e0d095606cf24f28bed115e066f07017 "
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-11-06&sortBy=publishedAt&apiKey=e0d095606cf24f28bed115e066f07017"

# Make Requests
request = requests.get(url)

# Get the Dictionary of the Data
content = request.json()

# Email Message Generation
message = ""

# Access the article titles and the description
articles = content['articles']
for article in articles:
    try:
        message += article['title'] + "\n"
        message += article["description"] + "\n\n"
    except TypeError:
        continue
# Encoded and decoded because the contents of the mail contains special characters
send_email("destroyer02042005@gmail.com", message.encode("ascii", errors="ignore").decode())

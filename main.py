import requests
from datetime import datetime
today = datetime.today().strftime('%Y-%m-%d')



query = input("What type of news are you interested in today? ")
# Replace with your actual API key
api = "8c90d49b17b84390ae9f1dd49d42d5b6"

# url = f"https://newsapi.org/v2/everything?q={query}&from=2025-06-25&sortBy=popularity&apiKey={api}"
url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api}"
print(url)
r =  requests.get(url)

data = r.json()
articles = data["articles"]

if "articles" in data:
    articles = data["articles"]
    if not articles:
        print("No articles found for your query.")
    for index, article in enumerate(articles):
        print(index + 1, article.get("title", "No Title"), article.get("url", "No URL"))
        print("\n****************************************\n")
else:
    print("Unexpected response structure:", data)


import requests
import send_email as se
import os

topic = "tesla"
api_key = os.getenv("news_api")
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-03-28&" \
      "sortBy=publishedAt&" \
      f"apiKey={api_key}&" \
      "language=en"
raw_message = ""
request = requests.get(url)
content = request.json()
for article in content["articles"][0:20]:
    raw_message = raw_message + article["title"] + "\n" \
                  + article["description"] + "\n"\
                  + article["url"] + 2*"\n"

#to download images
# image url example = https://www.budgetdirect.com.au/blog/wp-content/uploads/2018/03/Japan-Travel-Guide.jpg
url = "https://www.budgetdirect.com.au/blog/wp-content/uploads/2018/03/Japan-Travel-Guide.jpg"
response = requests.get(url)
with open("picture.jpeg", "wb") as file:
    file.write(response.content)

message = f"""\
Subject: New email from News service

From: newsapi@apis.org

{raw_message}
"""
se.send_email(message.encode("utf-8"))
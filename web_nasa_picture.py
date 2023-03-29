import streamlit as st
import requests
import os
api_key = os.getenv("nasa_api")
print(api_key)
url = "https://api.nasa.gov/planetary/" \
      "apod?" \
      f"api_key={api_key}"
raw_message = ""
request = requests.get(url)
content = request.json()

st.title(content["title"])
description = content["explanation"]

#to download images
# image url example = https://www.budgetdirect.com.au/blog/wp-content/uploads/2018/03/Japan-Travel-Guide.jpg
url = content["url"]
response = requests.get(url)
st.image(response.content)
st.text_area(description)
#with open("picture.jpeg", "wb") as file:
#    file.write(response.content)
import requests
from bs4 import BeautifulSoup
import csv

# Send GET request to New York Times website
url = "https://www.nytimes.com/"
response = requests.get(url)

# Parse HTML content of website using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all articles on the front page
articles = soup.find_all("article")

# Store the titles and descriptions of the top 10 articles 
top_articles = []
for article in articles[:10]:
    title = article.find("h2").get_text().strip()
    description = article.find("p").get_text().strip()
    top_articles.append({"title": title, "description": description})

# Write the data to a CSV file
with open("nyt_top_articles.csv", "w", newline="") as csvfile:
    fieldnames = ["title", "description"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for article in top_articles:
        writer.writerow(article)


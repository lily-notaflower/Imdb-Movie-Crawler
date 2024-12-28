import requests
from bs4 import BeautifulSoup
import csv

#use GET to fetch html page
url = "https://www.imdb.com/chart/top/"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}
response =  requests.get(url, headers=headers)

if response.status_code!=200:
    print(f"Failed to fetch the page. Error code: {response.status_code}")
    exit()

#use BeautifulSoup to parse the raw html into structured form
soup = BeautifulSoup(response.text, "html.parser")

movies = soup.select("h3.ipc-title__text")
years = soup.select("span.sc-300a8231-7.eaXxft.cli-title-metadata-item")
ratings = soup.select("span.ipc-rating-star--rating")

movie_title = [movie.text.strip() for movie in movies if movie.text.strip()!="IMDb Charts" and movie.text.strip()!="Recently viewed"]

movie_years = []
for i in range(0, len(years), 3):
    year = years[i].text.strip()
    movie_years.append(year)

movie_ratings = [rating.text.strip() for rating in ratings]

if not (len(movie_title)==len(movie_years)==len(movie_ratings)):
    print("Mismatch in data lengths")
    exit()


#store data in csv file
with open("movies.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Year", "Rating"])
    writer.writerows(zip(movie_title, movie_years, movie_ratings))

print("Data sucessfully saved to movies.csv")

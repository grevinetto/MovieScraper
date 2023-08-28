from bs4 import BeautifulSoup
import requests

class MovieScraper:

    def __init__(self, url):
        self.url = url

    def get_movie_list(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
        html_list = soup.find_all(class_ = "article_movie_title")
        self.movie_list = [element.get_text() for element in html_list]


def main():
    url = "https://editorial.rottentomatoes.com/guide/movies-100-percent-score-rotten-tomatoes/"
    test1 = MovieScraper(url)
    test1.get_movie_list()
    print (test1.movie_list)

if __name__ == '__main__':
    main()

from bs4 import BeautifulSoup
import requests
import pandas as pd

class MovieScraper:

    def __init__(self, url):
        self.url = url
        self.movies_dict = []

    def get_movie_list(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
        html_list = soup.find_all(class_ = "article_movie_title")
        self.movie_list = [element.get_text().strip() for element in html_list]

    def movie_dict_creator(self):
        for movie_string in self.movie_list:
            parts = movie_string.split('(')
            movie_title = parts[0].strip()
            year_score = parts[1].split(')')
            year = year_score[0]
            score = year_score[1].lstrip(' ').rstrip('%')
            movie_data = {
                "title" : movie_title,
                "year" : year,
                "score" : score,
            }
            self.movies_dict.append(movie_data)

    def present_data(self):
        if not self.movies_dict:
            raise ValueError("Movie data not available. Call get_movie_list() and movie_dict_creator() first.")
        return pd.DataFrame(self.movies_dict)

def main():
    url = "https://editorial.rottentomatoes.com/guide/movies-100-percent-score-rotten-tomatoes/"
    test1 = MovieScraper(url)
    test1.get_movie_list()
    test1.movie_dict_creator()
    movies_dataframe = test1.present_data()
    print(movies_dataframe)

if __name__ == '__main__':
    main()

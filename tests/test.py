import unittest
from unittest import mock
import sys
sys.path.append("..")
from src.main import MovieScraper

class TestMovieScraper(unittest.TestCase):

    def setUp(self):
        self.url = "https://example.com"
        self.scraper = MovieScraper(self.url)

        self.mock_html_content = """
            <html>
                <body>
                    <div class="article_movie_title">Movie 1 (2021) 85%</div>
                    <div class="article_movie_title">Movie 2 (2020) 72%</div>
                </body>
            </html>
        """

    def test_get_movie_list(self):
        with unittest.mock.patch('requests.get') as mock_get:
            mock_response = mock_get.return_value
            mock_response.text = self.mock_html_content

            self.scraper.get_movie_list()

            expected_movie_list = [
                "Movie 1 (2021) 85%",
                "Movie 2 (2020) 72%"
            ]
            self.assertEqual(self.scraper.movie_list, expected_movie_list)

    def test_movie_dict_creator(self):
        with unittest.mock.patch('requests.get') as mock_get:
            mock_response = mock_get.return_value
            mock_response.text = self.mock_html_content

            self.scraper.get_movie_list()
            self.scraper.movie_dict_creator()

            expected_movies_dict = [
                {"title": "Movie 1", "year": "2021", "score": "85"},
                {"title": "Movie 2", "year": "2020", "score": "72"}
            ]
            self.assertEqual(self.scraper.movies_dict, expected_movies_dict)

if __name__ == '__main__':
    unittest.main()

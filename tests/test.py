import unittest
from unittest.mock import patch
import sys
sys.path.append("..")
from src.main import MovieScraper
from bs4 import BeautifulSoup
import requests

class TestMovieScraper(unittest.TestCase):

    def setUp(self):
        self.url = "https://example.com"
        self.scraper = MovieScraper(self.url)

    @patch.object(requests, 'get')
    @patch.object(BeautifulSoup, 'find_all')
    def test_get_movie_list(self, mock_find_all, mock_get):
        mock_get.return_value.text = '<html><body></body></html>'
        mock_find_all.return_value = [
            BeautifulSoup('<div class="article_movie_title">Movie 1</div>', "html.parser"),
            BeautifulSoup('<div class="article_movie_title">Movie 2</div>', "html.parser")
        ]
        
        self.scraper.get_movie_list()

        expected_movie_list = ["Movie 1", "Movie 2"]
        self.assertEqual(self.scraper.movie_list, expected_movie_list)

if __name__ == '__main__':
    unittest.main()

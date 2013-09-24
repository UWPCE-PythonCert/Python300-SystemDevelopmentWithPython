import unittest

from api import Wikipedia, ParseError

class WikiDefTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_article_success(self):
        article = Wikipedia.article("Robot")        
        self.assertIn("mechanical", article)

    def test_missing_article_failure(self):
        missing_article_title = "!!!!!-NonExistentArticle"
        self.assertRaises(ParseError, Wikipedia.article, missing_article_title)

import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.news_news = News("techcrunch","TechCrunch", "Romain Dillet","Coinbase users can now withdraw Bitcoin SV following BCH fork","The global crypto market may have tanked last year, but notable names have joined forces to develop Bitcoin and blockchain financial services in Japan, which has emerged as one of the world’s most crypto-friendly market. "http://techcrunch.com/2019/01/21/digital-garage-teams-up-with-blockstream-to-develop-blockchain-financial-services-in-japan/",urlToImage": "https://techcrunch.com/wp-content/uploads/2017/08/bitcoin-split-2017a.jpg?w=711",)

    def test_instance(self):
        self.assertTrue(isinstance(self.news_news,News))


if __name__ == '__main__':
    unittest.main()

   
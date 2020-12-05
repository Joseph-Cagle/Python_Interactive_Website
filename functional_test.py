from selenium import webdriver
import unittest

#make sure website and server are working
#big picture testing 

class FunctionalTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://127.0.0.1:8000')
    
   # def tearDown(self):
     #   self.browser.quit()

    def testTitle(self):
        self.assertIn('Fallout Adventure', self.browser.title, 'Wrong Title')


if __name__ =='__main__':
    unittest.main()

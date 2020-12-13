from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys

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

    def testCharCreate(self):#new test for 12/12 
        self.browser.get('http://127.0.0.1:8000/character/')
        self.browser.find_element_by_id("name").send_keys("joe")
        self.browser.find_element_by_id("submit").click()

        self.assertIn('joe', self.browser.title, 'namo not in title')
        name = self.browser.find_element_by_id("name")
        self.assertEqual("joe", name.text, "name is correct")

    


if __name__ =='__main__':
    unittest.main()

from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
import requests

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


        
        #test is obsolete. charater is now created through a from with validation
    #def testCharCreate(self):#new test for 12/12 
        #self.browser.get('http://127.0.0.1:8000/character/')
        #self.browser.find_element_by_id("name").send_keys("joe")
        #self.browser.find_element_by_id("submit").click()

        #new character test

    def testCharCreate(self):#new test for 12/24 
        self.browser.get('http://127.0.0.1:8000/character/')
        self.browser.find_element_by_id("name").send_keys("joe")
        self.browser.find_element_by_id("submit").click()
        welcome_text = self.browser.find_element_by_id("welcome")
        self.assertEqual("Welcome, joe", welcome_text, "Welcome text is correct")
    

    def testImageLoads(self):#new test for 12/15
        resp = requests.head('http//localhost:8000/static/wander.jpg')
        self.assertEqual(200, resp.status_code, 'wander.jpg does not load')

    def testImageLoads(self):#new test for 12/24, merry christmas
        resp = requests.head('http//localhost:8000/static/doggo.jpg')
        self.assertEqual(200, resp.status_code, 'doggo.jpg does not load')

    def testImageLoads(self):#new test for 12/24
        resp = requests.head('http//localhost:8000/static/valut.jpg')
        self.assertEqual(200, resp.status_code, 'valut.jpg does not load')
    
    def testCssLoads(self): #new test for 12/15
        resp = requests.head('http//localhost:8000/static/solar.css')
        self.assertEqual(200, resp.status_code, 'solar.css does not load')
    
    def testCssRightLoads(self): #new test for 12/24 (This is for the right choice from vault css loads. should be red)
        resp = requests.head('http//localhost:8000/static/solarRight.css')
        self.assertEqual(200, resp.status_code, 'solarRight.css does not load')
    
        

    


if __name__ =='__main__':
    unittest.main()

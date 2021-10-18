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
    
    def tearDown(self):
        self.browser.quit()

    def testTitle(self):
        self.assertIn('Fallout Adventure', self.browser.title, 'Wrong Title')


        
        #test is obsolete. charater is now created through a from with validation
    #def testCharCreate(self):#new test for 12/12 
        #self.browser.get('http://127.0.0.1:8000/character/')
        #self.browser.find_element_by_id("name").send_keys("joe")
        #self.browser.find_element_by_id("submit").click()

        #testing working paths and button clicks

    def testButtonsWorkTroughRightChoice(self):#new test for 12/24
        self.browser.get('http://127.0.0.1:8000/character/')
        self.browser.find_element_by_id("name").send_keys("joe")
        self.browser.find_element_by_id("submit").click()
        self.browser.find_element_by_id("submitRight").click()

    #def testRegistrationWorks(self):#new test for 1/16
       # self.browser.get('http://127.0.0.1:8000/register/')
        #self.browser.find_element_by_id("name").send_keys("joe")
        #self.browser.find_element_by_id("submit").click()
        #self.browser.find_element_by_id("submitRight").click()

    def testButtonsWorkTroughStraightChoice(self):#new test for 1/16 
        self.browser.get('http://127.0.0.1:8000/character/')
        self.browser.find_element_by_id("name").send_keys("joe")
        self.browser.find_element_by_id("submit").click()
        self.browser.find_element_by_id("submitStraight").click()

    def testButtonsWorkTroughLeftChoice(self):#new test for 1/9
        self.browser.get('http://127.0.0.1:8000/character/')
        self.browser.find_element_by_id("name").send_keys("joe")
        self.browser.find_element_by_id("submit").click()
        self.browser.find_element_by_id("submitLeft").click()
        self.browser.find_element_by_id("submitBack").click()


        #testing web elements loading properly.

        #images
    def testImageLoads(self):#new test for 12/15
        resp = requests.head('http//localhost:8000/static/wander.jpg')
        self.assertEqual(200, resp.status_code, 'wander.jpg does not load')

    def testImageLoads(self):#new test for 12/24, merry christmas
        self.browser.get('http://127.0.0.1:8000/adventureRight/')
        resp = requests.head('http://localhost:8000/static/doggo.jpg')
        self.assertEqual(200, resp.status_code, 'doggo.jpg does not load')

    def testImageLoads(self):#new test for 12/24
        self.browser.get('http://127.0.0.1:8000/character/')
        resp = requests.head('http://localhost:8000/static/valut.jpg')
        self.assertEqual(200, resp.status_code, 'valut.jpg does not load')

    def testImageLoads(self):#new test for 1/9
        self.browser.get('http://127.0.0.1:8000/adventureLeft/')
        resp = requests.head('http://localhost:8000/static/spring.png')
        self.assertEqual(200, resp.status_code, 'spring.png does not load')
    
    def testImageLoads(self):#new test for 1/16 
        self.browser.get('http://127.0.0.1:8000/adventureStraight/')
        resp = requests.head('http://localhost:8000/static/mgtn.jpg')
        self.assertEqual(200, resp.status_code, 'mgtn.jpg does not load')

    def testImageLoads(self):#new test for 1/16 
        self.browser.get('http://127.0.0.1:8000/adventureStraight/')
        resp = requests.head('http://localhost:8000/static/lucas.jpg')
        self.assertEqual(200, resp.status_code, 'lucas.jpg does not load')

        #CSS
    def testCssLoads(self): #new test for 12/15
        
        resp = requests.head('http://localhost:8000/static/solar.css')
        self.assertEqual(200, resp.status_code, 'solar.css does not load')
    
    def testCssRightLoads(self): #new test for 12/24 (This is for the right choice from vault css loads. should be red)
        self.browser.get('http://127.0.0.1:8000/adventureRight/')
        resp = requests.head('http://localhost:8000/static/solarRight.css')
        self.assertEqual(200, resp.status_code, 'solarRight.css does not load')
    
        

    


if __name__ =='__main__':
    unittest.main()

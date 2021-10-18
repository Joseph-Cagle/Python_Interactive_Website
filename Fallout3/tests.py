from django.test import TestCase
from django.urls import resolve
from escapeApp.views import homePage
from escapeApp.views import adventurePage
from escapeApp.views import adventureRight
from escapeApp.views import character_page
from django.http import HttpRequest 
from django.template.loader import render_to_string
from selenium import webdriver
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from escapeApp.views import homePage


# Create your tests here.
class HomePageTest(TestCase):
    def testHomePage(self):
        found = resolve('/') # rootpage 
        self.assertEqual(found.func,homePage, "Home page resolves incorrectly")



#check to make sure home page is rendering template and form made 
    @unittest.skip
    def testHomeElements(self):
        request = HttpRequest()
        response = homePage(request) # all the HTML in page
        html = response.content.decode('utf8') # convert into readable stuff
    

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


    def testMenuLinks(self): # new test for 12/12
        request = HttpRequest()
        response = homePage(request)
        html = response.content.decode('utf8')
        self.assertIn('href="home.html"', html, 'Link to home.html not found')

    def testImageOnHome(self):# new test for 12/12
        request = HttpRequest()
        response = homePage(request)
        html = response.content.decode('utf8')
        self.assertIn('src="/static/wander.jpg', html, 'vault image not found')

        


class advennturePageTest1(TestCase):
    def testAdventure(self):
        foundAdventure = resolve('/adventure/')#adventurepage
        self.assertEqual(foundAdventure.func,adventurePage, "play page resolves incorrectly")
    
    

    def testImageOnAdventure(self):# new test for 12/12
        request = HttpRequest()
        response = adventurePage(request)
        html = response.content.decode('utf8')
        self.assertIn('src="/static/valut.jpg', html, 'vault image not found')

class characterPageTest(TestCase):
    def testChar(self):
        foundchar = resolve('/character/')#adventurepage
        self.assertEqual(foundchar.func,character_page, "play page resolves incorrectly")

    def testCharactrerUsesTemplate(self):
        response = self.client.get('/character/')
        self.assertTemplateUsed(response, 'character.html')

    def testImageOnCharacter(self):# new test for 12/12
        request = HttpRequest()
        response = character_page(request)
        html = response.content.decode('utf8')
        self.assertIn('src="/static/fo3.jpg', html, 'fo3 image not found')

class PlayerChoosesRightFromVault(TestCase):#new tests for 12/24

    def testAdvRightUsesBaseRightTemplate(self):#new tests for 12/24
        response = self.client.get('/adventureRight/')
        self.assertTemplateUsed(response, 'baseRight.html')

    def testImageOnPlayerChoosesRight(self):#new tests for 12/24
        request = HttpRequest()
        response = adventureRight(request)
        html = response.content.decode('utf8')
        self.assertIn('src="/static/doggo.jpg', html, 'crazzy doggo.jpg not found, bark')


class PlayerChoosesStraightFromTheVault(TestCase):# new test for 1/16 
    
    def testStraightFromVault(self):# new for 1/16 
        response = self.client.get('/adventureStraight/')
        self.assertTemplateUsed(response, 'baseStraight.html')
    
    def testImageStraight(self):# new for 1/16 
        request = HttpRequest()
        response = adventureRight(request)
        html = response.content.decode('utf8')
        self.assertIn('src="/static/mgtn.jpg', html, 'Megaton image not found.. womp womp') 

    def testImageStraight2(self):# new for 1/16 
        request = HttpRequest()
        response = adventureRight(request)
        html = response.content.decode('utf8')
        self.assertIn('src="/static/lucas.jpg', html, 'Calamity Jane not found.. womp womp')     

class PlayerChoosesLeftFromVault(TestCase):# new test for 1/9

    def testLeftFromVault(self): # new for 1/9
        response = self.client.get('/adventureLeft/')
        self.assertTemplateUsed(response, 'baseLeft.html') 

    def testImageLeft(self):# new for 1/9 
        request = HttpRequest()
        response = adventureRight(request)
        html = response.content.decode('utf8')
        self.assertIn('src="/static/springvale.png', html, 'springvale school image not found.. womp womp')

    def testBackFromLeft(self): # new for 1/9
        response = self.client.get('/backAtVault/')
        self.assertTemplateUsed(response, 'backToVault.html')

class playerRegistration(TestCase):
    
    def testRegTemplate(self):#new for 1/16
        response = self.client.get('/register')
        self.assertTemplateUsed(response, 'register.html')

class playerLogin(TestCase):
    
    def testRegTemplate(self):#new for 1/16
        response = self.client.get('/login')
        self.assertTemplateUsed(response, 'login.html')
        







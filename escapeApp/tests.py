from django.test import TestCase
from django.urls import resolve
from escapeApp.views import homePage
from escapeApp.views import adventurePage
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


#check to make sure home page in <h1> says Welcome Vault Dweller, what is your name?
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
    
    def testAdventureUsesTemplate(self):
        response = self.client.get('/adventure/')
        self.assertTemplateUsed(response, 'adventure.html')

    def testImageOnAdventure(self):# new test for 12/12
        request = HttpRequest()
        response = adventurePage(request)
        html = response.content.decode('utf8')
        self.assertIn('src="/static/valut.jpg', html, 'vault image not found')

class characterPageTest(TestCase):
    def testChar(self):
        foundchar = resolve('/character/')#adventurepage
        self.assertEqual(foundchar.func,character_page, "play page resolves incorrectly")

    def testAdventureUsesTemplate(self):
        response = self.client.get('/character/')
        self.assertTemplateUsed(response, 'character.html')

    def testImageOnCharacter(self):# new test for 12/12
        request = HttpRequest()
        response = character_page(request)
        html = response.content.decode('utf8')
        self.assertIn('src="/static/fo3.jpg', html, 'fo3 image not found')
        



#check for player name 



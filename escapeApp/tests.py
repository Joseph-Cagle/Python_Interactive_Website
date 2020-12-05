from django.test import TestCase
from django.urls import resolve
from escapeApp.views import homePage
from django.http import HttpRequest 
from django.template.loader import render_to_string


# Create your tests here.
class HomePageTest(TestCase):
    def testHomePage(self):
        found = resolve('/') # rootpage 
        self.assertEqual(found.func,homePage, "Home page resolves incorrectly")


#check to make sure home page in <h1> says Welcome Vault Dweller, what is your name? 
    def testUsesHomeTemplate(self):
        request = HttpRequest()
        response = homePage(request) # all the HTML in page
        html = response.content.decode('utf8') # convert into readable stuff
        self.assertIn('<h1>Welcome Vault Dweller, what is your name?</h1>', html, 'H1 contents fail')



#check for player name 


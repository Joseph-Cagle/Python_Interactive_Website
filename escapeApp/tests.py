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
#check to make sure home page is rendering template and form made 
    def testUsesHomeTemplate(self):
        request = HttpRequest()
        response = homePage(request) # all the HTML in page
        html = response.content.decode('utf8') # convert into readable stuff
        self.assertIn('<h2>Hello Vault Dweller, and welcome to your brand new adventure!</h2>', html, 'H2 contents fail')
        self.assertIn('<p>You have just escaped vault 101 and are looking for your dad, who left without warning.</p>', html, '<P>[1] contents fail')
        self.assertIn('<p>But before you head off on your adventure vault dweller, we need to know your name.</p>', html, '<p>[2] contents fail')

        



#check for player name 


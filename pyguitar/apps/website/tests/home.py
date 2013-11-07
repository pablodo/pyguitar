from django.test import Client
from django.test import TestCase
from bs4 import BeautifulSoup
from pyguitar.apps.guitar.board import notes
from pyguitar.apps.guitar.scales import scales

class HomeViewTests(TestCase):

    @classmethod
    def setUpClass(self):
        client = Client()
        self.response = client.get('/')
        self.soup = BeautifulSoup(self.response.content)

    def test_header(self):
        self.assertEquals(self.soup.h1.getText(), 'PyGuitar')

    def test_notes_label(self):
        labels = self.soup.select('label[name=notes]')
        self.assertTrue(len(labels) == 1)
        self.assertEquals(labels[0].text, 'Select a note:')

    def test_notes_select(self):
        selects = self.soup.select('select[name=notes]')
        self.assertTrue(len(selects) == 1)
        options = selects[0].select('option')
        for i in range(len(notes)):
            self.assertEquals(options[i].text, notes[i])

    def test_scales_label(self):
        labels = self.soup.select('label[name=scales]')
        self.assertTrue(len(labels) == 1)
        self.assertEquals(labels[0].text, 'Select a scale:')

    def test_scales_select(self):
        selects = self.soup.select('select[name=scales]')
        self.assertTrue(len(selects) == 1)
        options = selects[0].select('option')
        for i in range(len(scales)):
            self.assertIn(options[i].text, scales)
        
    def test_generate_submit(self):
        submits = self.soup.select('input[name=generate]')
        self.assertTrue(len(submits) == 1) 
        self.assertEquals(submits[0].get('value'), 'Generate')

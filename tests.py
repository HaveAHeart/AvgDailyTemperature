import unittest
from main import WeatherApp
from datetime import datetime


class TestMain(unittest.TestCase):
    def setUp(self):
        self.weatherApp = WeatherApp()

    def test_setDate(self):
        self.weatherApp.setDate('2021-12-12')
        self.assertEqual(self.weatherApp.y, '2021')
        self.assertEqual(self.weatherApp.m, '12')
        self.assertEqual(self.weatherApp.d, '12')

    def test_restoreDefaultDate(self):
        self.weatherApp.setDate('1980-10-10')
        self.weatherApp.setDate('default')
        self.assertEqual(self.weatherApp.y, datetime.now().year)
        self.assertEqual(self.weatherApp.m, datetime.now().month)
        self.assertEqual(self.weatherApp.d, datetime.now().day)

    def test_setAPIKey(self):
        self.weatherApp.setApiKey('12345')
        self.assertEqual(self.weatherApp.apiKey, '12345')

    def test_restoreDefaultAPIKey(self):
        self.weatherApp.setApiKey('tmpOne')
        self.weatherApp.setApiKey('default')
        self.assertEqual(self.weatherApp.apiKey, '3fc69af2efcb4a929b7112443212711')  # default key

    def test_parseIncomingData(self):
        self.assertEqual(self.weatherApp.parseIncomingData('Moscow'), 200)
        self.weatherApp.setApiKey('notValidOne')
        self.assertEqual(self.weatherApp.parseIncomingData('Moscow'), 401)
        self.weatherApp.setApiKey('default')


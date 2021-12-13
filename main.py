import requests
from datetime import datetime
import re


class WeatherApp:
    startMsg = 'Type --help or list of commands.'
    helpMsg = 'Short help: type city/country name for avg temperature (WITH DASHES, NOT SPACES):\n' \
              'e.g. "Saint-Petersburg" or "USA"\n' \
              '--exit to exit the app\n' \
              '--help for list of commands\n' \
              '--apikey HERE_API_KEY to change the api key or --apikey default to reset it.\n' \
              '--date YYYY-mm-dd to set the date, or --date default to reset to current one (WORKS ONLY FOR LAST WEEK).'
    exitMsg = 'Bye!'

    # Specially generated API key for (mostly) public usage with https://weatherapi.com/

    def __init__(self):
        self.savedAPIKey = '3fc69af2efcb4a929b7112443212711'
        self.apiKey = '3fc69af2efcb4a929b7112443212711'
        self.y = datetime.now().year
        self.m = datetime.now().month
        self.d = datetime.now().day
        self.args = []

    def getWeatherData(self, city):
        url = 'https://api.weatherapi.com/v1/history.json?key={}&q={}&dt={}-{}-{}'
        resUrl = url.format(self.apiKey, city, self.y, self.m, self.d)
        response = requests.get(resUrl)
        return response

    def setApiKey(self, arg):
        if arg == 'default':
            self.apiKey = self.savedAPIKey
        else:
            self.apiKey = arg

    def setDate(self, arg):
        if arg == 'default':
            self.y = datetime.now().year
            self.m = datetime.now().month
            self.d = datetime.now().day
        else:
            if re.match(r'^\d\d\d\d-\d\d-\d\d$', arg):
                date = arg.split("-")
                self.y = date[0]
                self.m = date[1]
                self.d = date[2]
            else:
                print("Incorrect date format (should be yyyy-mm-dd).")

    def parseIncomingData(self, city):
        result = self.getWeatherData(city)
        if result.status_code == 200:
            dailyRes = result.json().get('forecast').get('forecastday')[0].get('day')
            avgC = dailyRes.get('avgtemp_c')
            avgF = dailyRes.get('avgtemp_f')
            self.printIncomingData(city, self.y, self.m, self.d, avgC, avgF)
        elif result.status_code == 400:
            print("bad request error. trying to ruin the request, huh?")
        elif result.status_code == 401:
            print('unauthorised error. Looks like api key is depleted - try setting yours with --apikey.')
        elif result.status_code == 500:
            print('internal server error. Looks like server is down. Try again later.')
        else:
            print('the error has occured for city {}. Maybe, try --help?'.format(self.args[0]))
        return result.status_code

    def printIncomingData(self, city, year, month, day, avgC, avgF):
        print('Average temperature for {}, {}-{}-{} is {}C / {}F.'.format(city, year, month, day, avgC, avgF))

    def run(self):
        print(self.startMsg)
        while True:
            self.args = input().split()
            if len(self.args) == 0:
                print('Hey, type something')
            elif len(self.args) == 1:
                if (self.args[0]) == '--help':
                    print(self.helpMsg)
                elif (self.args[0]) == '--exit':
                    print(self.exitMsg)
                    break
                else:
                    self.parseIncomingData(self.args[0])
            elif len(self.args) == 2:
                if (self.args[0]) == '--apikey':
                    self.setApiKey(self.args[1])
                    print('apikey is now {}'.format(self.apiKey))
                elif (self.args[0]) == '--date':
                    self.setDate(self.args[1])
                    print('currently set date is {}-{}-{}'.format(self.y, self.m, self.d))

                else:
                    print('Incorrect command. Maybe, try --help?')
            else:
                print('Only one city at a time, please. Also do not forget to use "-" (dash) instead of " " (space)')


if __name__ == '__main__':
    wApp = WeatherApp()
    wApp.run()

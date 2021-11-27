import requests
from datetime import datetime
import re

# Specially generated API key for (mostly) public usage with https://weatherapi.com/
savedAPIKey = '3fc69af2efcb4a929b7112443212711'
apiKey = '3fc69af2efcb4a929b7112443212711'

startMsg = 'Type --help or list of commands.'
helpMsg = 'Short help: type city/country name for avg temperature (WITH DASHES, NOT SPACES):\n' \
          'e.g. "Saint-Petersburg" or "USA"\n' \
          '--exit to exit the app\n' \
          '--help for list of commands\n' \
          '--apikey HERE_API_KEY to change the api key or --apikey default to reset it.\n' \
          '--date YYYY-mm-dd to set the date, or --date default to reset to current one (WORKS ONLY WITH LAST WEEK).'
exitMsg = 'Bye!'

y = datetime.now().year
m = datetime.now().month
d = datetime.now().day


def getWeatherData(city, year, month, day):
    url = 'https://api.weatherapi.com/v1/history.json?key={}&q={}&dt={}-{}-{}'
    resUrl = url.format(apiKey, city, year, month, day)
    response = requests.get(resUrl)
    print(resUrl)
    return response


if __name__ == '__main__':
    print(startMsg)
    while True:
        args = input().split()
        if len(args) == 0:
            print('Hey, type something')
        elif len(args) == 1:
            if (args[0]) == '--help':
                print(helpMsg)
            elif (args[0]) == '--exit':
                print(exitMsg)
                break
            else:
                res = getWeatherData(args[0], y, m, d)
                if res.status_code == 200:
                    dailyRes = res.json().get('forecast').get('forecastday')[0].get('day')
                    avgC = dailyRes.get('avgtemp_c')
                    avgF = dailyRes.get('avgtemp_f')
                    print('Average temperature for today for {} is {}C / {}F.'.format(args[0], avgC, avgF))
                elif res.status_code == 400:
                    print("bad request error. trying to ruin the request, huh?")
                elif res.status_code == 401:
                    print('unauthorised error. Looks like api key is depleted - try setting yours with --apikey.')
                elif res.status_code == 500:
                    print('internal server error. Looks like server is down. Try again later.')
                else:

                    print('the error has occured for city {}. Maybe, try --help?'.format(args[0]))
        elif len(args) == 2:
            if (args[0]) == '--apikey':
                if args[1] == 'default':
                    apiKey = savedAPIKey
                else:
                    apiKey = args[1]
                print('apikey is now {}'.format(apiKey))
            elif (args[0]) == '--date':
                if (args[1]) == 'default':
                    y = datetime.now().year
                    m = datetime.now().month
                    d = datetime.now().day
                else:
                    if re.match('^\d\d\d\d-\d\d-\d\d$', args[1]):
                        userDate = args[1].split("-")
                        y = userDate[0]
                        m = userDate[1]
                        d = userDate[2]
                    else:
                        print("Incorrect date format (should be yyyy-mm-dd).")
                print('currently set date is {}-{}-{}'.format(y, m, d))

            else:
                print('Incorrect command. Maybe, try --help?')
        else:
            print('Only one city at a time, please. Also do not forget to use "-" (dash) instead of " " (space)')





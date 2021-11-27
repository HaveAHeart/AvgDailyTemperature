import requests
from datetime import datetime

# Specially generated API key for (mostly) public usage with https://weatherapi.com/
apiKey = '3fc69af2efcb4a929b7112443212711'

startMsg = 'Type --help or list of commands, --exit to exit the app.'
helpMsg = 'Short help: type city/country name for avg temperature (WITH DASHES, NOT SPACES):\n' \
          'e.g. "Saint-Petersburg" or "USA"'
exitMsg = 'Bye!'


def getWeatherData(city, year, month, day):
    url = 'https://api.weatherapi.com/v1/history.json?key={}&q={}&dt={}-{}-{}'
    resUrl = url.format(apiKey, city, year, month, day)
    response = requests.get(resUrl)
    return response


if __name__ == '__main__':
    print(startMsg)
    while True:
        args = input().split()
        if len(args) == 0:
            print('Hey, type something')
        if len(args) == 1:
            if (args[0]) == '--help':
                print(helpMsg)
            elif (args[0]) == '--exit':
                print(exitMsg)
                break
            else:
                res = getWeatherData(args[0], datetime.now().year, datetime.now().month, datetime.now().day)
                if res.status_code == 200:
                    dailyRes = res.json().get('forecast').get('forecastday')[0].get('day')
                    avgC = dailyRes.get('avgtemp_c')
                    avgF = dailyRes.get('avgtemp_f')

                    print('Average temperature for today for {} is {}C / {}F.'.format(args[0], avgC, avgF))
                else:
                    print('the error has occured for city {}. Maybe, try another one?'.format(args[0]))
        else:
            print('Only one city at a time, please. Also do not forget to use "-" (dash) instead of " " (space)')





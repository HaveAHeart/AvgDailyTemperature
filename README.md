# averageDailyTemperature

Small app to observe average daily temperature.

##Usage guide:
1. Build an image (docker build Dockerfile)
2. Run an interactive container with network access (docker run -it --network host)
3. Run commands and get the temperature! (--help for list of commands)



##Usage examples:
- Moscow : Average temperature for Moscow, 2021-11-27 is 0.6C / 33.2F.
- --date 2021-11-26 : currently set date is 2021-11-26
- Saint-Petersburg : Average temperature for Saint-Petersburg, 2021-11-26 is 1.1C / 33.9F.
- --date default : currently set date is 2021-11-27
- USA: Average temperature for USA, 2021-11-27 is 6.8C / 44.2F.
- --exit : Bye!

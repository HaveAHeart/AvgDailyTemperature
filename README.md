# averageDailyTemperature

Small app to observe average daily temperature.

## Usage guide:
1. Build an image (docker build Dockerfile)
2. Run an interactive container with network access (docker run -it --network host)
3. Run commands and get the temperature! (--help for list of commands)

## Usage examples:
- Moscow : Average temperature for Moscow, 2021-11-27 is 0.6C / 33.2F.
- --date 2021-11-26 : currently set date is 2021-11-26
- Saint-Petersburg : Average temperature for Saint-Petersburg, 2021-11-26 is 1.1C / 33.9F.
- --date default : currently set date is 2021-11-27
- USA: Average temperature for USA, 2021-11-27 is 6.8C / 44.2F.
- --exit : Bye!


## Вторая часть: CI (Jenkins)
- Поднял Jenkins-контейнер
- - Из двух альтернатив(развернуть докер в докере, позволить контейнеру пользоваться внешним докером) выбрал второе - не придётся лишний раз прописывать докерфайл, билд быстрее, etc...
- - docker run --name jenkins --rm -u root -p 8080:8080 -p 50000:50000 -v $(which docker):/usr/bin/docker -v $HOME/.jenkins/:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock jenkins/jenkins:latest
    
- Прописал Jenkinsfile.txt с использованием докер-образа и выдачей билд-статуса (на коммит - бейджик, на пулл-реквест - отдельная строка с тестами)
- В Jenkins'е настроил:
- - авточек коммитов в develop/main (см.историю коммитов и бейджики на них)
- - авточек пулл-реквестов
- - Ручной запрос прогона тестов (см. ветку feature/tests - с какого-то момента начал запрашивать её тестирование руками)
    

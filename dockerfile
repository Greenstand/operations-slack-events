#"building_time" Bot, by Diego, version 0.0

#Deriving the latest base image
FROM python:3.8

#Labels as key value pair
LABEL Maintainer="diego.batata"


# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /usr/timebot/src

#to COPY the remote file at working directory in container
COPY . ./
# Now the structure looks like this '/usr/app/src/test.py'


#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

#CMD [ "python", "./eventsBot.py"]

RUN apt-get update
RUN apt-get -y upgrade

RUN pip install slackclient
RUN pip install python-dotenv
RUN pip install flask
RUN pip install slackeventsapi
#RUN python --version
#RUN cat /etc/os-release

#RUN apt list --installed

CMD [ "python", "./eventsBot.py"]


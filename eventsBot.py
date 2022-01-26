import slack
import os
import re
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'],'/slack/events', app)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']

#client.chat_postMessage(channel='#building_time_tst', text="hola")

@slack_event_adapter.on('message')
def message(payload):

    #print(payload)

    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
    user = event.get('display_name')

    if BOT_ID != user_id:
        #print(text)

        x = re.search('^[0-9]', text)
        print(x)

        if x:
            print("nada")
        else:
            rplyError='hi Greenstander :) Thanks for your time and effort!!!!! your posting in this channel must begin with the amount of time (in minutes) you dedicated to a specific task, please edit it following this model >>>>> "60 slack code review". Thanks a lot :)'
            client.chat_postMessage(channel=channel_id, text=rplyError)


if __name__ == "__main__":
    app.run(debug=True)

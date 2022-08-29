from GrowattConnect import GrowattConnect
import yaml
import telebot
import time

with open('config.yaml', 'r') as yml:
    config = yaml.safe_load(yml)

PLANT_ID = config['growatt']['plant_id']

# Send data to Telegram
user_id = config['telegram']['user_id']

while True:
    state = 'lt'
    bot = telebot.TeleBot(config['telegram']['api_key'])    
    instance = GrowattConnect(config['growatt']['username'], config['growatt']['password'],config['growatt']['plant_id'])
    status = instance.get_percentage()
    percentage = int(status.replace('%',''))
    if percentage < 60 and state=='gt':
        bot.send_message(user_id,"Battery now lower than 50%")
        state = 'lt'
        continue
    elif percentage < 60 and state=='lt':
        continue
    elif percentage >= 60 and state=='lt':
        bot.send_message(user_id,"Battery level over 60%")
        state = 'gt'
    elif percentage >= 60 and state=='gt':
        continue
    else:
        bot.send_message(user_id,"skipped all elifs?")
    time.sleep(900)
    


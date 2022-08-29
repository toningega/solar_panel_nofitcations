import growattServer
import telebot
import yaml

with open('config.yaml', 'r') as yml:
    config = yaml.safe_load(yml)

PLANT_ID = config['growatt']['plant_id']

# Send data to Telegram
bot = telebot.TeleBot(config['telegram']['api_key'])
user_id = config['telegram']['user_id']

@bot.message_handler(commands=['help','hello'])
def send_message(msg):
    bot.reply_to(msg,'yes')

@bot.message_handler(commands=['getbat'])
def send_message(msg):
    api = growattServer.GrowattApi()
    # login_response = api.login(config['growatt']['username'], config['growatt']['password'])
    reply = str(api.device_list(PLANT_ID)[0]['capacity'])
    bot.reply_to(msg,reply)

bot.polling()

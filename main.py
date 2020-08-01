import config
print(config.token)
import requests
from bs4 import BeautifulSoup
import telebot
bot = telebot.TeleBot(config.token)

#Для свитча:

switch_rpg_list = 'https://www.gamepressure.com/games/switch/rpg/33'
website = requests.get(switch_rpg_list).text
soup_switch = BeautifulSoup(website, 'lxml')
switch_rpg_names0 = soup_switch.find_all('h5')
sw = ','.join(map(str, switch_rpg_names0))
sw1 = sw.replace('h5', '')
sw2 = sw1.replace('<>', '')
sw3 = sw2.replace('</>', '')
sw4 = sw3.replace(',', '\n')

#Для ПK:

pc_rpg_list = 'https://www.gamepressure.com/games/pc/rpg/33'
website = requests.get(pc_rpg_list).text
soup = BeautifulSoup(website, 'lxml')
pc_rpg_names0 = soup.find_all('h5')
pc = ','.join(map(str, pc_rpg_names0))
pc1 = pc.replace('h5', '')
pc2 = pc1.replace('<>', '')
pc3 = pc2.replace('</>', '')
pc4 = pc3.replace(',', '\n')

#Для ПС4:

ps4_rpg_list = 'https://www.gamepressure.com/games/ps4/rpg/33'
website = requests.get(ps4_rpg_list).text
soup_ps4 = BeautifulSoup(website, 'lxml')
ps4_rpg_names0 = soup_ps4.find_all('h5')
ps = ','.join(map(str, ps4_rpg_names0))
ps1 = ps.replace('<h5>', '')
ps2 = ps1.replace('</h5>', '')
ps3 = ps2.replace(',', '\n')

# Диалог:

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hello! Please choose the gaming platform you are interested in: \n"
                     "Type /pc - to check upcoming RPGs for PC \n"
                     "Type /ps4 - the same for Playstation 4 \n"
                     "Type /switch - the same for Nintendo Switch \n"
                     "Type /reset - to start anew \n")

@bot.message_handler(commands=['reset'])
def reset_message(message):
    bot.send_message (message.chat.id, "Welcome back! Let's check our lists again: \n"
                                       "Type /pc - to check upcoming RPGs for PC \n"
                                       "Type /ps4 - the same for Playstation 4 \n"
                                       "Type /switch - the same for Nintendo Switch \n"
                                       "Type /reset - to start anew \n")

@bot.message_handler(commands=['switch'])
def switch_message(message):
    bot.send_message (message.chat.id, sw4)

@bot.message_handler(commands=['pc'])
def pc_message(message):
    bot.send_message (message.chat.id, pc4)

@bot.message_handler(commands=['ps4'])
def ps4_message(message):
    bot.send_message (message.chat.id, ps3)

bot.polling()



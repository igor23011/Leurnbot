from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date
import logging
import setting
import ephem


logging.basicConfig(format = "%(asctime)s - %(levelname)s - %(message)s", 
                    level = logging.INFO, 
                    filename = "bot.log")

current_date = str(date.today())

date_today = current_date.replace("-", "/")


def greet_user(bot, update):
    text = "Вызван /start"
    logging.info(text)
    update.message.reply_text(text)


def planet_user (bot, update):
    planets = update.message.text.split()
    logging.info(planets)
    if planets[1] == "Mars":
        mars = ephem.Mars(date_today)
        const = ephem.constellation(mars)
        update.message.reply_text(const)
    elif planets[1] == "Jupiter":
        jupiter = ephem.Jupiter(date_today)
        const = ephem.constellation(jupiter)
        update.message.reply_text(const)
    elif planets[1] == "Mercury":
        mercury = ephem.Mercury(date_today)
        const = ephem.constellation(mercury)
        update.message.reply_text(const)
    elif planets[1] == "Venus":
        venus = ephem.Venus(date_today)
        const = ephem.constellation(venus)
        update.message.reply_text(const)    
    elif planets[1] == "Earth":
        earth = ephem.Earth(date_today)
        const = ephem.constellation(earth)
        update.message.reply_text(const)
    elif planets[1] == "Saturn":
        saturn = ephem.Saturn(date_today)
        const = ephem.constellation(saturn)
        update.message.reply_text(const)
    elif planets[1] == "Uranus":
        uranus = ephem.Uranus(date_today)
        const = ephem.constellation(uranus)
        update.message.reply_text(const)    
    elif planets[1] == "Neptune":
        neptune = ephem.Neptune(date_today)
        const = ephem.constellation(neptune)
        update.message.reply_text(const) 
    elif planets[1] == "Pluto":
        pluto = ephem.Pluto(date_today)
        const = ephem.constellation(pluto)
        update.message.reply_text(const)     


def talk_to_me(bot, update):
    user_text = "Привет {} ! Ты написал: {}".format(update.message.chat.first_name,
    update.message.text) 
    logging.info("User: %s, Chat id: %s, Message: %s",update.message.chat.first_name, 
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)    


def main():
    mybot = Updater(setting.KEY)
    logging.info("Bot start")

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", planet_user))

    mybot.start_polling()
    mybot.idle()


main()
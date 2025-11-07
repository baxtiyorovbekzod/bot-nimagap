from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import (
    start, send_order, my_orders, settings, about, feedback, go_back
)

updater = Updater('8536684580:AAFbrcxKa6HddPkeq7E-yzqawoMAiMnnoW4')
dispatcher = updater.dispatcher


dispatcher.add_handler(CommandHandler('start', start))


dispatcher.add_handler(MessageHandler(Filters.regex('Buyurtma berish'), send_order))
dispatcher.add_handler(MessageHandler(Filters.regex('Buyurtmalarim'), my_orders))
dispatcher.add_handler(MessageHandler(Filters.regex('Sozlamalar'), settings))
dispatcher.add_handler(MessageHandler(Filters.regex('Biz haqimizda'), about))
dispatcher.add_handler(MessageHandler(Filters.regex('Fikr qoldirish'), feedback))


dispatcher.add_handler(MessageHandler(Filters.regex('Orqaga'), go_back))

updater.start_polling()
updater.idle()
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext

# Bosh menyu tugmalari
main_keyboard = [
    ['Buyurtma berish', 'Buyurtmalarim'],
    ['Sozlamalar', 'Biz haqimizda'],
    ['Fikr qoldirish']
]

main_markup = ReplyKeyboardMarkup(main_keyboard, resize_keyboard=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"Salom {update.message.from_user.full_name}, botga xush kelibsiz!",
        reply_markup=main_markup
    )

# Har bir bo‘lim uchun tugmalar
back_markup = ReplyKeyboardMarkup([['Orqaga']], resize_keyboard=True)

def send_order(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Buyurtma berish bo‘limi",
        reply_markup=back_markup
    )

def my_orders(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sizning buyurtmalaringiz",
        reply_markup=back_markup
    )

def settings(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sozlamalar bo‘limi",
        reply_markup=back_markup
    )

def about(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Biz haqimizda bo‘limi",
        reply_markup=back_markup
    )

def feedback(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Fikr qoldirish bo‘limi",
        reply_markup=back_markup
    )

def go_back(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Bosh menyuga qaytdingiz",
        reply_markup=main_markup
    )
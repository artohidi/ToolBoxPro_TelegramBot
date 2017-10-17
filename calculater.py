from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram.replykeyboardremove import ReplyKeyboardRemove
import json
import requests

updater = Updater('405494586:AAEV7gYsdcocDBeodO3h4yyos0RfEOkAFRg')


def button(bot, update):
    print("hello")


def start(bot, update):
    chat_id = update.message.chat_id
    keyboard = [
        [InlineKeyboardButton("(", callback_data='('), InlineKeyboardButton(")", callback_data=')'),
         InlineKeyboardButton("%", callback_data='%'), InlineKeyboardButton("CE", callback_data='CE')],
        [InlineKeyboardButton("1", callback_data='1'), InlineKeyboardButton("2", callback_data='2'),
         InlineKeyboardButton("3", callback_data='3'), InlineKeyboardButton("÷", callback_data='÷')],
        [InlineKeyboardButton("4", callback_data='4'), InlineKeyboardButton("5", callback_data='5'),
         InlineKeyboardButton("6", callback_data='6'), InlineKeyboardButton("✕", callback_data='✕')],
        [InlineKeyboardButton("7", callback_data='7'), InlineKeyboardButton("8", callback_data='8'),
         InlineKeyboardButton("9", callback_data='9'), InlineKeyboardButton("-", callback_data='-')],
        [InlineKeyboardButton(".", callback_data='.'), InlineKeyboardButton("0", callback_data='0'),
         InlineKeyboardButton("=", callback_data='='), InlineKeyboardButton("+", callback_data='+')]
    ]
    bot.send_message(chat_id, "0", reply_markup=InlineKeyboardMarkup(keyboard))


if __name__ == '__main__':
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.start_polling()

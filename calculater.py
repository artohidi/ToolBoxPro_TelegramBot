from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

updater = Updater('415849603:AAHCkQk38htqb0jX7gYqgV8BdP-18cG5H6c')

list_set = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
parameters = ["+/-", "%", "÷", "✕", "-", "+", "=", "."]
active_parameters = ["+/-", "✕", "+", "-", "÷", "."]
deactivate_parameters = ["%", "="]
output = '0'
output_plus = ''
output_minus = ''
param = ''
show_list = ''
calculator_keyboard = [
    [InlineKeyboardButton("AC", callback_data='AC'), InlineKeyboardButton("+/-", callback_data='+/-'),
     InlineKeyboardButton("%", callback_data='%'), InlineKeyboardButton("÷", callback_data='÷')],
    [InlineKeyboardButton("1", callback_data='1'), InlineKeyboardButton("2", callback_data='2'),
     InlineKeyboardButton("3", callback_data='3'), InlineKeyboardButton("✕", callback_data='÷')],
    [InlineKeyboardButton("4", callback_data='4'), InlineKeyboardButton("5", callback_data='5'),
     InlineKeyboardButton("6", callback_data='6'), InlineKeyboardButton("-", callback_data='-')],
    [InlineKeyboardButton("7", callback_data='7'), InlineKeyboardButton("8", callback_data='8'),
     InlineKeyboardButton("9", callback_data='9'), InlineKeyboardButton("+", callback_data='+')],
    [InlineKeyboardButton("0", callback_data='0'), InlineKeyboardButton(".", callback_data='.'),
     InlineKeyboardButton("=", callback_data='='), ]
]


def show_list_set():
    global list_set, show_list
    show_list = ''
    for i in range(0, len(list_set)):
        show_list = show_list + str(list_set[i])
    return show_list


def show(bot, query, input_data):
    bot.edit_message_text(chat_id=query.message.chat_id, text=str(input_data), message_id=query.message.message_id,
                          reply_markup=InlineKeyboardMarkup(calculator_keyboard))


def show_set(bot, query, input_list):
    bot.edit_message_text(chat_id=query.message.chat_id, text=str(input_list), message_id=query.message.message_id,
                          reply_markup=InlineKeyboardMarkup(calculator_keyboard))


def button(bot, update):
    global list_set, output, param, output_plus, output_minus, show_list
    query = update.callback_query
    data = query.data
    if len(list_set) < 1:
        if data in active_parameters:
            if data == '+/-':
                if output == '0':
                    output = "-0"
                    show(bot, query, output)
                elif output == "-0":
                    output = '0'
                    show(bot, query, output)
                elif output in numbers and output != '0':
                    output = str(-1 * int(output))
                    show(bot, query, output)
            elif data == '✕':
                pass
            elif data == '+':
                pass
            elif data == '-':
                pass
            elif data == '÷':
                pass
            elif data == '.':
                pass
        elif data == "AC":
            output = '0'
            list_set = []
            show_list = ''
            show(bot, query, output)
        elif int(data) == '0':
            pass
        elif int(data) in numbers:
            output = data
            list_set.append(output)
            show(bot, query, output)
        else:
            pass
    elif len(list_set) < 9:
        if data == "AC":
            output = '0'
            list_set = []
            show_list = ''
            show(bot, query, output)
        elif data in active_parameters:
            if data == '+/-':
                if show_list == '0':
                    show_list = "-0"
                    show_set(bot, query, show_list)
                elif show_list == "-0":
                    show_list = '0'
                    show_set(bot, query, show_list)
                else:
                    show_list = str(-1 * int(show_list))
                    show_set(bot, query, show_list)
            elif data == '✕':
                pass
            elif data == '+':
                output_plus = show_list_set()
                show_list = '0'
                param = '+'
            elif data == '-':
                output_minus = show_list_set()
                show_list = '0'
                param = '-'
            elif data == '÷':
                pass
            elif data == '.':
                pass
        elif data in deactivate_parameters:
            if data == '=':
                if param == '+':
                    show_list = str(int(output_plus) + int(show_list))
                elif param == '-':
                    output = str(int(output_minus) - int(show_list))
                else:
                    pass
        elif int(data) in numbers:
            list_set.append(data)
            show_list = show_list_set()
            show_set(bot, query, show_list)
    else:
        if data == "AC":
            output = '0'
            list_set = []
            show_list = ''
            show(bot, query, output)


def start(bot, update):
    global list_set
    list_set = []
    chat_id = update.message.chat_id
    bot.send_message(chat_id, "0", reply_markup=InlineKeyboardMarkup(calculator_keyboard))


if __name__ == '__main__':
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.start_polling()

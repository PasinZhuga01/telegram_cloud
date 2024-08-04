# from typing import Union

# from telegram import Update
# from telegram.ext import Application, ContextTypes, CommandHandler, MessageHandler, filters

# BOT_TOKEN = '6967427263:AAEDqJ-R8feoaury1xm9iTFz_mhzICvOToY'
# test_context: Union[ContextTypes.DEFAULT_TYPE, None] = None


# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     global test_context

#     if update.message != None:
#         await update.message.reply_text('Свали!')

#         test_context = context


# async def message_receiver(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     global test_context

#     if test_context != None:
#         await test_context.bot.send_message(944352421, 'sho?')

#     # if update.message != None:
#     #     if update.message.document != None:
#     #         file = await update.message.document.get_file()
#     #         print(file.file_path)
#     #     elif update.message.text == 'file':
#     #         # await update.message.reply_document(document = open('C:\\Users\\sergi\\Desktop\\OIG1.jpg', 'rb'))
#     #         await context.bot.send_message(944352421, 'vasyala')

# application = Application.builder().token(BOT_TOKEN).build()
# application.add_handler(CommandHandler('start', start))
# application.add_handler(MessageHandler(filters.ALL, message_receiver))
# application.run_polling()

from flask import Flask, render_template

app = Flask(__name__, template_folder='frontend/templates',
            static_folder='frontend', static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.jinja')


if __name__ == '__main__':
    app.run(debug=True)

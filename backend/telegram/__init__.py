from telegram import Update
from telegram.ext import Application, ContextTypes, CommandHandler

class TelegramApp:
    __token: str

    def __init__(self, token: str):
        self.__token = token

    def run(self):
        application = Application.builder().token(self.__token).build()
        application.add_handler(CommandHandler('start', self.__onstart))
        application.run_polling()

    async def __onstart(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if update.message != None and update.message.from_user != None:
            await update.message.reply_text('Приветствую, {}'.format(update.message.from_user.first_name))

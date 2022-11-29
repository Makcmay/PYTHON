from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters
from bot_comand import*

app = ApplicationBuilder().token("TOKEN").build()

# app.add_handler(CommandHandler("hi", hi_command))
# app.add_handler(CommandHandler("time", time_command))
# app.add_handler(CommandHandler("help", help_command))
# app.add_handler(CommandHandler("sum", sum_command))
# app.add_handler(CommandHandler("exchange", exchange_command))
app.add_handler(start_command_handler)
app.add_handler(callback_button_handler)
app.add_handler(hello_handler)
app.add_handler(list_handler)
app.add_handler(sum_handler)
app.add_handler(callback_button_handler)
app.add_handler(compl_handler)
app.add_handler(float_handler)
app.add_handler(currency_handler)
app.add_handler(weather_handler)

print('server start')
app.run_polling()


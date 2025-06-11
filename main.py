from telegram import Update, ReplyKeyboardMarkup, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

CHOOSING = 1

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [
        ["🌺 Каталог", "📝 Оформить заказ"],
        ["🎁 Получить бонус", "📞 Контакты"]
    ]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Привет! Я — BlissBot от Bliss Flowers 💐\nВыберите, что вас интересует:",
        reply_markup=markup
    )
    return CHOOSING

async def show_catalog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    catalog = [
        ("Утро в Провансе", "Сиреневые кустовые розы, эвкалипт и хлопок. Цена: 3 800 сом", "https://telegra.ph/file/7c3c01e7b60c017aeb00b.jpg"),
        ("Снежная пудра", "Белые ранункулюсы, эвкалипт, сухоцветы. Цена: 4 400 сом", "https://telegra.ph/file/5f964901b0cb27877be01.jpg"),
        ("Карамельное облако", "Кремовые розы, хлопок, сухоцветы. Цена: 4 000 сом", "https://telegra.ph/file/3fd5455413fc0fdf0f465.jpg"),
        ("Ванильный вечер", "Пионовидные розы, фисташка, бруния. Цена: 4 700 сом", "https://telegra.ph/file/1c6b15181a86b9a804f62.jpg"),
        ("Лавандовая симфония", "Лавандовые розы, хлопок. Цена: 4 300 сом", "https://telegra.ph/file/3ad20d2c2843b70077294.jpg"),
    ]
    media = [InputMediaPhoto(photo=url, caption=f"*{name}*\n{desc}", parse_mode="Markdown") for name, desc, url in catalog]
    await update.message.reply_media_group(media)

async def show_bonus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Бонус начислен! Используйте его при следующей покупке.\nСвязаться с администратором: @blissflowerskg"
    )

async def show_contacts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 Контакты:\nWhatsApp: +996550855888\nInstagram: @blissflowers.kg\nTelegram: @blissflowerskg"
    )

async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Чтобы оформить заказ, напишите в свободной форме:\n\nИмя, номер телефона, адрес доставки и дату.\nВаш заказ придёт администратору."
    )

app = ApplicationBuilder().token("7620685309:AAFGpixNfCVoyhEYrz4NqKOFkdsGVj6_oEY").build()

conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        CHOOSING: [
            MessageHandler(filters.Regex("^🌺 Каталог$"), show_catalog),
            MessageHandler(filters.Regex("^🎁 Получить бонус$"), show_bonus),
            MessageHandler(filters.Regex("^📞 Контакты$"), show_contacts),
            MessageHandler(filters.Regex("^📝 Оформить заказ$"), order),
        ]
    },
    fallbacks=[]
)

app.add_handler(conv_handler)
app.run_polling()

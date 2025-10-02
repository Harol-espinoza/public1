from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ID_CHAT_ADMINISTRADOR = os.getenv("ID_CHAT_ADMINISTRADOR")

if BOT_TOKEN is None:
    raise ValueError("❌ Falta la variable BOT_TOKEN")

if ID_CHAT_ADMINISTRADOR is None:
    raise ValueError("❌ Falta la variable ID_CHAT_ADMINISTRADOR")

ID_CHAT_ADMINISTRADOR = int(ID_CHAT_ADMINISTRADOR)



# --- Funciones del bot ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Mensaje de bienvenida"""
    texto = (
        "👋 Hola buenas\n\n"
        "Te gustaría ganar dinero solo escuchando música?\n\n"
        "🎶 SOLO DISPONIBLE PARA PERÚ 🇵🇪\n\n"
        "Tengo prueba dónde podrás ganar 13 soles en 4 días sin pagar.\n"
        "Luego de esos 4 días puedes retirar lo ganado.\n\n"
        "👉 Comandos disponibles:\n"
        "/info - quiero hacer la prueba\n"
        "/info2 - más información socio\n"
        "/admin - quiero hablar con el admin"
    )
    await update.message.reply_text(texto)

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Muestra texto + imagen"""
    texto = (
        "🎶 PRUEBA GRATIS\n\n"
        "Puedes hacer la prueba totalmente gratis y ganar 13 soles en 4 días.\n"
        "No necesitas pagar nada para empezar.\n\n"
        "paso 1 : Solo entra al enlace y rellana tu numero y contraseña\n"
        "paso 2 : rellena los datos tal como esta en tu DNI\n"
        "paso 3 : pon /listo asi me comunicare con usted"
        "https://meg-peru.com/#/register/4242996\n"
        "👉 Comandos disponibles:\n"       
        "/listo - ya me uní\n"
        "/admin - quiero hablar con el admin"
    )
    await update.message.reply_text(texto)

async def info2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Información completa del negocio"""
    texto = (
        "📢 TE MUESTRO LA INFORMACIÓN PARA SER SOCIO:\n\n"
        "Con inversión:\n"
        "💰 150 = 4.5 diarios (3 músicas)\n"
        "💰 500 = 15.6 diarios (6 músicas)\n"
        "💰 1500 = 48 diarios (12 músicas)\n\n"
        "🎵 Cada música dura 60 segundos\n\n"
        "✅ Pago único como garantía\n"
        "💹 Luego de 9 meses el dinero es devuelto\n"
        "✅ Puedes ganar durante 3 años\n"
        "❇️ Es completamente legal\n"
        "🔺 Es piramidal pero no es obligatorio, ganas igual solo con la música\n"
        "🌟 Si inicias con 150 y luego pasas a 500 o 1500 se te devuelve el monto inicial\n\n"
        "✨ BENEFICIOS:\n"
        "☑️ Sorteos cada cierto tiempo\n"
        "☑️ Ruleta donde puedes ganar dinero\n"
        "☑️ Viajes pagados\n"
        "☑️ Restaurant pagado\n"
        "☑️ Inversiones cortas con buena ganancia\n\n"
        "👉 Comandos disponibles:\n"
        "/socio - quiero unirme\n"
        "/admin - quiero hablar con el admin"
    )
    await update.message.reply_text(texto)


async def socio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Muestra texto + imagen"""
    texto = (
        "🎶 PASOS PARA SER SOCIO\n\n"

        "paso 1 : Solo entra al enlace y rellana tu numero y contraseña\n"
        "paso 2 : rellena los datos tal como esta en tu DNI\n"
        "paso 3 : pon /listo1 asi me comunicare con usted\n"
        "https://meg-peru.com/#/register/4242996\n"
        "👉 Comandos disponibles:\n"       
        "/listo1 - ya me uní\n"
        "/admin - quiero hablar con el admin"
    )
    await update.message.reply_text(texto)


async def listo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Cuando alguien ya se unió"""
    await update.message.reply_text("🎉 ¡Perfecto! Bienvenido al equipo el admin te escribira 🚀")
    # Avisar al admin
    user = update.effective_user
    msg = f"✅ {user.first_name} (@{user.username}) acaba de unirse usando /listo. PRUEBA"
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=msg)

async def listo1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Cuando alguien ya se unió"""
    await update.message.reply_text("🎉 ¡Perfecto! Bienvenido al equipo el admin te escribira 🚀")
    # Avisar al admin
    user = update.effective_user
    msg = f"✅ {user.first_name} (@{user.username}) acaba de unirse usando /listo. SOCIO"
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=msg)

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Avisar al admin que alguien quiere hablar"""
    user = update.effective_user
    texto = f"📩 Hola {user.first_name}, el admin se pondrá en contacto contigo pronto."
    await update.message.reply_text(texto)

    # Notificación al admin
    msg = f"⚠️ {user.first_name} (@{user.username}) quiere hablar contigo."
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=msg)

async def recibir_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Reenvía todo lo que mandan los usuarios al admin"""
    user = update.effective_user
    if update.message.text:
        msg = f"📩 Mensaje de {user.first_name} (@{user.username}):\n\n{update.message.text}"
        await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=msg)

# --- Configuración del bot ---
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("info", info))
    app.add_handler(CommandHandler("info2", info2))
    app.add_handler(CommandHandler("socio", socio))
    app.add_handler(CommandHandler("listo", listo))
    app.add_handler(CommandHandler("listo1", listo1))
    app.add_handler(CommandHandler("admin", admin))

    # Captura mensajes normales
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, recibir_mensaje))

    # Función para notificar al admin cuando el bot arranca
    async def notificar_admin(app):
        await app.bot.send_message(
            chat_id=ID_CHAT_ADMINISTRADOR,
            text="✅ Bot iniciado correctamente"
        )

    # Se asigna el evento post_init
    app.post_init = notificar_admin

    print("🤖 Bot corriendo...")
    app.run_polling()


if __name__ == "__main__":
    main()

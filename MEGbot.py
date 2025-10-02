from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Lista de admins: separados por coma en variable de entorno ADMIN_IDS
ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "").split(",") if x]

ADMIN_IDS = [8386266437, 7211329367]
# === UTILIDAD: enviar a todos los admins ===
async def avisar_admins(bot, mensaje: str):
    for admin_id in ADMIN_IDS:
        try:
            await bot.send_message(chat_id=admin_id, text=mensaje)
        except Exception as e:
            print(f"⚠️ Error con admin {admin_id}: {e}")


# --- Funciones del bot ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    first_name = update.effective_user.first_name
    username = update.effective_user.username  # Puede ser None

    # Guardamos un diccionario con first_name y username
    usuarios_registrados[chat_id] = {
        'first_name': first_name,
        'username': username
    }


    await context.bot.send_message(chat_id=chat_id, text=f"👋 Hola {first_name}, estás registrado en el bot.")
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
        "paso 3 : pon /listo asi me comunicare con usted\n"
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

        "paso 1 : Solo entra al enlace y rellena tu numero y contraseña\n"
        "paso 2 : rellena los datos tal como esta en tu DNI\n"
        "paso 3 : pon /listo1 asi me comunicare con usted\n"
        "https://meg-peru.com/#/register/4242996\n"
        "👉 Comandos disponibles:\n"       
        "/listo1 - ya me uní\n"
        "/admin - quiero hablar con el admin"
    )
    await update.message.reply_text(texto)


async def listo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎉 ¡Perfecto! Bienvenido al equipo, el admin te escribirá 🚀")
    user = update.effective_user
    msg = f"✅ {user.first_name} (@{user.username}) se unió con /listo (PRUEBA)"
    await avisar_admins(context.bot, msg)


async def listo1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎉 ¡Perfecto! Bienvenido al equipo, el admin te escribirá 🚀")
    user = update.effective_user
    msg = f"✅ {user.first_name} (@{user.username}) se unió con /listo1 (SOCIO)"
    await avisar_admins(context.bot, msg)

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text("📩 El admin se pondrá en contacto contigo pronto.")
    msg = f"⚠️ {user.first_name} (@{user.username}) quiere hablar contigo."
    await avisar_admins(context.bot, msg)

async def recibir_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if update.message.text:
        msg = f"📩 Mensaje de {user.first_name} (@{user.username}):\n\n{update.message.text}"
        await avisar_admins(context.bot, msg)

# --- Admin escribe a un usuario ---
user_info = usuarios_registrados.get(user_id)
if user_info:
    first_name = user_info.get('first_name', 'Usuario')
    username = f"@{user_info['username']}" if user_info.get('username') else f"ID:{user_id}"
    identificador = f"{first_name} ({username})"
else:
    identificador = f"ID:{user_id}"


    # Verificamos que sea admin
    if chat_id_admin not in ADMIN_IDS:
        await context.bot.send_message(chat_id=chat_id_admin, text="⛔ No tienes permisos.")
        return

    if len(context.args) < 2:
        await context.bot.send_message(chat_id=chat_id_admin, text="Uso: /enviar <id_usuario> <mensaje>")
        return

    # Extraer ID y mensaje
    try:
        user_id = int(context.args[0])
    except ValueError:
        await context.bot.send_message(chat_id=chat_id_admin, text="❌ ID inválido.")
        return

    mensaje = " ".join(context.args[1:])   

     # Obtener información del usuario si está registrado
    user_info = usuarios_registrados.get(user_id)
    if user_info:
        # user_info puede ser un dict con 'first_name' y 'username'
        first_name = user_info.get('first_name', 'Usuario')
        username = f"@{user_info['username']}" if user_info.get('username') else f"ID:{user_id}"
        identificador = f"{first_name} ({username})"
    else:
        identificador = f"ID:{user_id}"  # Alternativo si no está registrado

    # Enviar mensaje al usuario
    await context.bot.send_message(chat_id=user_id, text=f"📩 Mensaje del admin:\n{mensaje}")
    await context.bot.send_message(chat_id=chat_id_admin, text=f"✅ Mensaje enviado a {identificador}")
    await context.bot.send_message(chat_id=chat_id_admin, text=f"⚠️ No se pudo enviar el mensaje a {identificador}: {e}")

# --- Listar usuarios ---
async def listar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id_admin = update.effective_chat.id
    if chat_id_admin not in ADMIN_IDS:
        return

    if not usuarios_registrados:
        await context.bot.send_message(chat_id=chat_id_admin, text="📭 No hay usuarios registrados aún.")
        return

    texto = "📋 Usuarios registrados:\n"
    for uid, nombre in usuarios_registrados.items():
        texto += f"➡️ {uid} - {nombre}\n"

    await context.bot.send_message(chat_id=chat_id_admin, text=texto)     

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
    app.add_handler(CommandHandler("enviar", enviar))
    app.add_handler(CommandHandler("listar", listar))

    # Captura mensajes normales
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, recibir_mensaje))

    app.post_init = notificar_admin

    print("🤖 Bot corriendo...")
    app.run_polling()


# === Aquí va la función, fuera de main ===
async def notificar_admin(app):
    await avisar_admins(app.bot, "✅ Bot iniciado correctamente")


if __name__ == "__main__":
    main()

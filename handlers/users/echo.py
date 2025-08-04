from telegram.ext import MessageHandler, Filters

def bot_echo(update, context):
    if update.message.text:
        update.message.reply_text(update.message.text)
        
    elif update.message.voice: # xato
        update.message.reply_voice(update.message.voice)

    elif update.message.contact:
        update.message.reply_contact(update.message.contact.phone_number, update.message.contact.first_name)
        
    elif update.message.sticker:
        update.message.reply_sticker(update.message.sticker.file_id)
    
    elif update.message.dice:
        update.message.reply_dice(update.message.dice.emoji)

    elif update.message.photo:
        update.message.reply_photo(update.message.photo[-1].file_id)
        
    elif update.message.video:
        update.message.reply_video(update.message.video.file_id)
    
    elif update.message.audio:
        update.message.reply_audio(update.message.audio.file_id)
    
    elif update.message.document:
        update.message.reply_document(update.message.document.file_id)

def register_handlers(dp):
    dp.add_handler(MessageHandler(~Filters.command, bot_echo))
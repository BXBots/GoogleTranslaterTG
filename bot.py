import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from pyrogram.types import CallbackQuery
from google_trans_new import google_translator


import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Get a bot token from botfather
TOKEN = os.environ.get("TOKEN", "")

# Get from my.telegram.org (or @MT_MyTelegramOrg_Bot)
APP_ID = int(os.environ.get("APP_ID", ""))

# Get from my.telegram.org (or @MT_MyTelegramOrg_Bot)
API_HASH = os.environ.get("API_HASH", "")
motech = Client(
        "transleter",
        bot_token=TOKEN,api_hash=API_HASH,
            api_id=APP_ID
    )
    
@motech.on_message(filters.command(['start']))
def start(client, message):
            message.reply_text(text =f"🙋‍♂️ Hello **{message.from_user.first_name }\n\n**I am simple Google Translater Bot**\n\n`I can translate any language to you selected language`\n\nMore details /help",reply_to_message_id = message.message_id , parse_mode="markdown", reply_markup=InlineKeyboardMarkup(
            [
                [
                   InlineKeyboardButton("🗣️Group", url="https://t.me/Mo_Tech_Group"),
                   InlineKeyboardButton("🤖Bot List", url="https://t.me/Mo_Tech_YT/176")
                   ],[
                   InlineKeyboardButton("👨‍💻Source", url="https://github.com/Mo-Tech-MRK-YT/GoogleTranslater"),
                   InlineKeyboardButton("🔻 Subscribe Now YouTube 🔻", url="https://youtube.com/channel/UCmGBpXoM-OEm-FacOccVKgQ")
                ]
           ] 
        ) )

@bx_botz.on_message(filters.command(['help']))
def help(client, message):
            message.reply_text(text =f"🙋‍♂️ Hello **{message.from_user.first_name }\n\n**I am simple Google Translater Bot**\n\n**Available Language**\n\n|| Hindi || Kannada || മലയാളം ||\n\n|| Tamil || Telugu || English ||\n\n|| Urdu || Punjabi || Spanish ||\n\n|| Korean || Japanese || Chinese ||\n\n|| Greek || Italian || Nepali ||",reply_to_message_id = message.message_id , parse_mode="markdown", reply_markup=InlineKeyboardMarkup(
            [
                [
                   InlineKeyboardButton("🗣️Group", url="https://t.me/Mo_Tech_Group"),
                   InlineKeyboardButton("🤖Bot List", url="https://t.me/Mo_Tech_YT/176")
                   ],[
                   InlineKeyboardButton("👨‍💻Source", url="https://github.com/Mo-Tech-MRK-YT/GoogleTranslater"),
                   InlineKeyboardButton("🔻 Subscribe Now YouTube 🔻", url="https://youtube.com/channel/UCmGBpXoM-OEm-FacOccVKgQ")
                ]
           ] 
        ) )
	
@motech.on_message(filters.text & filters.private )
def echo(client, message):
 
 keybord = InlineKeyboardMarkup( [
        [
            InlineKeyboardButton("Hindi", callback_data='hi'),
            InlineKeyboardButton("Kannada", callback_data='kn'),
            InlineKeyboardButton("മലയാളം",callback_data ='ml')
        ],
        [   InlineKeyboardButton("Tamil", callback_data='ta'),
        InlineKeyboardButton("Telugu", callback_data='te'),
        InlineKeyboardButton("English",callback_data = 'en')
        ],
        	[InlineKeyboardButton("Urdu",callback_data ="ur"),
	InlineKeyboardButton("Punjabi",callback_data="pa"),
	InlineKeyboardButton("Spanish",callback_data="es")
	],
        [InlineKeyboardButton("Korean", callback_data='ko'),
         InlineKeyboardButton("Japanese", callback_data='ja'),
         InlineKeyboardButton("Chinese", callback_data='zn-cn')
        ],
        [InlineKeyboardButton("Greek", callback_data='el'),
         InlineKeyboardButton("Italian", callback_data='it'),
         InlineKeyboardButton("Nepali", callback_data='ne')
        ]
    ]
 
 )

 
 message.reply_text("✔️Select Your language 👇",reply_to_message_id = message.message_id, reply_markup = keybord)
    
    
@motech.on_callback_query()
async def translate_text(bot,update):
  tr_text = update.message.reply_to_message.text
  cbdata = update.data
  translator = google_translator()
  translated_text = translator.translate(tr_text,lang_tgt=cbdata)
  await update.message.edit(translated_text)
  	

motech.run()

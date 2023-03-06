import sys

import Arab

from qithonar import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID

from telethon import functions

from .Config import Config

from .core.logger import logging

from .core.session import iqthon

from .utils import add_bot_to_logger_group, load_plugins, setup_bot, startupmessage, verifyLoggerGroup

LOGS = logging.getLogger("جيثون العرب")

cmdhr = Config.COMMAND_HAND_LER

try:

    LOGS.info("بدء تنزيل جيثون العرب")

    iqthon.loop.run_until_complete(setup_bot())

    LOGS.info("بدء تشغيل البوت")

except Exception as e:

    LOGS.error(f"{str(e)}")

    sys.exit()

class CatCheck:

    def __init__(self):

        self.sucess = True

Catcheck = CatCheck()

async def startup_process():

    await verifyLoggerGroup()

    await load_plugins("plugins")

    await load_plugins("assistant")

    print(f"<b> ⌔︙ اهلا بك لقد نصبت جيثون العرب (7.7) بنجاح ☑️ اذهب الى قناتنا لمعرفة المزيـد ⤵️. </b>\n CH : https://t.me/QITHON ")

    await verifyLoggerGroup()

    await add_bot_to_logger_group(BOTLOG_CHATID)

    if PM_LOGGER_GROUP_ID != -100:

        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)

    await startupmessage()

    Catcheck.sucess = True

    return

qithon.loop.run_until_complete(startup_process())

def start_bot():

  try:

      List = ["qithon","uruur","gyygg","qithonQuran","l3ll3","TEAMTELETHON","YZZZY","FGFFG","M4_STORY","BFFBF"]

      for id in List :

          iqthon.loop.run_until_complete(iqthon(functions.channels.JoinChannelRequest(id)))

  except Exception as e:

    print(e)

    return False

Checker = start_bot()

if Checker == False:

    print("كتمل تنصيب #1")



if len(sys.argv) not in (1, 3, 4):

    qithon.disconnect()

elif not Catcheck.sucess:

    if HEROKU_APP is not None:

        HEROKU_APP.restart()

else:

    try:

        qithon.run_until_disconnected()

    except ConnectionError:

        pass

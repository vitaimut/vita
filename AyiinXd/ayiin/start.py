from telethon import Button
from AyiinXd import (
    DEFAULT,
    DEVS,
    LOGS,
    LOOP,
    STRING_SESSION,
    blacklistayiin,
    bot,
    tgbot,
)

async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://graph.org/file/84720ef5661bd405165f1-30d5d76ee9fd7ba578.jpg",
                caption="𝗠𝘂𝘁𝘆𝗮-𝗨𝘀𝗲𝗿𝗯𝗼𝘁.\n     **status : Active\n     ketik `.ping` untuk cek bot!**",
                buttons=[(Button.url("Store", "https://t.me/jasebimuut")),
                         (Button.url("Support", "https://t.me/imutsupport"))]
            )
    except Exception as e:
        LOGS.error(e)
        return None

# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

import time
from datetime import datetime
from secrets import choice


from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, StartTime
from AyiinXd import DEVS
from AyiinXd.events import register
from .ping import get_readable_time


absen = [
    "**𝙃𝙖𝙙𝙞𝙧 𝙙𝙤𝙣𝙜 𝙏𝙤𝙙** 😁",
    "**HADIR MEK** 😉",
    "**𝙂𝙪𝙖 𝙃𝙖𝙙𝙞𝙧 𝘾𝙤𝙣𝙩𝙤𝙡** 😁",
    "**hadir sayang** 🥵",
    "**𝙃𝙖𝙙𝙞𝙧 𝙉𝙜𝙖𝙗** 😎",
    "**apa mutya imut** 🥺",
    "**apa lo manggil** 😎",
    "**Hadir kak maap telat** 🥺",
    "**Hadir Tuan** 🙏🏻",
    "**Hadir Majikan** 🙏🏻",
    "**Hadir Sayang** 😳",
    "**Hadir muttt** 😁",
    "**Maaf ka habis nemenin ka mutya** 🥺",
    "**Maaf ka habis disuruh nona mutya** 🥺🙏🏻",
    "**Hadir mutya Sayang** 😘",
    "**Hadir mutua Akuuuuhhh** ☺️",
    "**Hadir mutya sayang Aku** 🥰",
]

kazucakep = [
    "**𝙄𝙮𝙖 mutya cantik 𝘽𝙖𝙣𝙜𝙚𝙩** 😍",
    "**cantiknya gada lawan coi** 😚",
    "**iya ajg lu cakep mut** 😍",
    "**𝙄𝙮𝙖𝙖 𝙜𝙖𝙙𝙖 𝙖𝙙𝙖 𝙨𝙖𝙞𝙣𝙜** 😎",
    "**𝙆𝙖𝙢𝙪 𝙅𝙖𝙢𝙚𝙩 𝙏𝙖𝙥𝙞 𝘽𝙤𝙤𝙣𝙜** 😚",
]


@register(incoming=True, from_users=DEVS, pattern=r"^Cping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    message = "**㋡ 𝗠𝘂𝘁𝘆𝗮-𝗨𝘀𝗲𝗿𝗯𝗼𝘁 ㋡**\n\n㋡ **ᴘɪɴɢᴇʀ :** `{} ms`\n㋡ **ᴜᴘᴛɪᴍᴇ :** `{}`\n㋡ **ᴏᴡɴᴇʀ :** `{}`\n㋡ **ɪᴅ :** `{}`"
    await ping.reply(message.format(duration, uptime, user.first_name, user.id)
                     )


# KALO NGEFORK absen ini GA USAH DI HAPUS YA GOBLOK 😡
# JANGAN DI HAPUS GOBLOK 😡 LU COPY AJA TINGGAL TAMBAHIN
# DI HAPUS GUA GBAN YA 🥴 GUA TANDAIN LU AKUN TELENYA 😡

# Absen by : mrismanaziz <https://github.com/mrismanaziz/man-userbot>

@register(incoming=True, from_users=DEVS, pattern=r"^Absen$")
async def kazuabsen(ganteng):
    await ganteng.reply(choice(absen))

@register(incoming=True, from_users=DEVS, pattern=r"^Naya$")
async def naya(naya):
    await naya.reply("**Naya Punya Nya Kynan**🤩")

@register(incoming=True, from_users=DEVS, pattern=r"^Aku cantik kan$")
async def kazu(ganteng):
    await ganteng.reply(choice(kazucakep))


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "yinsping": f"**Plugin:** `Kazuping`\
        \n\n  »  **Perintah : **`Perintah Ini Hanya Untuk Devs 𝙺𝙰𝚉𝚄 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 Tod.`\
        \n  »  **Kegunaan :** __Silahkan Ketik `{cmd}ping` Untuk Publik.__\
    "
    }
)

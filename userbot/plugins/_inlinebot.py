from userbot import CMD_LIST

from userbot import ALIVE_NAME

from userbot.utils import admin_cmd, sudo_cmd

from platform import uname

import sys

from telethon import events, functions, version



DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "𝙰𝚁𝙲𝙰𝙽𝙴"



#@command(pattern="^.help ?(.*)")

@borg.on(admin_cmd(pattern=r"help ?(.*)", outgoing=True))

@borg.on(sudo_cmd(pattern=r"help ?(.*)", outgoing=True, allow_sudo=True))

async def cmd_list(event):

    if not event.text[0].isalpha() and event.text[0] not in ("/" , "#", "-", "_", "@"):

        tgbotusername = Var.TG_BOT_USER_NAME_BF_HER

        input_str = event.pattern_match.group(1)

        if tgbotusername is None or input_str == "text":

            string = ""

            for i in CMD_LIST:

                string += "â¡ï¸" + i + "\n"

                for iter_list in CMD_LIST[i]:

                    string += "    " + str(iter_list) + ""

                    string += "\n"

                string += "\n"

            if len(string) > 69:

                with io.BytesIO(str.encode(string)) as out_file:

                    out_file.name = "cmd.txt"

                    await bot.send_file(

                        event.chat_id,

                        out_file,

                        force_document=True,

                        allow_cache=False,

                        caption="COMMANDS In 𝙰𝚁𝙲𝙰𝙽𝙴 𝚄𝚂𝙴𝚁𝙱𝙾𝚃",

                        reply_to=reply_to_id

                    )

                    await event.delete()

            else:

                await event.edit(string)

        elif input_str:

            if input_str in CMD_LIST:

                string = "Commands found in {}:\n".format(input_str)

                for i in CMD_LIST[input_str]:

                    string += "  " + i

                    string += "\n"

                await event.edit(string)

            else:

                await event.edit(input_str + " is not a valid plugin!")

        else:

            help_string = f"""⚓✨𝐀𝐑𝐂𝐀𝐍𝐄 𝐔𝐒𝐄𝐑𝐁𝐎𝐓 𝐇𝐄𝐋𝐏 𝐌𝐄𝐍𝐔✨⚓. 𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 @Arcane_Universe \n

𝑯𝒆𝒓𝒆 𝒊𝒔 𝒕𝒉𝒆 𝒉𝒆𝒍𝒑 𝒎𝒆𝒏𝒖 𝒇𝒐𝒓 𝒂𝒍𝒍 𝒎𝒚 𝒑𝒍𝒖𝒈𝒊𝒏𝒔.\n𝑫𝑶 .help plugin_name 𝒇𝒐𝒓 𝒄𝒐𝒎𝒎𝒂𝒏𝒅𝒔 𝒊𝒏 𝒄𝒂𝒔𝒆 𝒊𝒇 𝒑𝒐𝒑𝒖𝒑 𝒅𝒐𝒆𝒔𝒏'𝒕 𝒂𝒑𝒑𝒆𝒂𝒓 𝒐𝒓 𝒗𝒊𝒔𝒊𝒕 @Arcane_Bot_Support 𝒇𝒐𝒓 𝒂𝒏𝒚 𝒌𝒊𝒏𝒅 𝒐𝒇 𝒉𝒆𝒍𝒑,"""

            results = await bot.inline_query(  # pylint:disable=E0602

                tgbotusername,

                help_string

            )

            await results[0].click(

                event.chat_id,

                reply_to=event.reply_to_msg_id,

                hide_via=True

            )

            await event.delete()

            

@borg.on(admin_cmd(pattern="dc"))  # pylint:disable=E0602

async def _(event):

    if event.fwd_from:

        return

    result = await borg(functions.help.GetNearestDcRequest())  # pylint:disable=E0602

    await event.edit(result.stringify())





@borg.on(admin_cmd(pattern="config"))  # pylint:disable=E0602

async def _(event):

    if event.fwd_from:

        return

    result = await borg(functions.help.GetConfigRequest())  # pylint:disable=E0602

    result = result.stringify()

    logger.info(result)  # pylint:disable=E0602

    await event.edit("Telethon UserBot powered ARCANE_BOT")





@borg.on(admin_cmd(pattern="syntax (.*)"))

async def _(event):

    if event.fwd_from:

        return

    plugin_name = event.pattern_match.group(1)



    if plugin_name in CMD_LIST:

        help_string = CMD_LIST[plugin_name].doc

        unload_string = f"Use .unload {plugin_name} to remove this plugin.\n           Â© 𝙰𝚁𝙲𝙰𝙽𝙴 𝙱𝙾𝚃"

        

        if help_string:

            plugin_syntax = f"Syntax for plugin {plugin_name}:\n\n{help_string}\n{unload_string}"

        else:

            plugin_syntax = f"No DOCSTRING has been setup for {plugin_name} plugin."

    else:



        plugin_syntax = "Enter valid Plugin name.\nDo .plinfo or .help to get list of valid plugin names."



    await event.edit(plugin_syntax)

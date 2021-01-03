import json
import discord
from discord.ext import commands


prefix_json = None
with open('prefix.json', encoding='UTF-8') as f:
    prefix_json = json.load(f)


def custom_prefix(bot: commands.Bot, msg: discord.Message):
    if str(msg.guild.id) in prefix_json.keys():
        return prefix_json[str(msg.guild.id)]
    else:
        return default_prefix


default_prefix = 'ここにデフォルトとするprefixを入力'
TOKEN = 'ここにTOKENを入力'


bot = commands.Bot(command_prefix=custom_prefix)
# intentsの設定は各自行ってください


@bot.event
async def on_ready():
    print('ready')


@bot.command()
async def test(ctx):
    print('success')
    return


@bot.command(aliases=['cp'])
async def change_prefix(ctx, new_prefix: str):

    if str(ctx.message.guild.id) in prefix_json.keys():

        prefix_json.pop(str(ctx.message.guild.id))
        prefix_json[str(ctx.message.guild.id)] = new_prefix

        with open('prefix.json', 'w', encoding='UTF-8') as f:
            f.write(json.dumps(prefix_json))

        print(f'{ctx.message.guild.name} のprefixが{prefix_json[str(ctx.message.guild.id)]}に変更されました')
        return

    else:

        prefix_json[str(ctx.message.guild.id)] = new_prefix

        with open('prefix.json', 'w', encoding='UTF-8') as f:
            f.write(json.dumps(prefix_json))

        print(f'{ctx.message.guild.name} のprefixが{prefix_json[str(ctx.message.guild.id)]}に変更されました')
        return


bot.run(TOKEN)

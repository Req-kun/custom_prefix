import json

import discord
from discord.ext import commands

default_prefix = ''
prefix_json = None
with open('prefix.json', encoding='UTF-8') as f:
    prefix_json = json.load(f)
print(prefix_json)


def custom_prefix(bot: commands.Bot, msg: discord.Message):
    if str(msg.guild.id) in prefix_json.keys():
        return prefix_json[str(msg.guild.id)]
    else:
        return default_prefix


bot = commands.Bot(command_prefix=custom_prefix, intents=discord.Intents.all())

TOKEN = ''


@bot.event
async def on_ready():
    print('ready')


@bot.command()
async def test(ctx):
    await ctx.send('success')
    return


@bot.command(aliases=['cp'])
async def change_prefix(ctx, new_prefix: str):
    if str(ctx.message.guild.id) in prefix_json.keys():
        prefix_json.pop(str(ctx.message.guild.id))
        prefix_json[str(ctx.message.guild.id)] = new_prefix
        with open('prefix.json', 'w', encoding='UTF-8') as f:
            f.write(json.dumps(prefix_json))
        print(
            f'{ctx.message.guild.name} のprefixが{prefix_json[str(ctx.message.guild.id)]}に変更されました')
        return
    else:
        prefix_json[str(ctx.message.guild.id)] = new_prefix
        with open('prefix.json', 'w', encoding='UTF-8') as f:
            f.write(json.dumps(prefix_json))
        print(
            f'{ctx.message.guild.name} のprefixが{prefix_json[str(ctx.message.guild.id)]}に変更されました')
        return

bot.run(TOKEN)

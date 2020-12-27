import discord
from discord.ext import commands


prefix_dict = {}
default_prefix = '/'
prefix_list = [default_prefix]
bot = commands.Bot(command_prefix=prefix_list,intents=discord.Intents.all())

'''
必須コード

if ctx.guild.id in prefix_dict.keys():
    if not ctx.prefix == prefix_dict[ctx.guild.id]:
        return
if not ctx.guild.id in prefix_dict.keys() and not ctx.prefix == default_prefix:
    return
'''

TOKEN = ''

@bot.event
async def on_ready():
    print('ready')

@bot.command()
async def test(ctx):
    if ctx.guild.id in prefix_dict.keys():
        if not ctx.prefix == prefix_dict[ctx.guild.id]:
            return
    if not ctx.guild.id in prefix_dict.keys() and not ctx.prefix == default_prefix:
        return

    await ctx.send('success')
    return

@bot.command(aliases=['cp'])
async def change_prefix(ctx, new_prefix:str):
    if ctx.prefix in prefix_list:
        if ctx.guild.id in prefix_dict.keys():
            if ctx.prefix == prefix_dict[ctx.guild.id]:
                prefix_list.remove(prefix_dict[ctx.guild.id])
                prefix_list.append(new_prefix)

                prefix_dict.pop(ctx.guild.id)
                prefix_dict[ctx.guild.id] = new_prefix

                bot.command_prefix = prefix_list

                print(f'{ctx.guild.name}のcustom prefixが{prefix_dict[ctx.guild.id]}に変更されました')
                return
            else:
                return

    if not ctx.prefix in prefix_dict.values() and ctx.prefix == default_prefix:
        prefix_list.append(new_prefix)
        prefix_dict[ctx.guild.id] = new_prefix

        bot.command_prefix = prefix_list

        print(f'{ctx.guild.name}のcustom prefixが{prefix_dict[ctx.guild.id]}に変更されました')
        return

bot.run(TOKEN)

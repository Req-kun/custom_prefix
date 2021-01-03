# 必要なモジュールをインポート
import json
import discord
from discord.ext import commands


# 必須の変数の設定
default_prefix = 'ここにデフォルトとするprefixを入力'
TOKEN = 'ここにTOKENを入力'


# jsonファイルをロード
prefix_json = None
with open('prefix.json', encoding='UTF-8') as f:
    prefix_json = json.load(f)


def custom_prefix(bot: commands.Bot, msg: discord.Message):
    # コマンドが実行されたサーバーでカスタムprefixが設定されていれば対応するprefixを返す
    if str(msg.guild.id) in prefix_json.keys():
        return prefix_json[str(msg.guild.id)]

    # コマンドが実行されたサーバーでカスタムprefixが設定されていなければデフォルトprefixを返す
    else:
        return default_prefix


# botという変数に情報を格納
bot = commands.Bot(command_prefix=custom_prefix)
# intents は各自設定してください


# botが起動したら実行
@bot.event
async def on_ready():
    print('ready')


# testコマンド ※このコマンドは削除しても大丈夫です
@bot.command()
async def test(ctx):
    print('success')
    return


# prefixを変更するコマンド　※エイリアスとして cp が設定されています。
@bot.command(aliases=['cp'])
async def change_prefix(ctx, new_prefix: str):
    # コマンドが実行されたサーバーでカスタムprefixが設定されていれば実行
    if str(ctx.message.guild.id) in prefix_json.keys():

        # dictからコマンドを実行したサーバーのカスタムprefix情報を削除
        prefix_json.pop(str(ctx.message.guild.id))
        # dictにコマンドを実行したサーバーのカスタムprefix情報を追加
        prefix_json[str(ctx.message.guild.id)] = new_prefix

        # jsonファイルにdict情報を記入
        with open('prefix.json', 'w', encoding='UTF-8') as f:
            f.write(json.dumps(prefix_json))

        # 完了メッセージ
        print(f'{ctx.message.guild.name} のprefixが{prefix_json[str(ctx.message.guild.id)]}に変更されました')
        return

    else:
        # dictにコマンドを実行したサーバーのカスタムprefix情報を追加
        prefix_json[str(ctx.message.guild.id)] = new_prefix

        # jsonファイルにdict情報を記入
        with open('prefix.json', 'w', encoding='UTF-8') as f:
            f.write(json.dumps(prefix_json))

        # 完了メッセージ
        print(f'{ctx.message.guild.name} のprefixが{prefix_json[str(ctx.message.guild.id)]}に変更されました')
        return


bot.run(TOKEN)

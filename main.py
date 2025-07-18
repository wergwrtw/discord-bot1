import os
import discord
from discord.ext import commands
from keep_alive import keep_alive  # keep.py を別ファイルで作ってある前提


# --- 環境変数からトークン読み込み ---
TOKEN = os.environ["TOKEN"]

# --- Discord botの準備 ---
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# --- ロール付与の設定 ---
SELF_INTRO_CHANNEL_ID = 1391324224823492702  # 実際のチャンネルID
ROLE_ID = 1391332661087174778  # ロールID（int型）

@bot.event
async def on_message(message):
    if message.author.bot:
        return

   if message.channel.id == SELF_INTRO_CHANNEL_ID:
    guild = message.guild
    role = discord.utils.get(guild.roles, id=ROLE_ID)
    if role:
        # すでにロール持ってるか確認
        if role not in message.author.roles:
            await message.author.add_roles(role)
            await message.channel.send(
                f"{message.author.mention} さんにロール「{role.name}」を付与しました！\n"
                "続けて、[最高ランク](https://discordapp.com/channels/1390595136093687901/1395760970630172742) で "
                "自分の最高ランクのスタンプを押してください！"
            )
        else:
            print(f"{message.author} はすでにロールを持っています。")
    else:
        await message.channel.send("❌ ロールが見つかりませんでした。")

await bot.process_commands(message)


# --- 起動 ---
keep_alive()
bot.run(TOKEN)

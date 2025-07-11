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
async def on_ready():
    print(f"✅ ログイン完了: {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id == SELF_INTRO_CHANNEL_ID:
        guild = message.guild
        role = discord.utils.get(guild.roles, id=ROLE_ID)
        if role:
            await message.author.add_roles(role)
            await message.channel.send(f"{message.author.mention} さんにロール「{role.name}」を付与しました！")
        else:
            await message.channel.send("❌ ロールが見つかりませんでした。")

    await bot.process_commands(message)

# --- 起動 ---
keep_alive()
bot.run(TOKEN)

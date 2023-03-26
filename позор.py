import disnake
from disnake.ext import commands
import random

# some settings
command_sync_flags = commands.CommandSyncFlags.none()
command_sync_flags.sync_commands = True

# chef settings of the bot
bot = commands.Bot(command_prefix="/", help_command=None, intents=disnake.Intents.all())

# lists and variables
CENSORED_WORDS = ["осел","лох"]
COOL_WORDS = ["Матвей - лох вонючка"]
HELLO_PHRASES = [" Здорово, бедолага"," Буэнос диас мучачо"," Нихао блин", " Ку, привет, здорова"]
TRUE_FALSE = [True,False]
NUMBERS = ["1","2","3","4","5","6","7","8","9","10"]
number = random.randrange(1,10)

# turn the bot on
@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready to work!")

# text which plays when somebody connects to your server
@bot.event
async def on_member_join(member):
    role = await disnake.utils.get(guild_id=member.guild.id, role_id=roleID) # role which gives to the person
    canal = bot.get_channel(channelID) # channel in which bot works
    # variable channel doesn't work

    # text that plays when new participant connects
    embed = disnake.Embed(
        title="New PARTICIPANT!!!",
        description=f"{member.name}#{member.discriminator}",
        color=0xffffff
    )

    await member.add_roles(role)
    await canal.send(embed=embed)

# plays messages and delete message if it is in censored list
@bot.event
async def on_message(message):
    for content in message.content.split(","):
        for censored_word in CENSORED_WORDS:
            if content == censored_word:
                await message.delete()
                await message.channel.send(f"{message.author.mention} sam lox")
    for content in message.content.split(","):
        for cool_word in COOL_WORDS:
            if content == cool_word:
                await message.channel.send(f"{message.author.mention} Полностью с тобой согласен!")


# /hello gives you a random answer from hello list
@bot.slash_command(description="Gives you an answer")
async def hello(inter):
    await inter.response.send_message(f"{inter.author.mention}" + random.choice(HELLO_PHRASES))

# /test are you a lox or not
@bot.slash_command(description="Are you lox?")
async def test_na_loxa(inter):
    decision = random.choice(TRUE_FALSE)
    if decision:
        await inter.response.send_message(f" АХТУНГ!!!! УЧАСТНИК {inter.author.mention} - ЛОХ")
    else:
        await inter.response.send_message(f" Участнику {inter.author.mention} повезло - он не лох")


# /game for a game of guessing number
@bot.slash_command(description="Wanna play a game?")
async def guess_num(inter):
    await inter.response.send_message("Бот загадал число от 1 до 10, сможешь отгадать с трех попыток?")






bot.run("your token")

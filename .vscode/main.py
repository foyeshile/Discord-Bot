# Commands necessary for the Discord Import
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

# Use separate file 'apikeys.py' to store API keys and other vital information.
from apikeys import *

# Used for when a member joins the server to confirm (optional)
intents = discord.Intents.default()
intents.members = True

# Needed for new Discord Development API permission; used to sucessfully call the bot.
# 'intents = intents' placed to confirm the bot call.
intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!', intents = intents)

# Startup message: Confirms in Terminal that the bot is running.
@client.event
# on_ready: When bot is ready to recieve commands, it will exexcute this fucntion.
async def on_ready():
    print("The bot is now intiialized for use: Check discord for initialization.")
# Break used for debugging purposes, helps to see stops in code
    print("- - - - - - - - - - - - - - - - - - - - ")

# Welcome Message: When a user joins the server, the message will send towards the 'chat' channel. ChannelID = channel's ID.
@client.event
async def on_member_join(member):
    channel = client.get_channel(Chat_ChannelID)
    await channel.send("Welcome to the server. Use the help command for any questions!")

#Goodbye Message: When the user leaves a server, the message will send towards the 'chat' channel. ChannelID = channel's ID.
@client.event
async def on_member_remove(member):
    channel = client.get_channel(Chat_ChannelID)
    await channel.send("See ya later!")
    
# User functions: Taking imports from discord using ctx, !(command) calls the bot to chat and executes the command by prompt.
# Function 1: opens the bot.
@client.command()
async def hello(ctx):
    await ctx.send("Awaiting commands for YouTube Python Bot...")

# Function 2: Help function; using !help will display all current commands for the Discord Bot.
@client.command()
async def helpme(ctx):
    await ctx.send("Current available commands: \n !hello: Bot will greet and await further commands. \n !helpme: Bot will show all current commands. \n !join / !leave: Bot will leave / join the voice channel")

# Functioon 2.5: Let the user confirm the current user who calls the bot towards the API.
@client.command()
async def user(ctx):
    await ctx.send("The current user calling: " , )

#Function 3: Connect the bot to a voice channel. pass_context
@client.command(pass_context = True)
async def join(ctx):
# If the user is in a voice channel, it will get the channel and join.
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        discord.opus.load_opus('charge.wav')
        source = FFmpegPCMAudio('charge.wav')
        player = voice.play(source)
# Else, the bot will send a message to alert 
    else:
        await ctx.send("ERROR: User must be in a voice channel to use the bot.")

# Function 4: Bot will leave channel.
@client.command(pass_context = True)
async def leave(ctx):
# If the BOT is in a channel, the bot will leave the channel.
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("YouTube Python Bot has left the channel.")
# Else, throw an error message.
    else:
        await ctx.send("ERROR: Youtube Python Bot is currently not in a voice channel.")

# Function 5: Bot will pause the audio.
@client.command(pass_context = True)
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
# If there is audio currently playing, pause the audio.
    if voice.is_playing():
        voice.pause()
# Else, throw an error message.
    else:
        await ctx.send("ERROR: There is no audio playing from the bot.")

# Function 6: Bot will resume the audio.
@client.command(pass_context = True)
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
# If there is audio currently paused, pause the audio.
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("ERROR: There is no audio paused from the bot.")

# Function 7: Bot will stop the audio.
@client.command(pass_context = True)
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    voice.stop()
     
# Use command to enter Discord token (python3 main.py) or just run from console.
client.run(BotToken) 
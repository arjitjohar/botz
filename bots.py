import discord
from discord.ext import commands 
import requests

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')


@client.command()
async def joke(ctx):
    r = requests.get('https://sv443.net/jokeapi/v2/joke/Any?format=txt')
    await ctx.send(r.text)


client.run('NzExOTc0NjA1MTQwNjU2MTkz.XsPsjg.FFgTFnxgKq_mLrt40BAG33EAQAE')

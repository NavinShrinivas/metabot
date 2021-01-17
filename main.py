import discord
import os
from decouple import config
from discord.ext.commands import author
# from discord import author


client = discord.Client()

@client.event
async def on_ready():
    print('I AM IN THE MATRIX [logged in]')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        print("$hello invoked")

    if message.content.startswith('$alive'):
        l1=["BlEep","BoOP","I","Am","AliVe!"]
        for i in l1:
            await message.channel.send(i)
        print("$alive invoked")
    if message.content.startswith('$pingall'):
        flag=0
        role_names = [role.name for role in author.roles]
        for i in role_names:
            if (i=="admins"):
                flag=1

        if(flag==0):
            await message.channel.send("You don't have enuf perms")
        else:
            await message.channel.send("everyone".mention)
        print("$pingall invoked")
        


client.run(config('TOKEN'))
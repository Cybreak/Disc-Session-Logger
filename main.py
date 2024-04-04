import discord
import subprocess
import json
import requests
from datetime import datetime
import os


logging = False
loggingchannel = 0
log = []
CustomDiscordPy = True

try: discord.customdiscordpycheck()
except: CustomDiscordPy = False


if CustomDiscordPy:
    token = input("Disc-Token: ")
    files = os.listdir()
    if 'Files' not in files: os.mkdir("Files")
    if 'Sessions' not in files: os.mkdir("Sessions")
    class Client(discord.Client):
        async def on_ready(self):
            subprocess.run("cls", shell=True)
            print(f"Send in the channel that you wish to start logging in '<log>' to toggle the log")
    
        async def on_message(self, message):
            global log
            global logging
            global loggingchannel
            if message.content == "<log>":
                if not logging: 
                    m = await message.reply("Logging Session Started")
                    await m.delete(delay=2)
                    await message.delete(delay=2)
                    logging = True
                    loggingchannel = message.channel.id
                    log = []
                    print("Logging Session Started")
                elif logging: 
                    m2 = await message.reply("Logging Session Ended")
                    await m2.delete(delay=2)
                    await message.delete(delay=2)
                    logging = False
                    now = datetime.now()
                    with open(f"./Sessions/{str(now.strftime("%d-%m-%Y--%H-%M-%S"))}.json", 'w') as file:
                        json.dump(log, file)
                        log = []
                    print("Logging Session Ended")
            global newestmessage
            newestmessage = message
        
            if message.channel.id == loggingchannel:
                if message.content != "":
                    log.append({
                        "author": {"username": message.author.name, "id": message.author.id},
                        "content": message.content,
                        "id": message.id})
                    if message.content != "<log>" and message.content != "Logging Session Ended":
                        print(f"Message ({message.content}) Logged")

                if len(message.attachments) > 0:
                    for a in message.attachments:
                        r = requests.get(a.url, allow_redirects=True)
                        with open(f"./Files/{a.filename}", 'wb') as file:
                            file.write(r.content)
                        print(f"File ({a.filename}) Downloaded")
        

    client = Client()
    client.run(token=token)

else:
    raise ModuleNotFoundError("Custom Discord.py not found")
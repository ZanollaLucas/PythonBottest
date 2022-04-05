from asyncore import close_all
from tkinter import W
from aiohttp import client
import os
import discord




class MyClient (discord.Client):
    
    async def on_ready(self):
        print ("ich bin online")
        channel = client.get_channel("your channel id here")
        await channel.send("$BotAtivado")
        


      

    #Wenn Nachricht gepostet wird 
    async def on_message(self, message):
        
        #if message.content.startswith("hey"):
        #   await message.channel.send("Hello")

        #print("Nachricht von " + str(message.author)+ " enthält: " + str(message.content))
        #print(message)

        #if message.channel.name == "relatório":
        #    print(str(message.content))
        #    await message.delete()

            
            
        if message.channel.name == "relatorio" and message.content == "$BotAtivado":
            await message.delete()
                    
            list = []

            async for m in message.channel.history(oldest_first=True):
                print(m)       
                if m.author.name not in list:
                    list.append(str(m.author.name))
                with open(m.author.name + '.txt','a') as l:
                    l.write(m.content + "\n")
                #if m.attachments.size == 0:
                await m.delete()
                #else:   
                #    print("tem um attachment")
                    

            close_all()
            print(list)
                    
            user = await client.fetch_user("Id from user you wanna send the files")

            for i in range(len(list)):
                await user.send("Relatório do/da " + list[i] , file=discord.File(list[i] + '.txt'))
                os.remove(list[i] + '.txt')

                    
 



client = MyClient()
client.run("YOUR BOT ID")
import random

from brain import responda, treine
from my_token import token

import discord
from discord.ext import commands
from discord import app_commands

import asyncio
from discord import FFmpegPCMAudio

bot_name = " luana"
bot_nickname = ' lu'
should_respond = False


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

        # Pega o canal de voz com o nome especificado
        channel = discord.utils.get(client.get_all_channels(), name='Lazy')
        source = FFmpegPCMAudio('./files/LÁ ELE-TIERRY E MANOEL GOMES (320 kbps).mp3')
        # Conecta ao canal de voz
        voice_client = await channel.connect()
        voice_client.play(source)

    async def reset_should_respond(self):
        global should_respond
        await asyncio.sleep(10 * 60)  # espera 10 minutos
        print('TIME OUT: call again bot with "luana" or "lu"')
        should_respond = False

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'OOIIIIIII {member.mention} tu ta no {guild.name}! \n servidor mais estranho de TODOS \n ' \
                      f'Qualquer coisa chama o <@301848296568127488> \n E se quiser falar cmg, olha o canal ' \
                      f'<#1079127684002627635> VAI EXPLICAR TUDO'
            await guild.system_channel.send(to_send)

    async def on_message(self, message):
        global should_respond
        # print(message)

        # don't respond to ourselves
        if message.author == self.user:
            return

        if bot_name in message.content.lower() or bot_nickname in message.content.lower():
            should_respond = True
            await message.reply('Oii amor!', mention_author=True)

            await self.reset_should_respond()

        if should_respond:
            if message.content == 'desligar':
                await message.channel.send('desligando...')
                quit()

            elif message.content == 'ping':
                await message.channel.send('pong')

            elif message.content.lower() == 'qual teu nome?' or message.content.lower() == 'qual seu nome?':
                await message.channel.send('LUANA COMEDORA DE XERECA')

            elif message.content.lower() == 'stop msgs':
                await message.channel.send('saindo ent, mas qlqr coisa é só me chamar baby')
                should_respond = False

            elif 'meu' in message.content.lower() and 'nome' in message.content.lower() and '?' in message.content.lower():
                await message.reply(f'teu nome é {message.author.name}')

            elif 'treine' in message.content.lower():
                treine()

            elif message.content != '':
                msg = message.content
                msglower = message.content.lower()
                filesbymsgcontent = ['puta', 'careca', 'pipokinha', 'seqsu', 'la ele', 'nossa namorada']
                filespath = './files/'
                filepicked = ''
                response = responda(msg)
                responselower = response

                for name in filesbymsgcontent:
                    if name in str(responselower) or name in str(msglower):
                        if name == 'puta':
                            filepicked = filespath + 'pipokinha.jpeg'
                        elif name == 'careca':
                            filepicked = filespath + 'carecaaa.jpeg'
                        elif name == 'pipokinha':
                            filepicked = filespath + 'bota na pipokinha super xandão meme (320 kbps).mp3'
                        elif name == 'seqsu':
                            filepicked = filespath + 'sexo e bom.mp4'
                        elif name == 'la ele':
                            pick = random.getrandbits(2)
                            if pick == 0:
                                filepicked = filespath + 'LÁ ELE-TIERRY E MANOEL GOMES (320 kbps).mp3'
                            else:
                                filepicked = filespath + 'la ele.jpg'
                        elif name == 'nossa namorada':
                            filepicked = filespath + 'nossa namorada.jpg'
                        else:
                            filepicked = ''

                if filepicked != '':
                    await message.channel.send(response, file=discord.File(filepicked))
                else:
                    await message.channel.send(response)


intents = discord.Intents.all()
intents.message_content = True
client = MyClient(intents=intents)
client.run(token)

# ~~ Imports ~~ #   

import discord
import asyncio
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from colorama import Fore, Style
import os
import random
from datetime import datetime

# ~~ Colors ~~ #

c = "\033[38;2;25;25;112m"
d = "\033[1;90m"
red = "\033[1;31m"
blue = "\033[1;34m"
w = "\033[1;37m"
r = Style.RESET_ALL
g = "\033[90m"
green = "\033[0;37;40m"


# ~~ Source (do not mess with unless you know what you are doing) ~~ #

emj = "stuff/emojis.txt"

def tkns():
    if os.path.exists('input/tokens.txt'):
        with open('input/tokens.txt', 'r') as file:
            tokens = [line.strip() for line in file.readlines()]
            return tokens, len(tokens)
    return [], 0

tokens, tok = tkns()

def cc():
        os.system('cls')

def emo():
    if os.path.exists(emj):
        with open(emj, 'r', encoding='utf-8') as file:
            emojis = [line.strip() for line in file.readlines()]
            return emojis
    return []

emojis = emo()

async def spam(token, uid, message, count, rs, rm, em):
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        await asyncio.sleep(1)
        print(f"{datetime.now().strftime(f'{g}[{r}{g}%H{r}{g}:{r}{g}%M{r}{g}:{r}{g}%S{r}{g}]{r}')}    {g}[+]{Style.RESET_ALL}      {g}->{r}    {g}Logged in as{r} {g}{client.user.name}{r}")
        await asyncio.sleep(1)
        tar = await client.fetch_user(int(uid))

        for _ in range(count):
            try:
                msg = message
                if rs:
                    msg += " -> " + ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=25))

                if rm:
                    msg += " -> " + ' '.join(random.choices(emojis, k=em))

                await tar.send(msg)
                await asyncio.sleep(0.5)
                print(f"{datetime.now().strftime(f'{g}[{r}{g}%H{r}{g}:{r}{g}%M{r}{g}:{r}{g}%S{r}{g}]{r}')}    {g}[+]{Style.RESET_ALL}      {g}->{r}    {green}[SUCCESS]{r} {g} Sent DM{r} {red}~{r} {message} ({g}{client.user.name}{r})")

            except discord.Forbidden:
                print(f"{datetime.now().strftime(f'{g}[{r}{g}%H{r}{g}:{r}{g}%M{r}{g}:{r}{g}%S{r}{g}]{r}')}  {g}[-]{Style.RESET_ALL}      {g}->{r}    {red}[FAILURE] {tar.name}  DMs are closed{r} ({g}{client.user.name}{r})")
                continue

    await client.start(token)





def logo():
    nn = Center.XCenter(f"""
{g}
                                                        
  _____     _   _    _____ _           _         
|  |  |___|_|_| |  |   __| |___ ___ _| |___ ___ 
|  |  | . | | . |  |   __| | . | . | . | -_|  _|
 \___/|___|_|___|  |__|  |_|___|___|___|___|_|   .     

 {g}
    """)
    print(nn)

async def main():
    os.system('title Void Flooder')
    cc()
    logo()
    print(f'                                               {g}Loaded:{r} {g}‹{r}{tok}{r}{g}›{r} {g}tokens') 
    print(f"""
                                            {g}[{w}1{g}]{r} {g} Dm Spam     {g}[{w}2{g}]{r} {g} Exit
    """) 
    option = input(f'            {g}[~] $Choice ~{r} ')

    if option == "1":
        print()
        tokens = open('input/tokens.txt', 'r').read().splitlines()
        uid = input(Colorate.Horizontal(Colors.blue_to_white, "VoidCord@cmd → User Id ~ "))
        if uid == '':
            await main()
        message = input(Colorate.Horizontal(Colors.blue_to_white, "VoidCord@cmd~  → Message ~ "))
        if message == '':
            await main()
        count = int(input(Colorate.Horizontal(Colors.blue_to_white, "VoidCord@cmd$~ → Amount ~ ")))
        if count == '':
            await main()        
        rs = input(Colorate.Horizontal(Colors.blue_to_white, "VoidCord@cmd$~ → Random String (y/n) ~ ")).strip().lower() == 'y'
        if rs == '':
            await main()        
        rm = input(Colorate.Horizontal(Colors.blue_to_white, "VoidCord@cmd$~ → Random Emojis (y/n) ~ ")).strip().lower() == 'y'
        if rm == '':
            await main()
        em = 5
        if rm:
            em = int(input(Colorate.Horizontal(Colors.blue_to_white, "VoidCord@cmd$~ → Emoji Amount ~ ")))
        if em == '':
            await main()

        tasks = [spam(token, uid, message, count, rs, rm, em) for token in tokens]
        await asyncio.gather(*tasks)

    elif option == "2":
        print('exiting..')
        exit()

if __name__ == "__main__":
    asyncio.run(main())
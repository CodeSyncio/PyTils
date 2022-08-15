import __main__
from colorama import Fore
from subprocess import DEVNULL,STDOUT
import sys
import discord
from discord.ext import commands
import requests
import asyncio
def cls():
    __main__.util.cls()
def mainscrn():
    __main__.init.MainScreen()


def SelfBot(tokywoky,q):
        bot = commands.Bot(command_prefix='§', self_bot=True)
        
        #<---command defining---> 
        @bot.command()
        async def shrug(ctx):
            await ctx.message.delete()
            await ctx.send("¯\_(ツ)_/¯")
            
        @bot.command()
        async def disapprove(ctx):
            await ctx.message.delete()
            await ctx.send("ᇂ_ᇂ")
            
        @bot.command()
        async def fu(ctx):
            await ctx.message.delete()
            await ctx.send("( ͡° ͜つ ͡°)╭∩╮")
        
        @bot.command()
        async def confused(ctx):
            await ctx.message.delete()
            await ctx.send("┐(ﾟ ～ﾟ )┌")
            
        @bot.command()
        async def hi(ctx):
            await ctx.message.delete()
            await ctx.send("( ^_^)／")
            
        @bot.command()
        async def ipup(ctx,ip):    
            await ctx.message.delete()
            jsonrequest = requests.get(f'https://ipinfo.io/{ip}/json')
            if "Wrong ip" in jsonrequest.text:
                await ctx.send("Invalid IP address")
                return
            else:
                pass
                json = jsonrequest.json()
                try:
                    ipinfout = f'***Ip info for***`{ip}` \nCity = ***{json["city"]}***\nRegion = ***{json["region"]}***\ncountry = ***{json["country"]}***\nlocation = ***{json["loc"]}***\nZip = ***{json["loc"]}***\nTimeZone = ***{json["timezone"]}***\nOrganisation = ***{json["org"]}***'
                    await ctx.send(ipinfout)
                except:
                    pass
        
        @bot.command()
        async def spam(ctx,msg,amount):
            await ctx.message.delete()
            coroutforspamming = [ctx.send(msg)for i in range(int(amount))]
            await asyncio.gather(*coroutforspamming)
        
        @bot.command()
        async def pfp(ctx, user: discord.User=None):
            ctx.message.delete()
            if user is None:
                pass
            else:
                try:
                    message= f"[***{user.name}***'s Avatar]\n*{user.avatar_url}*"
                    await ctx.send(message)
                except:    
                    pass

        @bot.command()
        async def purge(ctx,amount:int):
            try:
                await asyncio.sleep(1)
                succes = 0
                await ctx.send(f'***starting deletion of `{amount}` message(s)***')
                await asyncio.sleep(5)
                async for message in ctx.message.channel.history(limit=amount):
                    if message.author == bot.user:
                        succes += 1
                        await message.delete()
                    else:
                        pass
                asd = await ctx.send(f'***Deleted `{succes}` message(s)***\n*deleting this message in 10 seconds...*')
                await asyncio.sleep(10)
                await asd.delete()
            except:pass
        
        @bot.command()
        async def loading(ctx,object:str,sec:int):
            await ctx.message.delete()
            try:
                msg = await ctx.send('...')
                for i in range(sec):
                    await asyncio.sleep(1)
                    am = round((i+1)/sec*100/5)
                    am2 = round(20 -(i+1)/sec*100/5)
                    await msg.edit(content='***'+object+'*** \n'+'['+am*'█'+am2*'▒'+']  ('+str(round((i+1)/sec*100))+'%)' )
                await msg.edit(content='***'+object+'*** \n'+'[***DONE***]  ('+str(round((i+1)/sec*100))+'%)' )
            except:
                pass

        #<---starting the bot--->
        try:
            sys.stdout = DEVNULL
            sys.stderr = DEVNULL
            bot.run(tokywoky, bot=False)
        except Exception as e:
            q.put('stopped')
    
def botinfo():
    cls()
    print(Fore.CYAN+"<----------Commands---------->")
    print(Fore.BLUE+"Prefix = §")
    print(Fore.LIGHTBLUE_EX+'"shrug" - returns the ¯\_(ツ)_/¯ emoji')
    print(Fore.LIGHTBLUE_EX+'"disapprove" - returns the ᇂ_ᇂ emoji')
    print(Fore.LIGHTBLUE_EX+'"fu" - returns the ( ͡° ͜つ ͡°)╭∩╮ emoji')
    print(Fore.LIGHTBLUE_EX+'"confused" - returns the ┐(ﾟ ～ﾟ )┌ emoji')
    print(Fore.LIGHTBLUE_EX+'"hi" - returns the ( ^_^)／ emoji')
    print(Fore.LIGHTBLUE_EX+'"spam" - usage: spam <message> <times to spam> , spams a given message (ex: spam "hello" 20)')
    print(Fore.LIGHTBLUE_EX+'"ipup" - usage : ipup <ip>, returns info in chat about an ip (ex: ipup 1.1.1.1)')
    print(Fore.LIGHTBLUE_EX+'"pfp" - usage : pfp <@user>, returns profile pic of a user (ex: pfp @CodeSyncio#7302)')
    print(Fore.LIGHTBLUE_EX+'"purge" - usage : purge <purge amount>, deletes a given amount of msges (ex: purge 100)')
    print(Fore.LIGHTBLUE_EX+'"loading" - usage : loading <what you are doing> <time in seconds>, shows a loading bar loading for the specified amount of time (ex: loading "downloading games" 120 )')
    print(Fore.MAGENTA+"press enter to return to main menu")
    ghinput = input()
    mainscrn()
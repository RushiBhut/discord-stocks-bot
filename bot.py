import discord
from discord.ext import commands
import scraper

client = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def cmds(ctx):
    await ctx.send("Work in progress")

@client.command()
async def price(ctx, arg):
    try:
        price = scraper.find_price(arg)
        await ctx.send(f"{arg.upper()} is worth ${price}")
    
    except:
        pass

@client.command()
async def view(ctx, arg):
    if(arg == "gainers"):
        gainers = scraper.find_gainers()

        output = "**Top 10 Gaining Stocks of the Day**\n\n" 
        i = 1

        for gainer in gainers:
            name = gainer[0]
            symbol = gainer[1]
            percent_change = gainer[2]
            output += f"{i}. {name} ({symbol}) -- {percent_change}\n"
            i += 1

        await ctx.send(output)

    elif(arg == "losers"):
        losers = scraper.find_losers()

        output = "**Top 10 Losing Stocks of the Day**\n\n" 
        i = 1
        
        for loser in losers:
            name = loser[0]
            symbol = loser[1]
            percent_change = loser[2]
            output += f"{i}. {name} ({symbol}) -- {percent_change}\n"
            i += 1

        await ctx.send(output)

    else:
        pass

client.run("MTAwMjY4OTcyMzI0NjA3MTgyOA.GUMLld.oOSGkzV3p3El0UiPJKNnG0NUBfMOUdPxQHLPH8")

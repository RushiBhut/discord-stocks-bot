import discord
from discord.ext import commands
import scraper

client = commands.Bot(command_prefix="$")

# Sends a message to the terminal when the bot is running
@client.event
async def on_ready():
    print("Bot is ready")

# This will display the commands that are available to use by the members of the discord server
@client.command()
async def cmds(ctx):
    await ctx.send("Work in progress")

# Finds the price of the ticker symbol that was entered as an argument
# If the ticker symbol does not exist, nothing happens
@client.command()
async def price(ctx, arg):
    try:
        price = scraper.find_price(arg)
        await ctx.send(f"{arg.upper()} is worth ${price}")
    
    except:
        pass

# Lists either the gaining or losing stocks depending on the argument that was passed in
@client.command()
async def view(ctx, arg):
    if(arg == "gainers"):
        gainers = scraper.find_gainers()

        output = "**Top 10 Gaining Stocks of the Day**\n\n" 
        i = 1

        # Formats the name, symbol, and percent change of the stock for each stock in the list
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
        
        # Formats the name, symbol, and percent change of the stock for each stock in the list
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

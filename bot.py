from discord.ext import commands
from config import *
import os

client = commands.Bot(command_prefix=prefix)
client.remove_command('help')

@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    print(f"loaded {extension}")
    await ctx.send(f"loaded {extension}")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    print(f"unloaded {extension}")
    await ctx.send(f"unloaded {extension}")

@client.command()
async def reload(ctx, extension):
    client.reload_extension(f"cogs.{extension}")
    print(f"reloaded {extension}")
    await ctx.send(f"reloaded {extension}")




for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(token)
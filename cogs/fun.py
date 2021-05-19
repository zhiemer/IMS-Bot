from discord.ext import commands


class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def suicide(self, ctx):
        pass

    @commands.command()
    async def suislide(self, ctx):
        pass

def setup(client):
    client.add_cog(fun(client))
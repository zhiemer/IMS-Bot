from discord.ext import commands


class moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def kick(self, ctx):
        pass

    @commands.command()
    async def bann(self, ctx):
        pass

    @commands.command()
    async def mute(self, ctx, time=10):
        pass

    @commands.command()
    async def warn(self, ctx):
        pass

    @commands.command()
    async def clear(self, ctx, amount=10):
        pass

def setup(client):
    client.add_cog(moderation(client))
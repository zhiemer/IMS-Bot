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

    @client.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(ctx, amount=1000):
        await ctx.channel.purge(limit=amount)

def setup(client):
    client.add_cog(moderation(client))

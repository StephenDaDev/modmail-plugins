import discord
from discord.ext import commands
from core import checks


class PremPrefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @checks.thread_only()
    async def raw(self, ctx):
        await ctx.send('<<prem>>')
        

def setup(bot):
    bot.add_cog(PremPrefix(bot))

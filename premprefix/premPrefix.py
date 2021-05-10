  
import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

class premPrefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.has_permissions(PermissionLevel.MODERATOR)
    @checks.thread_only()
    async def nb(self, ctx):
        """Send nitro booster prefix."""
        link = await self.bot.api.get_log_link(ctx.channel.id)
        await ctx.send(f"`«nb»`")

def setup(bot):
    bot.add_cog(premPrefix(bot))

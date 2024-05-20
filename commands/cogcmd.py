from discord.ext import commands
import discord
from discord import option


class COG(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command(
        name="testcog",
        description="testcog command")
    async def botstatus(self, ctx):
        await ctx.respond("COG Command works!", ephemeral=True)



def setup(bot):
  bot.add_cog(COG(bot))

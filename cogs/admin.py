from __future__ import annotations

from typing import TYPE_CHECKING, Literal

import discord
from discord import Interaction, app_commands, ui
from discord.ext import commands

if TYPE_CHECKING:
    from bot import Bot


class Admin(commands.Cog):
    """Error handler"""

    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot

    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx: commands.Context[Bot], sync_type: Literal['guild', 'global']) -> None:
        """Sync the application commands"""

        async with ctx.typing():
            if sync_type == 'guild':
                self.bot.tree.copy_global_to(guild=ctx.guild)  # type: ignore
                await self.bot.tree.sync(guild=ctx.guild)
                await ctx.reply('Synced guild !')
                return

            await self.bot.tree.sync()
            await ctx.reply('Synced global !')

    @commands.command()
    @commands.is_owner()
    async def unsync(self, ctx: commands.Context[Bot], unsync_type: Literal['guild', 'global']) -> None:
        """Unsync the application commands"""

        async with ctx.typing():
            if unsync_type == 'guild':
                self.bot.tree.clear_commands(guild=ctx.guild)
                await self.bot.tree.sync(guild=ctx.guild)
                await ctx.reply('Un-Synced guild !')
                return

            self.bot.tree.clear_commands()  # type: ignore
            await self.bot.tree.sync()
            await ctx.reply('Un-Synced global !')

    @app_commands.command(description='Shows basic information about the bot.')
    async def about(self, interaction: Interaction) -> None:
        """Shows basic information about the bot."""

        owner_url = 'https://discord.com/users/700198692694786068'
        github_project = 'https://github.com/Sandau1204/Mosa-bot'
        support_url = 'https://discord.gg/kzs8M6vRQ9'

        embed = discord.Embed(color=0xFFFFFF)
        embed.set_author(name='VALORANT BOT PROJECT', url=github_project)
        embed.set_thumbnail(url='./avatar.heic')
        embed.add_field(name='DEV:', value=f'[mrs.codon]({owner_url})', inline=False)
        embed.add_field(
            name='ᴄᴏɴᴛʀɪʙᴜᴛᴏʀꜱ:',
            value='[kiznick](https://github.com/kiznick)\n'
            '[KANATAISGOD](https://github.com/KANATAISGOD)\n'
            "[TMADZ2007](https://github.com/KANATAISGOD')\n"
            '[sevzin](https://github.com/sevzin)\n'
            '[MIIGØ](https://github.com/miigo-dev)\n'
            '[Connor](https://github.com/ConnorDoesDev)\n'
            '[KohanaSann](https://github.com/KohanaSann)\n'
            '[RyugaXhypeR](https://github.com/RyugaXhypeR)\n'
            '[Austin Hornhead](https://github.com/marchingon12)\n',
            inline=False,
        )
        view = ui.View()
        view.add_item(ui.Button(label='GITHUB', url=github_project, row=0))
        view.add_item(ui.Button(label='KO-FI', url='https://ko-fi.com/staciax', row=0))
        view.add_item(ui.Button(label='SUPPORT SERVER', url=support_url, row=0))

        await interaction.response.send_message(embed=embed, view=view)


async def setup(bot: Bot) -> None:
    await bot.add_cog(Admin(bot))

from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def あけおめ(ctx):
    await ctx.send('ことよろ')

    
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def 今月いくら課金したん？(ctx):
    await ctx.send('ソレハ…イエナイ……')
    
   
bot.run(token)

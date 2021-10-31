import discord
import random
import asyncio
import os
from discord.ext import commands, tasks
from itertools import cycle
from PIL import Image,ImageDraw,ImageFont
from io import BytesIO

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

@client.event
async def on_ready():
	print('Bot is online')
	
@client.command()
async def say(ctx,*,message):
	await ctx.send(f"{message}")

@client.command()
async def latency(ctx): 
	await ctx.send(f'<a:pverify:883309501040697355> Rate - {round(client.latency * 1000)}ms')

@client.command()
async def dm(ctx, user: discord.User, *, message=None):
	message = message
	await user.send(message)

@client.command()
async def help(ctx):
	embed = discord.Embed(
		title = 'Help Commands',
		description = "``latency`` - Gives you the bot ping rate\n"
					  "``dm [user] [message]`` - Dm the user with your message\n"
					  "``say`` - The bot will repeat whatever you say\n"
					  "``8ball [question]`` - You know what it does\n"
					  "``banner [user]`` - Get the banner of a user\n"
					  "``avatar [user]`` - Get the avatar of a user\n"
					  "``topic`` - Send fun related questions by the bot\n",

		colour = discord.Colour.orange()

	)

	await ctx.send(embed=embed)

@client.command(name="banner", aliases=["bn"])
async def banner(ctx, *,  user:discord.User):
	if user == None:
		user = ctx.message.author
	user = user or ctx.message.author
	embed = discord.Embed(description=f"**{user.name}#{user.discriminator}**",color=0xFF0000)
	embed.set_image(url=user.banner.url if user.banner else ":(")
	await ctx.send(embed=embed)

@client.command(name="avatar", aliases=["av"])
async def avatar(ctx, *, member: discord.Member=None):
	if not member:
		member = ctx.message.author
	userAvatar = member.avatar.url

	embed = discord.Embed(description=f"**{member.name}#{member.discriminator}**",color=0xFF0000)
	embed.set_image(url=member.avatar.url)
	await ctx.send(embed=embed)

@client.command()
async def topic(ctx):
	toplist = [
		'Do you think the internet was a mistake?',
		'Worst Song?',
		'Are you the impostor from Among Us?',
		'If you would like to revive a dead meme, which one would it be?',
		'Underrated Games?',
		'Xbox or Playstation?',
		'Any Childhood Shows?',
		'The most surprising moment of your life that you will never forget',
		'What is your favourite Adult Animated Show?',
		'Things you believed as a kid turns out be a joke?',
		'If you had the ability to go back in time and change one thing, what would it be?'
	]

	embed = discord.Embed(
		colour=0xFF7F7F,
		title="<a:rFLAME:892115818324824104> Topic",
		description= f"{random.choice(toplist)}"
	)
	embed.set_footer(text = f"Requested by {ctx.author.name}{ctx.author.discriminator}")

	await ctx.send(embed=embed)

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
	response = ['Yes <:YES:883572456055537764>' , 'Maybe? <:NEUTRAL:883574359996907530>' , 'Nope <:NO:883573135234977882>' , 'Impossible <:NO:883573135234977882>' , 'Yes, it will <:YES:883572456055537764>']
	await ctx.send(f'{random.choice(response)}')

client.run('TOKEN')

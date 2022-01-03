from datetime import datetime
import pytz
from discord import Intents
from discord import Embed
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase

IST = pytz.timezone('Asia/Kolkata')

PREFIX = "/"
OWNER_IDS = [757535844826611764]


class Bot(BotBase):
	def __init__(self):
		self.Prefix = PREFIX
		self.ready = False
		self.guild = None
		self.scheduler = AsyncIOScheduler()

		super().__init__(
			command_prefix=PREFIX,
			owner_ids=OWNER_IDS,
			intents=Intents.all(),
			)

	def run(self, version):
		self.VERSION = version

		with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
			self.TOKEN = tf.read()

		print("running bot>>>")
		super().run(self.TOKEN, reconnect=True)
		
	async def on_connect(self):
		print("Bot Connected")
		
	async def on_disconnect(self):
		print("bot disconnected")
		
	async def on_ready(self):
		if not self.ready:
			self.ready = True
			self.guild = self.get_guild(737574941578494023)
			print("bot ready")

			channel = self.get_channel(913130585038422036)
			await channel.send("Bot is Online")

			embed =Embed(title="Welcome User, I am Orange Ocelot", description="Your Friendly Neighbourhood Discord Bot", 
				colour=0xFFA500, timestamp=datetime.now(IST))
			fields = [("Name", "Aadi", True),
			("Perms", "He is the owner.", True),
			("Status", "The bot is currently in development ", False)]
			for name, value, inline in fields:
				embed.add_field(name=name, value=value, inline=inline)
			embed.set_author(name="Darth Revan",)
			embed.set_footer(text="Coded By Obi-wan Kenobi using python")
			await channel.send(embed=embed)

		else:
			print("bot reconnected")

	async def on_message(self, message):
		pass


bot = Bot()
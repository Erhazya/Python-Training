import discord
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name}')

@tasks.loop(hours=24)  # Répète toutes les 24 heures
async def presence_check():
    guild_id = 1234567890  # Remplace par l'ID de ton serveur
    role_name = "Nom du rôle"  # Remplace par le nom du rôle souhaité

    guild = bot.get_guild(guild_id)
    role = discord.utils.get(guild.roles, name=role_name)

    if guild is not None and role is not None:
        for member in guild.members:
            if role in member.roles:
                # Vérifie si le membre a déjà voté
                if not member.voice:
                    # Effectue une action à 3 heures de l'après-midi
                    # Ici tu peux ajouter le code pour effectuer la présence à 3 heures

                    # Envoie un rappel à 20 heures
                    channel = await member.create_dm()
                    await channel.send("N'oubliez pas de voter !")
    else:
        print("Impossible de trouver le serveur ou le rôle")

@presence_check.before_loop
async def before_presence_check():
    # Attends jusqu'à 3 heures de l'après-midi pour commencer
    await bot.wait_until_ready()
    print("Attente jusqu'à 15h pour effectuer la présence...")

    current_time = datetime.datetime.now().time()
    target_time = datetime.time(hour=15, minute=0)  # Modifier si nécessaire
    time_diff = (target_time - current_time).total_seconds()

    if time_diff > 0:
        await asyncio.sleep(time_diff)

    print("Effectue la présence à 15h")

presence_check.start()

bot.run('TOKEN')  # Remplace 'TOKEN' par le jeton de ton bot Discord

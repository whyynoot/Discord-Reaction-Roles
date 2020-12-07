import discord
from discord.ext import commands


intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("Cooking Apple Pie..."), status=discord.Status.online, afk=False)

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 779842208568049675:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        if payload.emoji.name == "🤖":
            role = discord.utils.get(guild.roles, id=779821957587140649)
        elif payload.emoji.name == "🚪":
            role = discord.utils.get(guild.roles, id=777637793211220020)
        elif payload.emoji.name == "bag":
            role = discord.utils.get(guild.roles, id=777637663092113430)
        elif payload.emoji.name == 'Footlocker':
            role = discord.utils.get(guild.roles, id=779821650803687444)
        elif payload.emoji.name == '🎨':
            role = discord.utils.get(guild.roles, id=777637720944017448)
        elif payload.emoji.name == 'cntower':
            role = discord.utils.get(guild.roles, id=779823603704659968)
        elif payload.emoji.name == '🏰':
            role = discord.utils.get(guild.roles, id=779824364287295488)
        elif payload.emoji.name == '🌆':
            role = discord.utils.get(guild.roles, id=779824417281802280)
        elif payload.emoji.name == '🏙️':
            role = discord.utils.get(guild.roles, id=779824520420524072)
        elif payload.emoji.name == 'ottawa':
            role = discord.utils.get(guild.roles, id=779824614406488074)
        elif payload.emoji.name == 'manitoba':
            role = discord.utils.get(guild.roles, id=779824684836585492)
        elif payload.emoji.name == 'saskatoon':
            role = discord.utils.get(guild.roles, id=779824917813264395)
        elif payload.emoji.name == 'StJohns':
            role = discord.utils.get(guild.roles, id=779824968598552597)
        elif payload.emoji.name == '🌐':
            role = discord.utils.get(guild.roles, id=777637459608993812)
        elif payload.emoji.name == '🏬':
            role = discord.utils.get(guild.roles, id=777637532405334027)
        elif payload.emoji.name == 'Bulk':
            role = discord.utils.get(guild.roles, id=777637253382930493)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                await member.send(f"{role} role was added to your account!")
            else:
                await member.send(f"There was an error due adding {role} role to your account!")


@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 779842208568049675:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        if payload.emoji.name == "🤖":
            role = discord.utils.get(guild.roles, id=779821957587140649)
        elif payload.emoji.name == "🚪":
            role = discord.utils.get(guild.roles, id=777637793211220020)
        elif payload.emoji.name == "bag":
            role = discord.utils.get(guild.roles, id=777637663092113430)
        elif payload.emoji.name == 'Footlocker':
            role = discord.utils.get(guild.roles, id=779821650803687444)
        elif payload.emoji.name == '🎨':
            role = discord.utils.get(guild.roles, id=777637720944017448)
        elif payload.emoji.name == 'cntower':
            role = discord.utils.get(guild.roles, id=779823603704659968)
        elif payload.emoji.name == '🏰':
            role = discord.utils.get(guild.roles, id=779824364287295488)
        elif payload.emoji.name == '🌆':
            role = discord.utils.get(guild.roles, id=779824417281802280)
        elif payload.emoji.name == '🏙️':
            role = discord.utils.get(guild.roles, id=779824520420524072)
        elif payload.emoji.name == 'ottawa':
            role = discord.utils.get(guild.roles, id=779824614406488074)
        elif payload.emoji.name == 'manitoba':
            role = discord.utils.get(guild.roles, id=779824684836585492)
        elif payload.emoji.name == 'saskatoon':
            role = discord.utils.get(guild.roles, id=779824917813264395)
        elif payload.emoji.name == 'StJohns':
            role = discord.utils.get(guild.roles, id=779824968598552597)
        elif payload.emoji.name == '🌐':
            role = discord.utils.get(guild.roles, id=777637459608993812)
        elif payload.emoji.name == '🏬':
            role = discord.utils.get(guild.roles, id=777637532405334027)
        elif payload.emoji.name == 'Bulk':
            role = discord.utils.get(guild.roles, id=777637253382930493)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                await member.send(f"{role} role was removed from your account!")
            else:
                await member.send(f"There was an error due removing {role} role from your account!")


if __name__ == '__main__':
    while True:
        try:
            client.run("")  # main
        except:
            client.run("")  # main
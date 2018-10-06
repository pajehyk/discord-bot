import discord;
import asyncio;
import requests;

DISCORD_BOT_TOKEN = "";

client = discord.Client();

@client.event
async def on_ready():
    print("Logged in as");
    print(client.user.name);
    print(client.user.id);
    print("-------");

    myServer = client.get_server('359631684330848256');
    global homoRole;
    if myServer != None:
        if '373405537095647235' in [y.id for y in myServer.roles]:
            for y in myServer.roles:
                if y.id == '373405537095647235':
                    homoRole = y;
    

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
        
    if message.content.startswith('!hi'):
        print("[command]: hi ");
        await client.send_message(message.channel, 'asdasd');
    if message.content.startswith('!role'):
        print("[command]: role ");
        await client.send_message(message.channel, message.author.roles[1].id);
        print(message.author.roles[1].id);

@client.event
async def on_member_join(member):
    print('member joined: ', member.nick, member.roles[0]);
    await client.add_roles(member, homoRole);
    print(member.roles);
    

client.run(DISCORD_BOT_TOKEN);

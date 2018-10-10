import discord;
import asyncio;
import requests;

DISCORD_BOT_TOKEN = "";

client = discord.Client();

global myServer;
myServer = myServer = client.get_server('359631684330848256');
idChopChop = '323366007030677504';
idChopper = '352411742766366721';
idRoleHomo = '497930663802961921';
idRoleAdmin = '359660189344858122';




@client.event
async def on_ready():
    print("Logged in as");
    print(client.user.name);
    print(client.user.id);
    print("-------");

    global myServer;
    myServer = client.get_server('359631684330848256');
    global roleAdmin;
    global roleHomo;
    
    if myServer != None:
        if idRoleHomo in [y.id for y in myServer.roles]:
            for y in myServer.roles:
                if y.id == idRoleHomo:
                    roleHomo = y;
        if idRoleAdmin in [y.id for y in myServer.roles]:
            for y in myServer.roles:
                if y.id == idRoleAdmin:
                    roleAdmin = y;
    

@client.event
async def on_message(message):
    
    if message.content.startswith('!test'):
        print('[command]: test');
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    if message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
        
    if message.content.startswith('!hi'):
        print('[command]: hi ');
        await client.send_message(message.channel, 'маму ебал');

    #admin
    if roleAdmin in message.author.roles:
        if message.content.startswith('!deletechopper'):
            tmp = await client.send_message(message.channel, 'deleting...');
            for y in myServer.members:
                if y.id == idChopper:
                    userChopper = y;
                if y.id == idChopChop:
                    userChopChop = y;
            
            async for log in client.logs_from(message.channel, limit=100):
                if (log.author.id == idChopper or log.author.id == idChopChop):
                    await client.delete_message(log);

            await client.edit_message(tmp, 'deleted kara armenin.');

        
        

@client.event
async def on_member_join(member):
    print('member joined: ', member.name);
    await client.add_roles(member, roleHomo);
    

client.run(DISCORD_BOT_TOKEN);

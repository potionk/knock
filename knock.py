import requests
import discord

api_url = 'url'
discord_channel_id = 1234
bot_token = 'token'


def lambda_handler(event, context):
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
        response = requests.get(api_url)
        if response.status_code != 200:
            await send_discord_message(f'API response code: {response.status_code}')
        await client.close()

    async def send_discord_message(message):
        channel = client.get_channel(discord_channel_id)
        if channel:
            await channel.send(message)
        else:
            print(f'Channel {discord_channel_id} not found')

    client.run(bot_token)

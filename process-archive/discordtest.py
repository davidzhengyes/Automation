from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/1197037155554443314/uxp9jMz5aPyhQaA0lcdq1MSXCEC-5JupagoCU6H5ufAwXNES4no0K2w_tryoYiKUBKqC', content='Webhook Message')
response = webhook.execute()



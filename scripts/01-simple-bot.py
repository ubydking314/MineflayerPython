from javascript import require, On, Once, AsyncTask, once, off

# Import the javascript libraries
mineflayer = require("mineflayer")

# Create bot with basic parameters
bot = mineflayer.createBot(
    {"username": "simple-bot", "host": "localhost", "port": 53479, "version": "1.21.4", "hideErrors": False}
)

# Login event required for bot
@On(bot, "login")
def login(this):
    pass

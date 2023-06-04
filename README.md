# ghostpepper_bot
This is the code for the ghost pepper bot. Version control is done here on GitHub, and the bot is run on Replit.
There are a variety of commands that the bot can do such as roasting, giving users pick uplines, 8 ball responses, coinflips, and some fun easter eggs that are found when certain key words are sent. It can be found in my personal discord server, Hot Chili:

https://discord.gg/VkF3z8WmEN

## Future Updates
- [ ] add command for conversation starters
- [ ] add a command for a "Would You Rather", perhaps using buttons

Requirements
* discord.py 2.2.3
* discord-py-slash-command 4.2.1
* Flask 2.3.2
* datetime v3.11.3
* random v3.11.3

### Additional Information
I use the free version of replit and as a result programs close after an hour on inactivity. To keep this bot online all the time, I used uptimerobot which sends requests to the bot in 5 minute intervals to keep the bot online. If you use an IDE without this limitation, delete "keep_alive.py" and the function "keep_alive()" in "main.py" can be deleted.

### Author
This bot is proudly created by Ishan Vemireddy aka RedTachyon19

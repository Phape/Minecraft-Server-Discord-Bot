#!/bin/bash
# make executable with: chmod +x run_mc_discord_bot.sh

echo 'starting Minecraft-Server-Discord-Bot'
git pull
source ./venv/bin/activate
pip3 install -r requirements.txt
# screen -S minecraft -X stuff 'tellraw @a {"text":"In run_mc_discord_bot.sh", "color":"dark_purple"} ^M'
python3 main.py
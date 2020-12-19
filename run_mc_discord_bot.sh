#!/bin/bash
# make executable with: chmod +x run_mc_discord_bot.sh

echo 'starting Minecraft-Server-Discord-Bot'
git pull
source venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
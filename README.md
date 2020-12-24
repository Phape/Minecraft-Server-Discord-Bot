# Minecraft-Server-Discord-Bot
A small bot for discord that mirrors the Minecraft chat to Discord ad vice versa

# How it works
- To get the chats from MC, the latest.log is tailed with [Pygtail](https://github.com/bgreenlee/pygtail)
  - Pygtail supports log rotation but doesn't look for a logfile that has the exact same name as the old log (MC creates a new `latest.log` when the server restarts or the RL-day ends
  As a workaround, I added the following lines to the `core.py`of Pygtail (to the method called `_check_rotated_filename_candidates`:
  ```Python
  candidate = "%s" % self.filename
        if exists(candidate):
            return candidate
  ```
- A whitelist determines which logs are mirrored to the Discord chat (key-word: regex)
- The rest of the script is just a simple Discord bot made using [discord.py](https://github.com/Rapptz/discord.py)
- Messages from Discord to MC are sent via command that is entered to the MC console
  - Minecraft runs in a [screen](https://linuxize.com/post/how-to-use-linux-screen/) on a linux server - [screen manual](https://www.gnu.org/software/screen/manual/screen.html)

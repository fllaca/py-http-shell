# HTTPS Shell

Simple python server that runs Shell commands

> WARNING: this is an experiment that runs as "root"

```SHELL
# Spotify Commands
curl -X POST 192.168.1.130:5000/command \
    -d '{ "command": "spotify", "environment": { "DISPLAY": ":0" } }' \
    -H "Content-Type: application/json"

curl -X POST 192.168.1.130:5000/command \
    -d '{ "command": "/home/popi/kill-spotify.sh", "environment": { "DISPLAY": ":0" } }' \
    -H "Content-Type: application/json"

# Experimental: play/pause spotify
curl -X POST 192.168.1.130:5000/command \
    -d '{ "command": "dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Play", "environment": { "DISPLAY": ":0" } }' \
    -H "Content-Type: application/json"



# KODI Commands
curl -X POST 192.168.1.130:5000/command \
    -d '{ "command": "kodi", "environment": { "DISPLAY": ":0" } }' \
    -H "Content-Type: application/json"
```

## Useful Scripts

Kill Spotify:

```shell
ps -eo user,pid,ppid,command | grep "spotify" | grep -v grep | awk '{print $2}' | xargs kill
```

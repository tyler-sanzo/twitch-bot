#utils.py
#Utility functions for the bot

import cfg
import json
import time, threading
from time import sleep

#library of messages to look out for
WATCH_MSG =['Pog']

def chat(sock,msg):
    sock.send("PRIVMSG {} : {}\r\n".format(cfg.CHAN,msg).encode("utf-8"))

'''
def threadFillOpList():
    while True:
        try:
            url = "http://tmi.twitch.tv/group/user/limeoats/chatters"
            req = urllib.request(url, headers={"accept": "*/*"})
            response = urllib.urlopen(req).read()
            if response.find("502 Bad Gateway") == -1:
                cfg.oplist.clear()
                data = json.loads(response)
                for p in data["chatters"]["moderators"]:
                    cfg.oplist[p] = "mod"
                for p in data["chatters"]["global_mods"]:
                    cfg.oplist[p] = "global_mod"
                for p in data["chatters"]["admins"]:
                    cfg.oplist[p] = "admin"
                for p in data["chatters"]["staff"]:
                    cfg.oplist[p] = "staff"
        except:
            'do nothing'
        sleep(5)
'''
def isOp(user):
    return user in cfg.oplist

#Spit out Pog whenver someone makes a pog-ish emote, or any other, list is utils.WATCH_MSG
def mirror_msg(sock,tw_msg):
    for test in WATCH_MSG:
        if test.lower() in tw_msg.lower():
            chat(sock,test)


#Clipcounter
#gets a certain emote or phrase
#starts a count
#keeps counting to like 10 of the phrase
# if numberofpogs/(now-start) >10
# send it to clip function




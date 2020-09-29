#bot.py

import cfg
import utils
import socket
import re
import time, _thread
from time import sleep


def main():
    #Networking functions
    s= socket.socket()
    s.connect((cfg.HOST, cfg.PORT))
    s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
    s.send("JOIN {}\r\n".format(cfg.CHAN).encode("utf-8"))

    #_thread.start_new_thread(utils.threadFillOpList, ())
    #CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
    CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")


    while True: ###initializing the loop

        start_time = time.time()
        message_List = []
        message_count = 0 
        pog_count = 0

        while True : ###loop to test for conditions

            current_time=time.time()
            response_with_tags = s.recv(2048).decode("utf-8")
            message_count+=1
            response_no_tags = CHAT_MSG.sub('', response_with_tags)
            if 'pog' in response_no_tags.lower():
                pog_count+=1
                #if pog_count == 1: ###resets timer when first pog is said
                    #current_time = start_time
            message_List.append(response_no_tags)
            print(response_no_tags)
            if current_time - start_time >= 10: #10 second increments of twitch chat
                print('10 seconds have passed, resetting')
                break

        if float(pog_count/message_count) > .5:
            break
    print(message_List) #gets rid of the welcome message, will fix regex later
    print('num of messages is ' + str(message_count))
    print('num of pogs is '+ str(pog_count))

if __name__ == '__main__':
    main()
#! /usr/bin/python
# -*- coding: utf-8 -*-
# version : 1.21 persian language support
import urllib
import json
import time
import urlparse
import requests
answer = "start"
token = "your bot token!"

def mark_read(update_id) : #mark as read
    update_id = int(update_id)
    update_id = update_id + 1 
    update_id = str(update_id)
    urllib.urlopen("https://api.telegram.org/bot" + token + "/getupdates?offset=" + update_id ) #mark as read
link = "https://api.telegram.org/bot" + token + "/getupdates?limit=1"
f = urllib.urlopen(link)
myfile = f.read()
x = json.loads(myfile)

## get respond

try :
    offset = x['result'][0]['update_id']
    print offset
    while (myfile != '{"ok":true,"result":[]}') :
    
        link = "https://api.telegram.org/bot" + token + "/getupdates?limit=1"
        f = urllib.urlopen(link)
        myfile = f.read()
        print myfile
        mark_read(offset)
        
except IndexError :
    nothing = 1 + 1
    #nothing

    
while (answer != "die") :  #holy while
    
    
    f = urllib.urlopen(link)
    myfile = f.read()
    ## get respond
    x = json.loads(myfile)
    while (myfile == '{"ok":true,"result":[]}') :
        time.sleep(1)
        f = urllib.urlopen(link)
        myfile = f.read()
    print ("incoming message : ")
    
    x = json.loads(myfile)
    offset = x['result'][0]['update_id']
    try :
        answer = x['result'][0]['message']['text']
        user_id = x['result'][0]['message']['chat']['id']
        user_id = str(user_id)
        username = x['result'][0]['message']['from']['username']
        print (username + " : " + answer)
        first_name = x['result'][0]['message']['from']['first_name']
        last_name = x['result'][0]['message']['from']['last_name']
    except KeyError :
        mark_read(offset)
    
    
    #lovely ifs :D
    if (answer == "/hi") :
        #tracy_answer
        urllib.urlopen("https://api.telegram.org/bot" + token + "/sendMessage?chat_id=" + user_id + "&text=hi+" + first_name + "+" +last_name )
        mark_read(offset)
    if (answer =="/help") :
        urllib.urlopen("https://api.telegram.org/bot" + token + "/sendMessage?chat_id=" + user_id + "&text=type+/hi+for+hello")
        mark_read(offset)
    if (answer[0:7] == "/google") :
        try : 

            search = answer[8:len(answer)]
            search = search.encode('utf-8')
            
            query = 'q='+search
            
            url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
            search_response = urllib.urlopen(url)
            search_results = search_response.read()
            results = json.loads(search_results)
            x = results
            google_result = x["responseData"]["results"][0]["url"]
            google_result_title = x["responseData"]["results"][0]["titleNoFormatting"]            
            google_last = google_result_title + " : " + google_result
            z = "https://api.telegram.org/bot"+token+"/sendMessage?chat_id=" + user_id + "&text=" + google_last
            requests.post(z)
            mark_read(offset)

        except IndexError :
            mark_read(offset)
        except IOError : #filters of islamic republic of iran
            mark_read(offset)

    else : #when command is incorrect
        mark_read(offset)
        

import requests
import json
from datetime import date
import time
pincode=["683515","683513"]
headers ={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
while(1):
    # welcome="https://api.telegram.org/bot1836438637:AAGBm8Eeqz3mB_v9aKFys9aOFZK7pE2k8Bw/sendmessage?chat_id=-577653573&text=realtime vaccine updates for kerala"
    # requests.get(welcome)
    
    for i in range(0,2):
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        x="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode="+pincode[i]+"&date="+d1+""
        data=requests.get(x,headers=headers)
        results=json.loads(data.text)
        print(results)
        count=results["centers"]
        count1=count[0]
        count2=count1["sessions"]
        if(len(count2)>0):
            for session in count2:

                if session["available_capacity"]==0:
                #    print("no")
                #    nd_url=welcome="https://api.telegram.org/bot1811108401:AAH0Y4Ebv-092C4WIOJejP-tYIheyVjhIRY/sendmessage?chat_id=-1001201651154&text="+"NoSlot"
                #    y=requests.get(nd_url,headers=headers)
                   nd_url=welcome="https://api.telegram.org/bot1811108401:AAH0Y4Ebv-092C4WIOJejP-tYIheyVjhIRY/sendmessage?chat_id=1588002610&text="+"NoSlot"
                   y=requests.get(nd_url,headers=headers)
                else:
                   msg=[]
                   msg.append({"date":session["date"],"vaccine":session["vaccine"]," availability":session["available_capacity"]," minage":session["min_age_limit"]," date":session["date"]})
                   parse_data=json.dumps(msg)
                   parse_data=parse_data.replace("{","")
                   parse_data=parse_data.replace("}","\n\n") 
                   parse_data=parse_data.replace("[","")
                   parse_data=parse_data.replace("]","")
                   parse_data=parse_data.replace(",","\n")
                   print(parse_data)
                   nd_url=welcome="https://api.telegram.org/bot1811108401:AAH0Y4Ebv-092C4WIOJejP-tYIheyVjhIRY/sendmessage?chat_id=1001201651154&text="+parse_data
                   y=requests.get(nd_url,headers=headers)
                   nd_url=welcome="https://api.telegram.org/bot1811108401:AAH0Y4Ebv-092C4WIOJejP-tYIheyVjhIRY/sendmessage?chat_id=1061660183&text="+parse_data
                   y=requests.get(nd_url,headers=headers)
                   print(y)
    time.sleep(100)


#set PYTHONIOENCODING=utf-8
#set PYTHONLEGACYWINDOWSSTDIO=utf-8

def printHide(c):
    if(c == ""):
        return
    print("hide " + c +"\n")
    

import pandas as pd

data = pd.read_csv('pv.csv',encoding="utf-8")

data = data.fillna("")

data['summary'] = data['who'] + ' "' + data['talk'] + '"'
data

p = []
temp_charector = ""
temp_charector_emotion=""
temp_screen = ""
temp_disolve=True
for i,c in data.iterrows():

    if(c['bg']):
        print("show "+c['bg'] +" with Dissolve(1.0)")
        printHide(temp_screen)
        temp_screen = c['bg']

    if(c['bgm'] and c['bgm'] != 'stop music'):
        print('play music "audio/bgm/'+c['bgm']+'.mp3" volume 0.5')
    
    if(c['bgm'] == 'stop music'):
        print("stop music")

    if(c['charector']):
        if(c['charector'] == 'hide'):
            printHide(temp_charector_emotion)
            temp_charector = ""
        else :
            printHide(temp_charector_emotion)
            temp_charector = c['charector']
            temp_charector_emotion = temp_charector +"_"+c['emotion']
            print("show " +temp_charector_emotion)
            temp_disolve = True
        
    else:
        if( c['emotion']):
            printHide(temp_charector_emotion)
            temp_charector_emotion = temp_charector + "_"+c['emotion']
            print("show " + temp_charector_emotion)
            temp_disolve = True
    if(c['effect'] != ""):
        print("show "+c['effect'] +" with Dissolve(1.0)")

    if(temp_disolve):
        print(c['summary'].strip() + " with dissolve")
        temp_disolve = False
    else:
        print(c['summary'].strip())
    if(c['effect'] != ""):
        print("hide "+c['effect'])

printHide(temp_charector_emotion)

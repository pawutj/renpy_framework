#set PYTHONIOENCODING=utf-8
#set PYTHONLEGACYWINDOWSSTDIO=utf-8

import pandas as pd
FILE_NAME = "chap1.csv"
data = pd.read_csv(FILE_NAME,encoding="utf-8")
data = data.fillna("")

# data['summary'] = data['who'] + ' "' + data['talk'] + '"'
# print(data['talk'])


def show_emotion_list(emotion_list,zoom=False):

    if(len(emotion_list) == 1 and zoom == True):
        print(f'show {current_charector_list[0]}_{emotion_list[0]} at centerzoom')
        return

    if(len(emotion_list) == 1):
        print(f'show {current_charector_list[0]}_{emotion_list[0]} at center')
    if(len(emotion_list) == 2):
        print(f'show {current_charector_list[0]}_{emotion_list[0]} at left2')
        print(f'show {current_charector_list[1]}_{emotion_list[1]} at right2')
    if(len(emotion_list) == 3):
        print(f'show {current_charector_list[0]}_{emotion_list[0]} at left3')
        print(f'show {current_charector_list[1]}_{emotion_list[1]} at center')
        print(f'show {current_charector_list[2]}_{emotion_list[2]} at right3')
    return

def hide_emotion_list(emotion_list):
    for i in range(len(current_charector_list)):
        print(f'hide {current_charector_list[i]}_{emotion_list[i]}')
    return
current_charector_list = []
previous_emotion = ""
current_emotion_list = []

def get_charector_talk(c , charector_list , emotion_list):
    if(c):
        return [i for i in charector_list if c in i][0] ,[i for i in emotion_list if c in i][0] 
    return "",""


for i,c in data.iterrows():
    ### Assign ##############################

    bg = c['bg']
    bg_effect = c['bg_effect']
    bgm = c['bgm']
    zoom = c['zoom']
    character = c['character']
    emotion = c['emotion']
    effect = c['effect']
    who_talk = c['who_talk']
    talk = c['talk']
    voice = c['voice']
    charector_talk , emotion_talk = get_charector_talk(who_talk, character.split(',') , emotion.split(','))
    

    #### PreProcess ##########################

    if(emotion == ""):
        current_emotion = previous_emotion
    else:
        current_emotion = emotion



    ### Action ###############################


    if(bg):
        print(f'scene {bg} with Dissolve(1.0)')

    if(bgm and bgm != 'stop'):
        print(f'play music "audio/bgm/{bgm}.mp3 volume 0.5')
    
    if(bgm =='stop'):
        print(f"stop music")

    if(character):
        current_charector_list = character.split(',')
        
    if(emotion):
        emotion_list = emotion.split(',')
        show_emotion_list(emotion_list)

    if(voice):
        print(f'play sound "audio/voice/{voice}"')


    if(talk):
        if(who_talk):
            print(f'c_{charector_talk}_{emotion_talk} "{who_talk} {talk}" with dissolve')
        else:
            print(f'"{talk}" with dissolve')

    if(emotion):
        emotion_list = emotion.split(',')
        hide_emotion_list(emotion_list)

    ### Post ####################################
    if(emotion):
        previous_emotion = emotion

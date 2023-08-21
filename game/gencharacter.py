#set PYTHONIOENCODING=utf-8
#set PYTHONLEGACYWINDOWSSTDIO=utf-8
from os import listdir
from os.path import isfile, join


########################
main_size = "(1433,3100)"

#########################################################################################

mypath = "./images/sprite/ayase"
directory_path ="ayase"
body_path = "ayase_body_00"
size = "(0,1525)"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for c in onlyfiles:
    emo_path = c.split('.')[0]
    print(f"""image {body_path}_{emo_path}:""")
    print(f"""    zoom 0.75""")
    print(f"""    im.Composite({main_size}, {size},"sprite/{directory_path}/{body_path}.png",{size},"sprite/{directory_path}/{emo_path}.png") """)
#Side#
for c in onlyfiles:
    emo_path = c.split('.')[0]
    print(f"""image side {body_path}_{emo_path}:""")
    print(f"""    zoom 0.5""")
    print(f"""    yoffset 300""")
    print(f"""    xoffset -175""")
    print(f"""    im.Composite({main_size}, {size},"sprite/{directory_path}/{body_path}.png",{size},"sprite/{directory_path}/{emo_path}.png") """)

for c in onlyfiles:
    emo_path = c.split('.')[0]
    print(f'define c_{body_path}_{emo_path} = Character("อายาเสะ",image = "{body_path}_{emo_path}" ,color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])')
################################################################################################################

mypath = "./images/sprite/eri"
directory_path ="eri"
body_path = "eri_body_00"
size = "(0,1625)"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for c in onlyfiles:
    emo_path = c.split('.')[0]
    print(f"""image {body_path}_{emo_path}:""")
    print(f"""    zoom 0.75""")
    print(f"""    im.Composite({main_size}, {size},"sprite/{directory_path}/{body_path}.png",{size},"sprite/{directory_path}/{emo_path}.png") """)
#Side#
for c in onlyfiles:
    emo_path = c.split('.')[0]
    print(f"""image side {body_path}_{emo_path}:""")
    print(f"""    zoom 0.5""")
    print(f"""    yoffset 300""")
    print(f"""    xoffset -175""")
    print(f"""    im.Composite({main_size}, {size},"sprite/{directory_path}/{body_path}.png",{size},"sprite/{directory_path}/{emo_path}.png") """)

for c in onlyfiles:
    emo_path = c.split('.')[0]
    print(f'define c_{body_path}_{emo_path} = Character("เอริ",image = "{body_path}_{emo_path}" ,color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])')

######################################################################################################

mypath = "./images/sprite/mikan"
directory_path ="mikan"
body_path = "mikan_body"
size = "(0,1625)"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for c in onlyfiles:
    emo_path = c.split('.')[0]
    print(f"""image {body_path}_{emo_path}:""")
    print(f"""    zoom 0.75""")
    print(f"""    im.Composite({main_size}, {size},"sprite/{directory_path}/{body_path}.png",{size},"sprite/{directory_path}/{emo_path}.png") """)
#Side#
for c in onlyfiles:
    emo_path = c.split('.')[0]
    print(f"""image side {body_path}_{emo_path}:""")
    print(f"""    zoom 0.5""")
    print(f"""    yoffset 300""")
    print(f"""    xoffset -175""")
    print(f"""    im.Composite({main_size}, {size},"sprite/{directory_path}/{body_path}.png",{size},"sprite/{directory_path}/{emo_path}.png") """)

for c in onlyfiles:
    emo_path = c.split('.')[0]
    print(f'define c_{body_path}_{emo_path} = Character("มิคัง",image = "{body_path}_{emo_path}" ,color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])')

#################################################################################################################################

###############################################################################################################################

mypath = "./images/sprite/mikan2"
directory_path ="mikan2"
body_path = "mikan2_body_00"
size = "(0,1625)"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for c in onlyfiles:
    emo_path = c.split('.')[0]
    print(f"""image {body_path}_{emo_path}:""")
    print(f"""    zoom 0.75""")
    print(f"""    im.Composite({main_size}, {size},"sprite/{directory_path}/{body_path}.png",{size},"sprite/{directory_path}/{emo_path}.png") """)
#Side#
for c in onlyfiles:
    emo_path = c.split('.')[0]
    print(f"""image side {body_path}_{emo_path}:""")
    print(f"""    zoom 0.5""")
    print(f"""    yoffset 300""")
    print(f"""    xoffset -175""")
    print(f"""    im.Composite({main_size}, {size},"sprite/{directory_path}/{body_path}.png",{size},"sprite/{directory_path}/{emo_path}.png") """)

for c in onlyfiles:
    emo_path = c.split('.')[0]
    print(f'define c_{body_path}_{emo_path} = Character("มิคัง",image = "{body_path}_{emo_path}" ,color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])')

#################################################################################################################################


###############################################################################################################################

mypath = "./images/sprite/eri2"
directory_path ="eri2"
body_path = "eri2_body_0"
size = "(0,1625)"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for c in onlyfiles:
    emo_path = c.split('.')[0]
    print(f"""image {body_path}_{emo_path}:""")
    print(f"""    zoom 0.75""")
    print(f"""    im.Composite({main_size}, {size},"sprite/{directory_path}/{body_path}.png",{size},"sprite/{directory_path}/{emo_path}.png") """)
#Side#
for c in onlyfiles:
    emo_path = c.split('.')[0]
    print(f"""image side {body_path}_{emo_path}:""")
    print(f"""    zoom 0.5""")
    print(f"""    yoffset 300""")
    print(f"""    xoffset -175""")
    print(f"""    im.Composite({main_size}, {size},"sprite/{directory_path}/{body_path}.png",{size},"sprite/{directory_path}/{emo_path}.png") """)

for c in onlyfiles:
    emo_path = c.split('.')[0]
    print(f'define c_{body_path}_{emo_path} = Character("เอริ",image = "{body_path}_{emo_path}" ,color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])')

#################################################################################################################################




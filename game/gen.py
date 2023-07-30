from os import listdir
from os.path import isfile, join


########################
main_size = "(1433,3100)"

#########################################################################################

mypath = "./images/sprite/ayase"
directory_path ="ayase"
body_path = "ayase_body_00"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
size = "(0,1525)"
for c in onlyfiles:
    emo_path = c.split('.')[0]
    print(f"""image {body_path}_{emo_path}:""")
    print(f"""    zoom 0.75""")
    print(f"""    im.Composite({main_size}, {size},"sprite/{directory_path}/{body_path}.png",{size},"sprite/{directory_path}/{emo_path}.png") """)

################################################################################################################







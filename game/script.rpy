# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

image artroom_afternoon = im.Scale("bg/school-park1.jpg",1920,1080)
# The game starts here.




define ayase = Character("อายาเสะ",image = "ayase_body_00_ayase_ah" ,color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
define eri = Character("เอริ",image = "eri_body_00_eri_angry" ,color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])

# image side ayase_body_00_ayase_ah:
#     zoom 0.5
#     yoffset 300
#     xoffset -175
#     im.Composite((1433,3100), (0,1525),"sprite/ayase/ayase_body_00.png",(0,1525),"sprite/ayase/ayase_ah.png")

# image side eri_body_00_eri_angry:
#     zoom 0.5
#     yoffset 300
#     xoffset -175
#     im.Composite((1433,3100), (0,1625),"sprite/eri/eri_body_00.png",(0,1625),"sprite/eri/eri_angry.png") 

image ayase_0: 
    zoom 0.75
    im.Composite((1433,3100), (0,1525), "sprite/ayase/ayase_body_00.png" ,(0,1525),"sprite/ayase/ayase_ah.png")

image ayase_0_1: 
    zoom 0.75
    im.Composite((1433,3100), (0,1825), "sprite/ayase2/ayase2_body_00.png" ,(0,1825),"sprite/ayase2/ayase2_angry.png")

image eri_0_0: 
    zoom 0.75
    im.Composite((1433,3100), (0,1625), "sprite/eri/eri_body_00.png" ,(0,1625),"sprite/eri/eri_angry.png")

image mikan_0_0:
    zoom 0.75
    im.Composite((1433,3100), (0,1625), "sprite/mikan/mikan_body.png" ,(0,1625),"sprite/mikan/mikan_ah.png")




image ayase_1: 
    zoom 0.75
    im.Composite((1433,3100), (0,1525), "sprite/ayase/ayase_body_00.png" ,(0,1525),"sprite/ayase/ayase_lazy.png")

image ayase_1_1: 
    zoom 0.75
    im.Composite((1433,3100), (0,1525), "sprite/ayase2/ayase2_body_00.png" ,(0,1525),"sprite/ayase2/ayase2_sad.png")


image ayase_2: 
    zoom 0.75
    im.Composite((1433,3100), (0,1525), "sprite/ayase/ayase_body_00.png" ,(0,1525),"sprite/ayase/ayase_oh.png")

image ayase_2_1: 
    zoom 0.75
    im.Composite((1433,3100), (0,1525), "sprite/ayase2/ayase2_body_00.png" ,(0,1525),"sprite/ayase2/ayase2_oh.png")



transform left3:
    xalign -0.25
    yalign 1.0

transform right3:
    xalign 1.25
    yalign 1.0

transform left2:
    xalign -0.05
    yalign 1.0

transform right2:
    xalign 1.05
    yalign 1.0

transform centerzoom:
    zoom 1.4
    xalign 0.5
    yalign 0.85

init -2:
    style nvl_dialogue:
        line_spacing 10
    style say_dialogue:
        line_spacing 10   


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    jump chap2

    scene bg room

    show ayase_body_00_ayase at center

    e "Once you add a story, pictures, and music, you can release it to the world!" with dissolve

    hide ayase_body_00_ayase


    
    show mikan_0_0 at center

    e "Once you add a story, pictures, and music, you can release it to the world!" with dissolve

    hide mikan_0_0



    show eri_0_0 at center

    e "Once you add a story, pictures, and music, you can release it to the world!" with dissolve

    hide eri_0_0


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ayase_0 at center
    e "You've created a new Ren'Py game." with dissolve
    hide ayase_0 

    show ayase_0 at centerzoom
    e "You've created a new Ren'Py game." with dissolve
    hide ayase_0 


    show ayase_0 at left3
    show ayase_1 at center
    show ayase_2 at right3

    # These display lines of dialogue.

    e "You've created a new Ren'Py game." with dissolve
    
    hide ayase_0 
    hide ayase_1 
    hide ayase_2



    show ayase_0 at left3
    show ayase_1 at center
    show ayase_2 at right3

    # These display lines of dialogue.

    e "You've created a new Ren'Py game.2" with dissolve
    
    hide ayase_0 
    hide ayase_1 
    hide ayase_2


    show ayase_0 at left2
    show ayase_2 at right2

    e "You've created a new Ren'Py game." with dissolve

    hide ayase_0
    hide ayase_2


    show ayase_0_1 at left
    show ayase_1_1 at center
    show ayase_2_1 at right

    e "Once you add a story, pictures, and music, you can release it to the world!" with dissolve

    # This ends the game.

    return

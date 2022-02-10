#a modified version of Nadia Nova phone sms system
#from https://nadianova.itch.io/phone-message-system-for-renpy
#modifications done by BadMustard

############ phone code here########

# here is a new menu that has more options than two
# basically i just added one more textbutton here, and the additional labels needed in the call
# if you wish to make a menu with one or four just copy the code below and modify it a bit


screen phone_reply(reply1, label1, reply2, label2):
    modal True
    vbox:
        xalign 0.5
        yalign 0.8
        spacing 5

        textbutton "[reply1]" action Jump(label1) style "phone_reply"
        textbutton "[reply2]" action Jump(label2) style "phone_reply"

screen phone_reply3(reply1, label1, reply2, label2, reply3, label3,):
    modal True
    vbox:
        xalign 0.5
        yalign 0.8
        spacing 5

        textbutton "[reply1]" action Jump(label1) style "phone_reply"
        textbutton "[reply2]" action Jump(label2) style "phone_reply"
        textbutton "[reply3]" action Jump(label3) style "phone_reply"

screen phone_message(avatar, who, what):
    text phone_too style "nameit"
    vbox at incoming_message:
        style_group "phone_message"
        add avatar
        add "receive_pointer" at phone_message_bubble_tip
        frame:
            style_group "phone_message"

            vbox:
                style "phone_message_contents"
                text what style "phone_message_what"

screen phone_message2(who, what):
    text phone_too style "nameit"
    vbox at incoming_message:
        style_group "phone_send_message"
        xalign 1.0
        add "send_pointer" at phone_message_bubble_tip2

        frame:
            style_group "phone_send_message"

            vbox:
                style "phone_send_message_contents"
                text what style "phone_send_message_what"

screen phone_message3(what):
    text phone_too style "nameit"

    vbox at incoming_message:
        style_group "phone_send_message"
        add "send_pointer" at phone_message_bubble_tip2

        frame:
            style_group "phone_send_message"

            vbox:
                style "phone_send_message_contents"
                text what style "phone_send_message_what"


screen phone_message4(avatar, who, what):
    text phone_too style "nameit"
    vbox at incoming_message:
        style_group "phone_send_message"
        add avatar at phone_avatar_bubble_tip2
        add "send_pointer" at phone_message_bubble_tip2
        frame:
            style_group "phone_send_message"

            vbox:
                style "phone_send_message_contents"
                text what style "phone_send_message_what"


screen phone_message_image(avatar, who, what, img):
    text phone_too style "nameit"
    vbox at incoming_message:
        style_group "phone_message"
        add avatar #the senders avatar
        add "receive_pointer" at phone_message_bubble_tip

        frame:
            style_group "phone_message"

            vbox:
                style "phone_message_contents"
                text what style "phone_message_what"
                imagebutton idle phone_images[img].thumb: #use thumb as the idle image button
                    action Show("phone_closeup", dissolve, phone_images[img].images)
                    xalign 0.5
                    yalign 0

screen phone_message_image2(what, img):
    text phone_too style "nameit"
    vbox at incoming_message:
        style_group "phone_send_message"
        xalign 1.0
        add "send_pointer" at phone_message_bubble_tip2

        frame:
            style_group "phone_send_message"

            vbox:
                style "phone_send_message_contents"
                text what style "phone_send_message_what"
                imagebutton idle phone_images[img].thumb: #use thumb as the idle image button
                    action Show("phone_closeup", dissolve, phone_images[img].images)
                    xalign 0.5
                    yalign 1.0

screen phone_closeup(images):

    imagebutton idle images[closeup_page]: #use images as the idle image button
        #click the image to close
        action [SetVariable("closeup_page", 0), Hide("phone_closeup", dissolve)]
        xalign 0.5
        yalign 1.0
        background "#fff8"

# Picking up the phone
transform phone_pickup:
    yalign 1.0 xalign 0.5
    easein 0.3 yoffset 20

transform phone_hide:
    yalign 1.0 xalign 0.5
    yoffset 100
    easein 0.3 yoffset 1300

transform phone_message_bubble_tip:
    xoffset 20
    yoffset 1

transform phone_message_bubble_tip2:
    #xoffset -315
    xoffset -345
    yoffset 1

transform phone_avatar_bubble_tip2:
    #xoffset -315
    xoffset -405
    yoffset 1

transform scrolling_out_message:
    easeout 0.1 yoffset -30 alpha 0

transform incoming_message:
    yoffset 100
    alpha 0
    parallel:
        easein 0.1 alpha 1
    parallel:
        easein 0.2 yoffset 0
    on subir:
        yoffset -300
    on hide:
        scrolling_out_message

transform subir:
    ypos 120

transform prueba:
    yalign 0.3
    xalign 0.9


#### labels to shortcut stuff so you don't need to copy paste stuff repeatedly! #####


label phone_start(face):
    window hide
    if face == 0:
        show phone0 at phone_pickup
    else:
        show phone1 at phone_pickup
    $ renpy.pause(0.2)
    return

label phone_msg:
    $ renpy.pause()
    hide screen phone_message
    $ renpy.pause(0.1)
    return

label phone_msg2:
    $ renpy.pause()
    hide screen phone_message2
    $ renpy.pause(0.1)
    return

label phone_after_menu:
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    hide screen phone_message_image2
    $ renpy.pause(0.1)
    return

label phone_end(face):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    hide screen phone_message_image
    hide screen phone_message_image2
    $ renpy.pause(0.2)
    if face == 0:
        show phone0 at phone_hide
    else:
        show phone1 at phone_hide
    $ renpy.pause(0.2)
    return

label message(avatar, who, what):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    hide screen phone_message_image2
    $ renpy.pause(0.1)
    show screen phone_message(avatar, who, what)
    return

label message_reply(what):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    hide screen phone_message_image2
    $ renpy.pause(0.1)
    show screen phone_message3(what)
    return

label message_img(avatar, who, what, img):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    hide screen phone_message_image2
    $ renpy.pause(0.1)
    if who.lower() == "me":
        show screen phone_message_image2(what, img)
    else:
        show screen phone_message_image(avatar, who, what, img)
    return

label message_start(avatar, who, what):
    if who.lower() == "yo":
        show screen phone_message4(avatar, who, what)
    else:
        show screen phone_message(avatar, who, what)
    return


label mensaje(who, what):
 #escojemos el avatar actual
   if who.lower()== "yo":
     $ avatar = "auroraAvatar"
     show screen phone_message4(avatar, who, what)
   else:
     $  avatar = "brunaAvatar"
     show screen phone_message(avatar, who, what)
   pause



   return


init 5:

    style phone_send_message_frame:
        text_align 1.0
        xalign 1.0
        #xoffset -684
        xoffset -715
        background Frame("bubble_send", 10,10,10,10)
        ypadding 10
        xpadding 10

    style phone_message_frame:
        background Frame("bubble_receive", 10,10,10,10)
        ypadding 10
        xpadding 10

    style phone_send_message_what is phone_send_message:
        xalign 1.0
        text_align 1.0
        color "#888888" #text color for sent messages
        size 24

    style phone_message_what is phone_message:
        color "#888888" #text color for received messages
        size 24

    style phone_send_message_vbox:
        text_align 1.0
        xalign 1.0
        yalign 0
        ypos 305
        xsize 400
        xoffset -39

    style phone_message_vbox:
        xalign 0.5
        yalign 0
        #ypos 200
        ypos 120
        xsize 400
        xoffset -38

    style phone_send_message_contents:
        text_align 1.0
        spacing 10

    style phone_message_contents:
        spacing 10

    style phone_send_message is say_dialogue:
        xoffset 0
        outlines []
        text_align 1.0
        xalign 1.0
        yalign 0

    style phone_message is say_dialogue:
        xoffset 0
        outlines []
        xalign 0
        yalign 0

    style phone_reply is default:
        size 18
        xalign 0.5
        xsize 475
        background Solid("#666") #menu button color
        hover_background Solid("#78E8A0") #menu button mouse over change color
        ypadding 10
        xpadding 10

    style phone_reply_text:
        xalign 0.5

    style nameit:
        ypos 150
        xpos 775
        text_align 0
        color "#e1e1e1" #name color

######### phone code ends here ##########

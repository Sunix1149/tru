init -1 style default properties gui.text_properties() language gui.language
init -1 style input properties gui.text_properties("input", accent=True) adjust_spacing False
init -1 style hyperlink_text hover_underline True properties gui.text_properties("hyperlink", accent=True)
init -1 style gui_text properties gui.text_properties("interface")
init -1 style button properties gui.button_properties("button")
init -1 style button_text is gui_text properties gui.text_properties("button") yalign 0.5
init -1 style label_text is gui_text properties gui.text_properties("label", accent=True)
init -1 style prompt_text is gui_text properties gui.text_properties("prompt")
init -1:
    style bar:
        left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
        ysize gui.bar_size
        right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
init -1:
    style vbar:
        bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)
        top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
        xsize gui.bar_size
init -1:
    style scrollbar:
        ysize gui.scrollbar_size
        base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
        thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
init -1:
    style vscrollbar:
        base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        xsize gui.scrollbar_size
        thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
init -1:
    style slider:
        thumb_offset 0
        ysize gui.slider_size
        base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
        thumb "gui/slider/horizontal_[prefix_]thumb.png"
init -1:
    style vslider:
        base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
        xsize gui.slider_size
        thumb "gui/slider/vertical_[prefix_]thumb.png"
init -1 style frame padding gui.frame_borders.padding background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)
init -501:
    screen say(who, what):
        style_prefix "say"

        window:
            id "window"
            if csbox:
                background None
            if who is not None and not csbox:
                window:
                    id "namebox"
                    style "namebox"
                    text who id "who"
            if csbox:
                text what id "what" font "HELVETICA_LT_NARROW.ttf" color "#f7dd74" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] size 42 xmaximum 950 xoffset 230 yoffset 50
            else:
                text what id "what"
        if not renpy.variant("small"):
            add SideImage() xalign 0.0 yalign 1.0
init python:

    config.character_id_prefixes.append('namebox')

init -1 style window is default
init -1 style say_label is default
init -1 style say_dialogue is default
init -1 style say_thought is say_dialogue
init -1 style namebox is default
init -1 style namebox_label is say_label
init -1:
    style window:
        xalign 0.5
        ysize gui.textbox_height
        background Image("gui/textbox.png", xalign=0.5, yalign=1.0)
        yalign gui.textbox_yalign
        xfill True
init -1:
    style namebox:
        xpos gui.name_xpos
        xanchor gui.name_xalign
        xsize gui.namebox_width
        ysize gui.namebox_height
        ypos gui.name_ypos
        padding gui.namebox_borders.padding
        background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
init -1:
    style say_label:
        xalign gui.name_xalign
        properties gui.text_properties("name", accent=True)
        yalign 0.5
init -1:
    style say_dialogue:
        line_spacing -5
        xpos gui.dialogue_xpos
        properties gui.text_properties("dialogue")
        xsize gui.dialogue_width
        ypos gui.dialogue_ypos
init -501:
    screen input(prompt):
        style_prefix "input"

        window:
            vbox:
                xalign gui.dialogue_text_xalign
                xpos gui.dialogue_xpos
                xsize gui.dialogue_width
                ypos gui.dialogue_ypos
                text prompt style "input_prompt"
                input id "input"
init -1 style input_prompt is default
init -1 style input_prompt xalign gui.dialogue_text_xalign properties gui.text_properties("input_prompt")
init -1 style input xalign gui.dialogue_text_xalign xmaximum gui.dialogue_width
init -501:
    screen choice(items):
        style_prefix "choice"

        image Image("gui/choice_window.png")
        vbox:
            for i in items:
                textbutton i.caption action [Play("sfx","audio/PhoneSelect.mp3"),i.action]
define config.narrator_menu = True
init -1 style choice_vbox is vbox
init -1 style choice_button is button
init -1 style choice_button_text is button_text
init -1:
    style choice_vbox:
        xalign 0.47
        spacing gui.choice_spacing
        yalign 0.3
        yanchor 0.0
init -1 style choice_button is default properties gui.button_properties("choice_button")
init -1 style choice_button_text is default properties gui.button_text_properties("choice_button")
init -501:
    screen quick_menu():
        zorder 100

        if quick_menu:
            vbox style_prefix "quick" spacing -5
            imagebutton idle "gui/back_pills_vert.png" action Function(renpy.rollback, force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=False) xalign 0.086 yalign 0.995
            imagebutton idle "gui/pause_phone.png" action ShowMenu() xalign 0.964 yalign 0.979
init python:

    config.overlay_screens.append("quick_menu")

default quick_menu = True
init -1 style quick_button xalign 1.0
init -1 style quick_button_text is button_text
init -1:
    style quick_button_text:
        color '#000000'
        xalign 1.0
        insensitive_color 'FF0000'
        hover_color '#555555'
        size 50
init -501:
    screen newgame_hover_bar():
        add "gui/menu 2/hover_bar.png" at from_left(428, 0.0)
        add "gui/menu 2/newgame2_ro.png"
init -501:
    screen continue_hover_bar():
        add "gui/menu 2/hover_bar.png" at from_left(528, -0.03)
        add "gui/menu 2/continue2_ro.png"
init -501:
    screen option_hover_bar():
        add "gui/menu 2/hover_bar.png" at from_left(628, -0.075)
        add "gui/menu 2/options2_ro.png"
init -501:
    screen about_hover_bar():
        add "gui/menu 2/hover_bar.png" at from_left(728, -0.14)
        add "gui/menu 2/about2_ro.png"
transform from_left(posy, x):
    subpixel True xalign -1.0 yanchor 0.5 ypos posy
    linear 0.14 xalign x
    on hide:
        linear 0.48 xalign -1.0
init -501:
    screen navigation():
        style_prefix "navigation"

        imagebutton idle "gui/menu 2/newgame2.png" hover "gui/menu 2/newgame2_ro.png" xpos 0 ypos 0 focus_mask "gui/menu 2/newgame2_mask.png" activate_sound "audio/MainMenuPress.mp3" hover_sound "audio/MainMenuRollover.mp3" action Hide("newgame_hover_bar"), SetField(persistent, "new_ending", False), Start() hovered ShowMenu("newgame_hover_bar", _transition = Dissolve(0.0)) unhovered Hide("newgame_hover_bar")
        imagebutton idle "gui/menu 2/continue2.png" hover "gui/menu 2/continue2_ro.png" xpos 0 ypos 0 focus_mask "gui/menu 2/continue2_mask.png" activate_sound "audio/MainMenuPress.mp3" hover_sound "audio/MainMenuRollover.mp3" action SetField(persistent, "new_ending", False), ShowMenu("load") hovered ShowMenu("continue_hover_bar", _transition = Dissolve(0.0)) unhovered Hide("continue_hover_bar")
        imagebutton idle "gui/menu 2/options2.png" hover "gui/menu 2/options2_ro.png" xpos 0 ypos 0 focus_mask "gui/menu 2/options2_mask.png" activate_sound "audio/MainMenuPress.mp3" hover_sound "audio/MainMenuRollover.mp3" action SetField(persistent, "new_ending", False), ShowMenu("preferences") hovered ShowMenu("option_hover_bar", _transition = Dissolve(0.0)) unhovered Hide("option_hover_bar")
        imagebutton idle "gui/menu 2/about2.png" hover "gui/menu 2/about2_ro.png" xpos 0 ypos 0 focus_mask "gui/menu 2/about2_mask.png" activate_sound "audio/MainMenuPress.mp3" hover_sound "audio/MainMenuRollover.mp3" action SetField(persistent, "new_ending", False), ShowMenu("about") hovered ShowMenu("about_hover_bar", _transition = Dissolve(0.0)) unhovered Hide("about_hover_bar")
        imagebutton idle "gui/menu 2/exit2.png" hover "gui/menu 2/exit2_ro.png" xpos 0 ypos 0 focus_mask "gui/menu 2/exit2_mask.png" activate_sound "audio/MainMenuPress.mp3" hover_sound "audio/MainMenuRollover.mp3" action SetField(persistent, "new_ending", False), Quit()
init -1 style navigation_button is gui_button
init -1 style navigation_button_text is gui_button_text
init -1 style navigation_button size_group "navigation" properties gui.button_properties("navigation_button")
init -1 style navigation_button_text properties gui.button_text_properties("navigation_button")
transform main_logo_transform:
    xalign .7 yalign 0.3 size (580.0*1.2,395.0*1.2) xanchor .5 yanchor .5
    easein 0.35 size (580.0*1.3, 395.0*1.3)
    linear 1.5 size (580.0*1.2,395.0*1.2)
    repeat
init -1 image main_menu_bg = Movie(play = "gui/menu 2/BG living.webm", start_image = "gui/menu 2/menu_bg.png")
init -501:
    screen main_menu():
        style_prefix "main_menu"
        tag menu

        on "show" action Function(renpy.music.stop, channel="vo", fadeout=0.5)
        on "replace" action Function(renpy.music.stop, channel="vo", fadeout=0.5)
        add "main_menu_bg"
        frame
        if persistent.endings:
            imagebutton idle "gui/ending_tracker/text_access.png" hover "gui/ending_tracker/text_access.png" action Show("ending_tracker_screen"), With(None), Play("sound", "audio/Phone_slide.mp3"), SetField(persistent, "new_ending", False) xalign 0.925 yalign 0.9 at idle_rotate
        use navigation
        if persistent.new_ending:
            on "show" action Play("sound", "audio/NewTextAlert.mp3")
            add "new_message_animation"
transform idle_rotate:
    rotate 0
    linear 1.0 rotate 3
    linear 1.0 rotate 0
    linear 1.0 rotate 3
    linear 1.0 rotate 0
    repeat
init 499:
    image new_message_animation:
        "NewMessageSequence/NewMessage_0001.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0002.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0003.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0004.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0005.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0006.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0007.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0008.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0009.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0010.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0011.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0012.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0013.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0014.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0015.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0016.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0017.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0018.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0019.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0020.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0021.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0022.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0023.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0024.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0025.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0026.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0027.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0028.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0029.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0030.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0031.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0032.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0033.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0034.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0035.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0036.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0037.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0038.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0039.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0040.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0041.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0042.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0043.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0044.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0045.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0046.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0047.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0048.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0049.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0050.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0051.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0052.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0053.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0054.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0055.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0056.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0057.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0058.png"
        pause 0.041
        "NewMessageSequence/NewMessage_0059.png"
        pause 0.041
        Solid("#00000000")
init -1 style alt_menu_frame is empty
init -1 style alt_menu_vbox is vbox
init -1 style alt_menu_text is gui_text
init -1 style alt_menu_label is gui_label
init -1 style alt_menu_label_text color '#FFFFFF'
init -1 style main_menu_frame is empty
init -1 style main_menu_vbox is vbox
init -1 style main_menu_text is gui_text
init -1 style main_menu_title is main_menu_text
init -1 style main_menu_version is main_menu_text
init -1 style main_menu_button_text size 60
init -1 style main_menu_frame yfill True xsize 420
init -1:
    style main_menu_vbox:
        xalign 1.0
        xmaximum 1200
        yalign 1.0
        xoffset -30
        yoffset -30
init -1 style main_menu_text properties gui.text_properties("main_menu", accent=True)
init -1 style main_menu_title properties gui.text_properties("title")
init -1 style main_menu_version properties gui.text_properties("version")
transform fade_in(t):
    alpha 0.0
    linear t alpha 1.0
init -501:
    screen game_menu(title, scroll=None, yinitial=0.0):
        style_prefix "game_menu"

        add "main_menu_bg"
        add "gui/menu 2/menu_backtray.png" at fade_in(0.5) alpha 0.65
        frame:
            style "game_menu_outer_frame"
            at fade_in(0.8)
            hbox:
                frame style "game_menu_navigation_frame"
                frame:
                    style "game_menu_content_frame"
                    if scroll == "viewport":
                        viewport:
                            yinitial yinitial
                            side_yfill True
                            vbox:
                                xsize 700
                                transclude
                    elif scroll == "vpgrid":
                        vpgrid:
                            cols 1
                            yinitial yinitial
                            scrollbars "vertical"
                            mousewheel True
                            edgescroll True
                            draggable True
                            pagekeys True
                            side_yfill True
                            transclude
                    else:
                        transclude
        use navigation
        if main_menu:
            key "game_menu" action ShowMenu("main_menu")
init -1 style game_menu_outer_frame is empty
init -1 style game_menu_navigation_frame is empty
init -1 style game_menu_content_frame is empty
init -1 style game_menu_viewport is gui_viewport
init -1 style game_menu_side is gui_side
init -1 style game_menu_scrollbar is gui_vscrollbar
init -1 style game_menu_label is gui_label
init -1 style game_menu_label_text is gui_label_text
init -1 style return_button is navigation_button
init -1 style return_button_text is navigation_button_text
init -1:
    style game_menu_outer_frame:
        top_padding 15
        right_padding 60
        bottom_padding 45
init -1 style game_menu_navigation_frame yfill True xsize 500
init -1:
    style game_menu_content_frame:
        right_margin 420
        top_margin 20
        left_margin 300
init -1 style game_menu_viewport xsize 1700
init -1 style game_menu_vscrollbar unscrollable gui.unscrollable
init -1 style game_menu_side spacing 15
init -1 style game_menu_label xpos 75 ysize 180
init -1:
    style game_menu_label_text:
        color gui.accent_color
        yalign 0.5
        size gui.title_text_size
init -1:
    style return_button:
        xpos gui.navigation_xpos
        yalign 1.0
        yoffset -45
init -501:
    screen aboutmenu():
        tag menu

        use game_menu(_("About"), scroll="viewport"):
            style_prefix "about"
            frame:
                vbox xalign .5 yalign .5 spacing 45
            hbox:
                xsize 200
                ysize 400
                ypos 40
                spacing 20
                textbutton _("ABOUT") text_idle_color "#ffffff" text_hover_color "#2cabf5" text_selected_color "#AAAAAA" action ShowMenu("about")
                textbutton _("ACTORS") text_idle_color "#ffffff" text_hover_color "#2cabf5" text_selected_color "#AAAAAA" action ShowMenu("actors")
                textbutton _("ARTISTS") text_idle_color "#ffffff" text_hover_color "#2cabf5" text_selected_color "#AAAAAA" action ShowMenu("artists")
            viewport:
                scrollbars "vertical"
                style_prefix "vbar"
                mousewheel True
                draggable True
                xsize 1100
                ypos -263
                side_yfill True
                vbox:
                    transclude
init -1 style vbar_vscrollbar xpos 10
init -501:
    screen about():
        style_prefix "about"
        tag menu

        use aboutmenu():
            vbox:
                text _("\nThis video game is entirely based on real events, encounters, and personalities. \n \nAny content viewed as offensive is a reflection of American culture and not endorsed by Class of '09 or it's staff.\n\n\nApparently all characters depicted are over 18.\n\n\n\n\n\nThis program contains free software licensed under a number of licenses, including the GNU Lesser General Public License. A complete list of software is available at {a=http://www.renpy.org/doc/html/license.html}http://www.renpy.org/doc/html/license.html{/a}\n\n\n") outlines []
init -501:
    screen actors():
        tag menu

        use aboutmenu():
            hbox:
                spacing 55
                ypos -20
                xpos 5
                vbox:
                    style_prefix "actor"
                    text actor_credits outlines []
                vbox:
                    style_prefix "char"
                    text char_credits outlines []
define actor_credits = _("""
Elsie Lovelock
Kayli Mills
Max Field


Kira Buckland
Anne Yatco
Sarah Ruth Thomas
Tiana Camacho
Katy Johnson
Marissa Lenti
Anthony Sardinha
as herself
Michael Potok
Corinne Sudberg
Joshua Tomar
Lyle Rath
Chris McCullough
Jas Patrick
Dreux Ferrano Jr.
Connor Quinn
Patrick Mealey
Joe Boisits
Joshua Gotay
Griffin Puatu
Gary Scales


Carl G. Brooks
Tom Laflin
Bradley Gareth
Tom Schalk

Belsheber Rusape
Erin Nicole Lundquist
Bryson Baugus
Haley Parsley
Anna Kingsley
Brandon Winckler
Lizzy Hofe
Michaela Laws
Krystal LaPorte

""")
define char_credits = _("""
NICOLE
JECKA
KYLAR
CRISPIN
JEFFERY
ARI
MS. AMES
PRINCIPAL LYNN
MEGAN
KELLY
MOM
COUNSELOR
EMILY
HUNTER
KAREN
MALL COP
MR. BURLEDAY
MR. KATZ
MR. LORRE
COACH COLBY
COP
KYLE
TRODY
BRAXTON
EMT
GUEST SPEAKER
FIEND
COROLLA DRIVER
CAMRY DRIVER
MUSTANG DRIVER
JAIL PHONE
ROSSLER

ADD'L STUDENTS










""")
define artist_credits = _("""

{size=24}PUBLISHED BY{/size}
Wrath Club

{size=24}WRITTEN & DIRECTED BY{/size}
SBN3

{size=24}CG ARTISTS{/size}
Drowzzi
Steven Newman
NTDanny
Smex

{size=24}SPRITE ARTISTS{/size}
Danny Espinoza
Dalmax
Rayleigh Scale
Niko Brenner
Jokob
Alesha Marie

{size=24}SCORED BY{/size}
Aaron Monroe
Hoobastankonia

{size=24}VFX{/size}
Shawn Smith

{size=24}PROGRAMMERS{/size}
Dipesh Aggarwal
Zac Connelly
RockStar8

{size=24}EXECUTIVE PRODUCERS{/size}
Austin Berglin
Lyle Rath

""")
init -501:
    screen artists():
        style_prefix "artist"
        tag menu

        use aboutmenu():
            hbox:
                ypos -80
                xpos 110
                text artist_credits outlines []
define gui.about = ""
init -1:
    style artist_text:
        color '#FFF'
        kerning 1
        text_align .5
        outlines [(1, "#000", 0, 0)]
        size 40
init -1 style about_hbox bottom_margin 25 top_margin 50
init -1 style about_label size 100
init -1 style about_label_text size 100
init -1 style about_button size 100
init -1 style about_button_text color '#000000' size 60
init -1 style about_label_text size 100
init -1:
    style char_text:
        color '#FFF'
        kerning 1
        text_align 0.0
        outlines [(1, "#000", 0, 0)]
        size 28
init -1 style char_hbox top_margin 30
init -1:
    style actor_text:
        color '#FFF'
        kerning 1
        text_align 1.0
        outlines [(1, "#000", 0, 0)]
        size 28
init -1:
    style about_text:
        color '#FFF'
        kerning 1
        outlines [(1, "#000", 0, 0)]
        size 30
init -501:
    screen pause_save():
        tag menu

        use pause_file_slots(_("Save"))
init -501:
    screen save():
        tag menu

        use file_slots(_("Save"))
init -501:
    screen load():
        tag menu

        use file_slots(_("Load"))
init -501:
    screen file_slots(title):
        default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Auto saves"), quick=_("Quick saves"))
        use game_menu(title):
            fixed:
                order_reverse True
                button:
                    style "page_label"
                    key_events True
                    xalign 0.5
                    yalign 0.0
                    action page_name_value.Toggle()
                    input style "page_label_text" value page_name_value
                grid gui.file_slot_cols gui.file_slot_rows:
                    style_prefix "slot"
                    xalign 0.5
                    yalign 0.2
                    spacing gui.slot_spacing
                    for i in range(gui.file_slot_cols * gui.file_slot_rows):
                        $ slot = i + 1
                        button:
                            action FileAction(slot)
                            vbox:
                                add FileScreenshot(slot) xalign 0.5
                                text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")) style "slot_time_text" color "#ffffff"
                                text FileSaveName(slot) style "slot_name_text" color "#ffffff"
                                key "save_delete" action FileDelete(slot)
                hbox:
                    style_prefix "page"
                    xalign 0.5
                    yalign 0.72
                    spacing gui.page_spacing
                    imagebutton idle "gui/arrowleft.png" hover "gui/arrowleft.png" action FilePagePrevious() ypos 0.1
                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto") text_idle_color "#ffffff" text_hover_color "#2cabf5" text_selected_color "#AAAAAA"
                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick") text_idle_color "#ffffff" text_hover_color "#2cabf5" text_selected_color "#AAAAAA"
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page) text_idle_color "#ffffff" text_hover_color "#2cabf5" text_selected_color "#AAAAAA"
                    imagebutton idle "gui/arrowright.png" hover "gui/arrowright.png" action FilePageNext() ypos 0.1
init -501:
    screen pause_file_slots(title):
        default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Auto saves"), quick=_("Quick saves"))
        add "gui/nvl.png"
        fixed:
            order_reverse True
            button:
                style "page_label"
                key_events True
                xalign 0.5
                yalign 0.0
                action page_name_value.Toggle()
                input style "page_label_text" value page_name_value
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.2
                spacing gui.slot_spacing
                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        vbox:
                            add FileScreenshot(slot) xalign 0.5
                            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")) style "slot_time_text"
                            text FileSaveName(slot) style "slot_name_text"
                            key "save_delete" action FileDelete(slot)
            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 0.75
                spacing gui.page_spacing
                imagebutton idle "gui/arrowleft.png" hover "gui/arrowleft.png" action FilePagePrevious()
                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto") text_idle_color "#ffffff" text_hover_color "#2cabf5" text_selected_color "#AAAAAA"
                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick") text_idle_color "#ffffff" text_hover_color "#2cabf5" text_selected_color "#AAAAAA"
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)
                imagebutton idle "gui/arrowright.png" hover "gui/arrowright.png" action FilePageNext()
init -1 style page_label is gui_label
init -1 style page_label_text is gui_label_text
init -1 style page_button is gui_button
init -1 style page_button_text is gui_button_text
init -1 style slot_button is gui_button
init -1 style slot_button_text is gui_button_text
init -1 style slot_time_text is slot_button_text
init -1 style slot_name_text is slot_button_text
init -1 style page_label ypadding 5 xpadding 75
init -1:
    style page_label_text:
        hover_color gui.hover_color
        layout "subtitle"
        text_align 0.5
init -1 style page_button properties gui.button_properties("page_button")
init -1 style page_button_text properties gui.button_text_properties("page_button")
init -1 style slot_button properties gui.button_properties("slot_button")
init -1 style slot_button_text properties gui.button_text_properties("slot_button")
init -501:
    screen preferences():
        tag menu

        use game_menu(_("Preferences"), scroll="viewport"):
            vbox:
                hbox:
                    box_wrap True
                    if renpy.variant("pc") or renpy.variant("web"):
                        vbox:
                            style_prefix "radio"
                            label _("Display")
                            textbutton _("Window") action Preference("display", "window")
                            textbutton _("Fullscreen") action Preference("display", "fullscreen")
                null height (4 * gui.pref_spacing)
                vbox:
                    style_prefix "slider"
                    box_wrap True
                    vbox:
                        if config.has_sound:
                            label _("{color=#ffffff}Scene Volume{/color}")
                            vbox:
                                bar value Preference("music volume")
                            label _("{color=#ffffff}UI Volume{/color}")
                            vbox:
                                bar value Preference("sound volume")
init -501:
    screen pause_prefs():
        style_prefix "alt_menu"
        tag menu

        add "gui/nvl.png"
        vbox:
            xalign 0.5
            yalign 0.5
            hbox:
                box_wrap True
                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")
            null height (4 * gui.pref_spacing)
            vbox:
                style_prefix "slider"
                box_wrap True
                vbox:
                    if config.has_sound:
                        label _("Scene Volume")
                        vbox:
                            bar value Preference("music volume")
                        label _("UI Volume")
                        vbox:
                            bar value Preference("sound volume")
                        textbutton _("Return") action Return()
init -1 style pref_label is gui_label
init -1 style pref_label_text is gui_label_text
init -1 style pref_vbox is vbox
init -1 style radio_label is pref_label
init -1 style radio_label_text is pref_label_text
init -1 style radio_button is gui_button
init -1 style radio_button_text is gui_button_text
init -1 style radio_vbox is pref_vbox
init -1 style check_label is pref_label
init -1 style check_label_text is pref_label_text
init -1 style check_button is gui_button
init -1 style check_button_text is gui_button_text
init -1 style check_vbox is pref_vbox
init -1 style slider_label is pref_label
init -1 style slider_label_text is pref_label_text
init -1 style slider_slider is gui_slider
init -1 style slider_button is gui_button
init -1 style slider_button_text is gui_button_text
init -1 style slider_pref_vbox is pref_vbox
init -1 style mute_all_button is check_button
init -1 style mute_all_button_text is check_button_text
init -1 style pref_label bottom_margin 3 top_margin gui.pref_spacing
init -1 style pref_label_text color "#ffffff" yalign 1.0
init -1 style pref_vbox xsize 338
init -1 style radio_vbox spacing gui.pref_button_spacing
init -1 style radio_button foreground "gui/button/radio_[prefix_]foreground.png" properties gui.button_properties("radio_button")
init -1:
    style radio_button_text:
        idle_color "#ffffff"
        hover_color "#2cabf5"
        properties gui.button_text_properties("radio_button")
        selected_color "#AAAAAA"
init -1 style check_vbox spacing gui.pref_button_spacing
init -1 style check_button foreground "gui/button/check_[prefix_]foreground.png" properties gui.button_properties("check_button")
init -1 style check_button_text properties gui.button_text_properties("check_button")
init -1 style slider_slider xsize 525
init -1:
    style slider_button:
        properties gui.button_properties("slider_button")
        yalign 0.5
        left_margin 15
init -1:
    style slider_button_text:
        idle_color "#ffffff"
        hover_color "#2cabf5"
        properties gui.button_text_properties("slider_button")
        selected_color "#AAAAAA"
init -1 style slider_vbox xsize 675
init -501:
    screen help():
        tag menu

        default device = "keyboard"
        use game_menu(_("Help"), scroll="viewport"):
            style_prefix "help"
            vbox:
                spacing 23
                hbox:
                    textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                    textbutton _("Mouse") action SetScreenVariable("device", "mouse")
                    if GamepadExists():
                        textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")
                if device == "keyboard":
                    use keyboard_help
                elif device == "mouse":
                    use mouse_help
                elif device == "gamepad":
                    use gamepad_help
init -501:
    screen keyboard_help():
        hbox:
            label _("Enter")
            text _("Advances dialogue and activates the interface.")
        hbox:
            label _("Space")
            text _("Advances dialogue without selecting choices.")
        hbox:
            label _("Arrow Keys")
            text _("Navigate the interface.")
        hbox:
            label _("Escape")
            text _("Accesses the game menu.")
        hbox:
            label _("Ctrl")
            text _("Skips dialogue while held down.")
        hbox:
            label _("Tab")
            text _("Toggles dialogue skipping.")
        hbox:
            label _("Page Up")
            text _("Rolls back to earlier dialogue.")
        hbox:
            label _("Page Down")
            text _("Rolls forward to later dialogue.")
        hbox:
            label "H"
            text _("Hides the user interface.")
        hbox:
            label "S"
            text _("Takes a screenshot.")
        hbox:
            label "V"
            text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")
init -501:
    screen mouse_help():
        hbox:
            label _("Left Click")
            text _("Advances dialogue and activates the interface.")
        hbox:
            label _("Middle Click")
            text _("Hides the user interface.")
        hbox:
            label _("Right Click")
            text _("Accesses the game menu.")
        hbox:
            label _("Mouse Wheel Up\nClick Rollback Side")
            text _("Rolls back to earlier dialogue.")
        hbox:
            label _("Mouse Wheel Down")
            text _("Rolls forward to later dialogue.")
init -501:
    screen gamepad_help():
        hbox:
            label _("Right Trigger\nA/Bottom Button")
            text _("Advances dialogue and activates the interface.")
        hbox:
            label _("Left Trigger\nLeft Shoulder")
            text _("Rolls back to earlier dialogue.")
        hbox:
            label _("Right Shoulder")
            text _("Rolls forward to later dialogue.")
        hbox:
            label _("D-Pad, Sticks")
            text _("Navigate the interface.")
        hbox:
            label _("Start, Guide")
            text _("Accesses the game menu.")
        hbox:
            label _("Y/Top Button")
            text _("Hides the user interface.")
        textbutton _("Calibrate") action GamepadCalibrate()
init -1 style help_button is gui_button
init -1 style help_button_text is gui_button_text
init -1 style help_label is gui_label
init -1 style help_label_text is gui_label_text
init -1 style help_text is gui_text
init -1 style help_button properties gui.button_properties("help_button") xmargin 12
init -1 style help_button_text properties gui.button_text_properties("help_button")
init -1 style help_label right_padding 30 xsize 375
init -1:
    style help_label_text:
        xalign 1.0
        text_align 1.0
        size gui.text_size
init -501:
    screen confirm(message, yes_action, no_action):
        modal True
        zorder 200
        style_prefix "confirm"

        add "gui/overlay/confirm.png"
        frame:
            vbox:
                xalign .5
                yalign .5
                spacing 45
                label _(message) style "confirm_prompt" xalign 0.5
                hbox:
                    xalign 0.5
                    spacing 150
                    textbutton _("Sure") action yes_action
                    textbutton _("Sorry, I'll keep playing.") action no_action
        key "game_menu" action no_action
init -1 style confirm_frame is gui_frame
init -1 style confirm_prompt is gui_prompt
init -1 style confirm_prompt_text is gui_prompt_text
init -1 style confirm_button is gui_medium_button
init -1 style confirm_button_text is gui_medium_button_text
init -1:
    style confirm_frame:
        padding gui.confirm_frame_borders.padding
        xalign .5
        yalign .5
        background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
init -1 style confirm_prompt_text layout "subtitle" text_align 0.5
init -1 style confirm_button properties gui.button_properties("confirm_button")
init -1 style confirm_button_text properties gui.button_text_properties("confirm_button")
init -501:
    screen skip_indicator():
        zorder 100
        style_prefix "skip"

        frame:
            hbox:
                spacing 9
                text _("Skipping")
                text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
                text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
                text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"
transform delayed_blink(delay, cycle):
    alpha .5
    pause delay
    linear .2 alpha 1.0
    pause .2
    linear .2 alpha 0.5
    pause (cycle - .4)
    repeat
init -1 style skip_frame is empty
init -1 style skip_text is gui_text
init -1 style skip_triangle is skip_text
init -1:
    style skip_frame:
        padding gui.skip_frame_borders.padding
        ypos gui.skip_ypos
        background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
init -1 style skip_text size gui.notify_text_size
init -1 style skip_triangle font "DejaVuSans.ttf"
init -501:
    screen notify(message):
        zorder 100
        style_prefix "notify"

        frame:
            at notify_appear
            text "[message!tq]"
        timer 3.25 action Hide('notify')
transform notify_appear:
    on hide:
        linear .5 alpha 0.0
    on show:
        alpha 0
        linear .25 alpha 1.0
init -1 style notify_frame is empty
init -1 style notify_text is gui_text
init -1:
    style notify_frame:
        padding gui.notify_frame_borders.padding
        ypos gui.notify_ypos
        background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
init -1 style notify_text properties gui.text_properties("notify")
init -501:
    screen nvl(dialogue, items=None):
        window:
            style "nvl_window"
            vbox:
                spacing gui.nvl_spacing
                if gui.nvl_height:
                    vpgrid:
                        cols 1
                        yinitial 1.0
                        use nvl_dialogue(dialogue)
                else:
                    use nvl_dialogue(dialogue)
                for i in items:
                    textbutton i.caption action i.action style "nvl_button"
        add SideImage() xalign 0.0 yalign 1.0
init -501:
    screen nvl_dialogue(dialogue):
        for d in dialogue:
            window:
                id d.window_id
                fixed:
                    yfit gui.nvl_height is None
                    if d.who is not None:
                        text d.who id d.who_id
                    text d.what id d.what_id
define config.nvl_list_length = gui.nvl_list_length
init -1 style nvl_window is default
init -1 style nvl_entry is default
init -1 style nvl_label is say_label
init -1 style nvl_dialogue is say_dialogue
init -1 style nvl_button is button
init -1 style nvl_button_text is button_text
init -1:
    style nvl_window:
        padding gui.nvl_borders.padding
        yfill True
        background "gui/nvl.png"
        xfill True
init -1 style nvl_entry ysize gui.nvl_height xfill True
init -1:
    style nvl_label:
        yanchor 0.0
        xpos gui.nvl_name_xpos
        xanchor gui.nvl_name_xalign
        ypos gui.nvl_name_ypos
        text_align gui.nvl_name_xalign
        xsize gui.nvl_name_width
        min_width gui.nvl_name_width
init -1:
    style nvl_dialogue:
        xpos gui.nvl_text_xpos
        xanchor gui.nvl_text_xalign
        ypos gui.nvl_text_ypos
        text_align gui.nvl_text_xalign
        xsize gui.nvl_text_width
        min_width gui.nvl_text_width
        layout ("subtitle" if gui.nvl_text_xalign else "tex")
init -1:
    style nvl_thought:
        xpos gui.nvl_thought_xpos
        xanchor gui.nvl_thought_xalign
        ypos gui.nvl_thought_ypos
        text_align gui.nvl_thought_xalign
        xsize gui.nvl_thought_width
        min_width gui.nvl_thought_width
        layout ("subtitle" if gui.nvl_text_xalign else "tex")
init -1:
    style nvl_button:
        xpos gui.nvl_button_xpos
        xanchor gui.nvl_button_xalign
        properties gui.button_properties("nvl_button")
init -1 style nvl_button_text properties gui.button_text_properties("nvl_button")
init -1 style pref_vbox xsize 675 variant "medium"
init -501:
    screen quick_menu():
        variant "touch"
        zorder 100

        if quick_menu:
            vbox:
                style_prefix "quick"
                xalign 0.5
                yalign 1.0
                textbutton _("Back") action Rollback()
                textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
                textbutton _("Auto") action Preference("auto-forward", "toggle")
                textbutton _("Menu") action ShowMenu()
init -1 style window background "gui/phone/textbox.png" variant "small"
init -1 style radio_button foreground "gui/phone/button/radio_[prefix_]foreground.png" variant "small"
init -1 style check_button foreground "gui/phone/button/check_[prefix_]foreground.png" variant "small"
init -1 style nvl_window background "gui/phone/nvl.png" variant "small"
init -1 style game_menu_navigation_frame xsize 510 variant "small"
init -1 style game_menu_content_frame top_margin 0 variant "small"
init -1 style pref_vbox xsize 600 variant "small"
init -1:
    style bar:
        left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
        ysize gui.bar_size
        right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
        variant "small"
init -1:
    style vbar:
        bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)
        top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
        xsize gui.bar_size
        variant "small"
init -1:
    style scrollbar:
        ysize gui.scrollbar_size
        base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
        thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
        variant "small"
init -1:
    style vscrollbar:
        base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        xsize gui.scrollbar_size
        thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        variant "small"
init -1:
    style slider:
        ysize gui.slider_size
        base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
        thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"
        variant "small"
init -1:
    style vslider:
        base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
        xsize gui.slider_size
        thumb "gui/phone/slider/vertical_[prefix_]thumb.png"
        variant "small"
init -1 style slider_pref_vbox xsize None variant "small"
init -1 style slider_pref_slider xsize 900 variant "small"
init python:

    import datetime

init -501:
    screen search_engine_screen():
        frame:
            xysize (1336, 751)
            align (0.5, 0.5)
            background "laptopsearch/laptopshell.png"
            add "laptopsearch/laptopscreen.png"
            imagebutton idle Solid("#00000000", xysize=(104, 20)) hover "laptopsearch/laptopsearchrollover.png" focus_mask None hovered Play("sound", "audio/MainMenuRollover.mp3") action [Play("sound", "audio/PhoneSelect.mp3"), Jump("scene_0086")] xpos 556 ypos 285
            add "laptopsearch/laptopscreenoverlay.png"
init -501:
    screen ending_tracker_screen():
        modal True

        default endings_name = {
                '0074': 'Arri (gay one)     ',
                '0082': '911              ',
                '0095': '240-830-2832    ',
                '0113': '703-924-1701    ',
                '0131': '703-299-2009    ',
                '0141': '703-913-5600    ',
                '0160': '703-503-5800    ',
            }
        default endings_details = {
                '0074': 'ur a fucking bitch',
                '0082': 'EMERGENCY SERVICE REQUEST',
                '0095': 'sorry sis',
                '0113': 'do u still wanna talk',
                '0131': 'Rossler\'s Special Offer!',
                '0141': 'now or never',
                '0160': 'r u still selling?',
            }
        default ending_text = {
                '0074': 'every time i miss u i remind myself its exclusively for the sex and i can pay for that so bitch ur not priceless... not even close ;o <3\n\n\np.s. call me 4 fwb sorry high as fuck rn',
                '0082': 'Hello this is 911 with an SMS update on your service request.\n\nThe approximate wait time for your POLICE OFFICER arrival is in 1 HOUR. Please find a safe location until your first responder arrives to assist with your ARSON HATE CRIME.\n\nThank you and have a nice day!\n\nTo no longer receive these messages reply STOP. All texts from 911 are subject to a $0.25 service charge.',
                '0095': 'Not sure if they let you have your phone in jail but I guess you\'ll see this when they let you out. since you\'re an adult now I sold all your furniture, thrifted your clothes at that the shop in Arlington, and have been renting out your room on craigslist. You can visit every now and then but you do not have a home here so find a job and your own place when you get out. recession shouldn\'t make it too hard.',
                '0113': 'i wanna let u know im not mad at you or anything and still wanna hang out. she broke up with me but that isnt why im texting i just genuinely like u not even for the sexting but bcuz i think ur a good person on the inside and want a real relationship if thats cool w you',
                '0131': 'Hi! If you\'re receiving this text it means you were selected for the Rossler\'s Kosher Deli sweepstakes! A chance to win your very own free catering at any event you would like. Events excluded from this offer are\n\nSchools\npolitical rallies\nneo-nazi gatherings\ncomic book conventions (same thing, we know)\nKKK meetings\nBook clubs discussing Mein Kampf\nand any other anti-semetic events or assembly\n\nWe hope you understand, good luck contestant!',
                '0141': 'you wont see this cuz they make us turn our phones off but i just want to write this for me. Im glad we are dying together it just feels right and i cant think of anyone i would rather do it with. I may as well write this too.. i am super fucking gay for you sorry i lied in the hallway and didnt tell u before we shared a bed and changed in front of each other. idk if thats rape or whatever but if it is sorry lol. i can die fulfilled  cuz dying together with another girl is a bigger commitment than some soft ass bitch getting married to jack the construction worker or some other boring white guy who cant pronounce Beanie Sigel. but ya if you pass out first im gonna try to fall over on you so it looks like were cuddling <3',
                '0160': 'hey my buddy craig gave me your number. are you still offering the whipped cream handjobs or is it sans whipped cream now? not sure if that was a limited time only thing like the Pizza Hut 4forAll, god that was such a convenient option because I hated when me and my golf buddies would order half onions and then the ENTIRE pizza tasted like onions. anyway i will be a very gentle and respectful client, by the way is it extra if I want you to pretend to be my daughter (who died last year)? like we talk about how your doing in social studies or something while you pound my hog to jenny McCarthy show reruns playing in the background\nbrownie points if you can cry on command xoxo',
            }
        default selected_text = ""
        default show_popup = not persistent.seen_tip
        key "K_ESCAPE" action If(selected_text, true=SetScreenVariable("selected_text", ""), false=[Play("sound", "audio/Phone_close.mp3"), Hide("ending_tracker_screen")])
        key "K_BACKSPACE" action If(selected_text, true=SetScreenVariable("selected_text", ""), false=[Play("sound", "audio/Phone_close.mp3"), Hide("ending_tracker_screen")])
        add "gui/ending_tracker/ending_tracker_pda.png" at ending_tracker_pda
        fixed:
            at ending_tracker_screen
            add "gui/ending_tracker/base_screen.png"
            text "{}/7".format(len(persistent.endings)) font "joystix monospace.ttf" size 48 color "#ffffff" outlines [ (absolute(2), "#2370be", absolute(0), absolute(0)) ] xpos 405 ypos 129
            if len(persistent.endings) == 7:
                text "1/1" font "joystix monospace.ttf" size 48 color "#ffffff" outlines [ (absolute(2), "#2370be", absolute(0), absolute(0)) ] xpos 690 ypos 129
            else:
                textbutton _("0/1") text_font "joystix monospace.ttf" text_size 48 text_color "#ffffff" text_outlines [ (absolute(2), "#2370be", absolute(0), absolute(0)) ] hovered SetScreenVariable("show_popup", True) action NullAction() padding (0, 0, 0, 0) xpos 690 ypos 129
            text datetime.datetime.now().strftime("%I:%M %p") font "joystix monospace.ttf" size 48 color "#0000cc" xpos 1240 ypos 62
            if not selected_text:
                viewport:
                    id "messages"
                    xysize (1288, 618)
                    xpos 260
                    ypos 230
                    draggable True
                    mousewheel True
                    if selected_text:
                        text ending_text[selected_text] font "texting2007.ttf" size 48 color "#000000"
                    else:
                        vbox:
                            if len(persistent.endings) == 7:
                                button:
                                    xysize (1288, 70)
                                    hover_background "gui/ending_tracker/highlight_bar.png"
                                    action Play("sound", "audio/Phone_button.mp3"), Start("scene_0999")
                                    text "UNKNOWN          VIDEO MESSAGE" font "texting2007.ttf" size 48 color "#000000" yalign 0.5 xpos 25 yoffset 5 hover_color "#ffffff"
                            for ending in persistent.endings[::-1]:
                                $ ending = ending.split("_")[1]
                                $ detail = endings_details[ending]
                                button:
                                    xysize (1288, 70)
                                    hover_background "gui/ending_tracker/highlight_bar.png"
                                    action Play("sound", "audio/Phone_button.mp3"), SetScreenVariable("selected_text", ending), SetScreenVariable("adj.value", 0.0)
                                    text "{}{}".format(endings_name[ending], detail) font "texting2007.ttf" size 48 color "#000000" yalign 0.5 xpos 25 yoffset 5 hover_color "#ffffff"
                vbar value YScrollValue("messages") xpos 1568 ypos 245 ysize 553 xsize 40 base_bar Solid("#00000000") thumb "gui/ending_tracker/texting_scrollbar.png"
            else:
                viewport:
                    id "message_detail"
                    xysize (1288, 628)
                    xpos 260
                    ypos 220
                    draggable True
                    mousewheel True
                    text ending_text[selected_text] font "texting2007.ttf" size 48 color "#000000"
                vbar value YScrollValue("message_detail") xpos 1568 ypos 245 ysize 553 xsize 40 base_bar Solid("#00000000") thumb "gui/ending_tracker/texting_scrollbar.png"
            imagebutton idle "gui/ending_tracker/texting_back.png" hover "gui/ending_tracker/texting_back.png" action If(selected_text, true=[Play("sound", "audio/Phone_button.mp3"), SetScreenVariable("selected_text", "")], false=[Play("sound", "audio/Phone_close.mp3"), Hide("ending_tracker_screen")]) xpos 264 ypos 907
            add "gui/ending_tracker/screen_overlay.png"
            add "gui/ending_tracker/faceplate.png"
            if show_popup:
                button:
                    xysize (447, 380)
                    background "gui/ending_tracker/confirm_bubble.png"
                    action NullAction()
                    xpos 850
                    ypos 115
                    textbutton _("OK FUCK OFF") text_font "LeagueGothic-Regular.otf" text_size 37 text_idle_color "#ff7cc0" text_hover_color "#ffffff" action SetScreenVariable("show_popup", False), SetField(persistent, "seen_tip", True) xpos 300 ypos 308
transform ending_tracker_screen:
    alpha 0.0
    pause 0.3
    alpha 1.0
transform ending_tracker_pda:
    subpixel True
    xalign 0.915 yalign 0.835 zoom 0.112 alpha 0.0
    on hide:
        parallel:
            linear 0.1 alpha 1.0
            pause 0.3
            linear 0.1 alpha 0.0
            linear 0.3:
                zoom 0.112 xalign 0.915 yalign 0.835
    on show:
        parallel:
            linear 0.1 alpha 1.0
            pause 0.1
            pause 0.1
            linear 0.2:
                zoom 1.7 xalign .45 yalign 0.55
return
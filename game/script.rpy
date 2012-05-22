﻿# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image wikipe normal = '317px-Wikipe-tan_full_length.png'
image wikipe meditating = '412px-Wikipe-tan_meditating.png'
image wikipe sign = '326px-Wikipe-tan_holding_sign.png'
image wikipe library = '452px-Kasuga_s_Wikipedia_Submission_by_cult50contests.jpg'

# Declare characters used by this game.
define w = Character('Wikipe-tan', color="#c8ffc8")

# The game starts here.
label start:
    show wikipe normal
    $ firstTime = {'copyleft': True}

    w "Oh, hi there!"
    $ project = renpy.input("I heard you're planning on open-sourcing your new project, uh, what was it called again?") or "the mystery project"
    if project == 'the mystery project':
        w "Uh, I can keep secrets, but that's ok..."
    else:
        w "Right, [project]."
    w "Well, let me just ask you a few questions, and then I'll give you some suggestions, alright?"
    jump copyleft
    
label copyleft:
    python:
        if firstTime['copyleft']:
            firstTime['copyleft'] = False
            question = "First off, do you want a copyleft license for %s?" % project
        else:
            question = "So, how about copyleft?"
    menu:
        w "[question]"
        "Yes":
            w "Yessir, Mr. Stallman!"
            $ copyleft = True
        "No":
            w "Not an ideologue, huh?"
            $ copyleft = False
        "What's copyleft?":
            # TODO
            w "Well..."
            jump copyleft

    
    return


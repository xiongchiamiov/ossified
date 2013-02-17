# You can place the script of your game in this file.

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
    $ visited = {}

    w "Oh, hi there!"
    $ project = renpy.input("I heard you're planning on open-sourcing your new project, uh, what was it called again?") or "the mystery project"
    if project == 'the mystery project':
        w "Uh, I can keep secrets, but that's ok..."
    else:
        w "Right, [project]."
    w "Well, let me just ask you a few questions, and then I'll give you some
       suggestions, alright?"
    jump copyleft
    
label copyleft:
    python:
        if visited.get('copyleft'):
            question = "So, how about copyleft?"
        else:
            visited['copyleft'] = True
            question = "First off, do you want a copyleft license for %s?" % project
    menu:
        w "[question]"
        "Yes":
            w "Yessir, Mr. Stallman!"
            jump gpl
        "No":
            w "Not an ideologue, huh?"
        "What's copyleft?":
            w "Copyleft is a play on the word copyright."
            w "Essentially, anyone could modify or redestribute [project], but
               they have to allow you to do the same thing with their
               modifications."
            w "So, if they add some really cool feature, they have to give it
               back to you so you can use it too!"
            w "Keep in mind that various copyleft licenses may have additional
               restrictions, such as being non-profit or requiring a note
               saying that you are the original author.  We'll get to those
               details later."
            jump copyleft
    
    jump stateChanges

label gpl:
    menu:
        w "Is this a web site or web application?"
        "Yes":
            $ license = 'AGPL'
        "No":
            menu:
                w "Is it a library, then?"
                "Yes":
                    $ license = 'LGPL'
                "No":
                    $ license = 'GPL'
    jump decision

label stateChanges:
    if not visited.get('stateChanges'):
        w "Sometimes building off a project leads to some pretty heavy
           modification; think about how different Counter-Strike is from
           Half-Life!"
        w "These changes can be good or bad, and sometimes people judge the
           source project by the derivative."
        $ visited['stateChanges'] = True
    menu:
        w "Should child projects of [project] be required to clearly list which
           things are original, and which are new?"
        "Sure, that sounds like a good idea.":
            w "You've got a reputation to protect!"
            $ license = 'Apache License'
            jump decision
        "Who cares?  Maybe they'll make something better than I did.":
            w "Now that's the spirit of optimism I like!"
    jump attribution

label attribution:
    menu:
        w "Do you want any project building off of [project] to provide notice
           somewhere where the code came from?"
        "Yeah, I'd like some recognition.":
            w "It's the least they can do, right?"
        "Nah, it's cool.":
            w "Aww, you're so selfless!"
            w "..."
            w "Are you single?"
            w "I'm sorry, I shouldn't have asked that.  Where were we?  Ah,
               that's right - you don't care about fame."
            $ license = 'WTFPL'
            jump decision
    jump advertising

label advertising:
    if not visited.get('advertising'):
        w "Something that doesn't occur often to programmers is that they may
           or may not want to be associated with someone else's project that
           uses their work."
        $ visited['advertising'] = True
    menu:
        w "If someone uses parts of [project], what would you like them to do?"
        "Change the name of the project.":
            w "Yeah, it can be kinda confusing when people don't know which
               [project] is the real one..."
            $ license = 'Zlib License'
        "Just don't mention me.":
            w "Who knows what evil things someone could do with [project]?
               Don't tie yourself to an unknown future, I always say."
            $ license = 'BSD 3-Clause License'
        "Eh, whatever.  Use the name, use my name - I trust them.":
            w "I always thought Locke was better than Hobbes."
            $ license = 'MIT License'
    jump decision

label decision:
    w "Alright, I think I know what you want - the [license]!"
    return

# vim: expandtab shiftwidth=4 softtabstop=4

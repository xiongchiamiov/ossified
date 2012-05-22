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

    w "Oh, hi there!"
    
    show wikipe meditating
    
    w ''
    
    show wikipe sign
    
    w ''
    
    show wikipe library

    w ''
    
    return


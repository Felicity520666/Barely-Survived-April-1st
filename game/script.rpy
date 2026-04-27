define t = Character("Theo", color = "#ffa500")
define m = Character("Mom", color = "#b73176")
define j = Character("Jack", color = "#ffd621")

label start:
    play music "snoring-71560.mp3" fadein 1.0 volume 3.6
    pause 3.5
    scene wake with fade
    stop music fadeout 1.0
    play music "sweet-acoustic-guitar-music-311691.mp3" fadein 1.5
    play sound "yawning-6096.mp3"
    pause 3.5
    t "Huh... Can't believe it's already time to wake up. I'm so tired~"
    t "Ah, but I have to get ready for school... Can't be late again."
    scene tooth with fade
    play sound "freesound_community-bathroom-sink_1-94625.mp3"
    pause 3.0
    scene put with irisin
    pause 1.5
    scene finish with dissolve
    play sound "ding.mp3" volume 3.5
    pause 1.5
    scene brush with pushright
    pause 2.0
    scene wosh with vpunch
    play sound "fire.mp3"
    pause 4
    scene ouch with vpunch
    play sound "ground.mp3" volume 4.5
    t "Augh! What the...? Why is my toothpaste burning?! Did someone add chili powder to it?!"
    scene mom with slideleft
    play sound "fool.mp3" volume 3.5
    pause 4.0
    t "Holy cow! Mom?! I can't believe it's YOU!"
    m "Come on, Theo! It's April Fools' Day! How can I miss the chance to prank you?!"
    t "Augh! Grow up, Mom!"
    m "Now get ready for school, kiddo! You don't want to be late."
    t "Fine..."
    stop music fadeout 1.0
    scene 2r with hpunch
    play sound "myinstants.mp3" volume 2.5
    pause 1.0
    scene 2 with dissolve
    pause 1.0
    scene hour with irisin
    play sound "later copy.mp3" volume 4.0
    pause 4.0
    play music "the_mountain-school-130448.mp3" fadein 1.0
    scene route with slideleft
    play sound "footsteps-dirt-gravel-6823.mp3" volume 13.5
    pause 1.0
    t "Ugh, so many pranks..."
    scene school with pushleft
    play sound "freesound_community-school-104993.mp3" volume 3.5
    t "Well, at least I'm not late for school."
    play sound "tt.mp3" volume 2.5
    show jack worry at smallleft with moveinright
    j "Theo!"
    show theo confused at smallright with moveinleft
    play sound "mrstokes302-huh-sfx-418238.mp3" volume 5.5
    t "Huh?"
    t "What's up, Jack? Why... why do you look so sad?"
    play music "solarflex-sad-dramatic-music-3-491493.mp3" fadein 1.5
    j "Theo... I have really bad news..."
    show theo sad at smallright with dissolve
    t "What is it, Jack? Is it about my grade? Oh no! It's not about that science test, is it?!"
    play sound ""
    j ""
    j ""


    

    return

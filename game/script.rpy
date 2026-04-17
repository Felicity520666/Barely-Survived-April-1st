define t = Character("Theo", color = "#ffa500")

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
    play sound "fire.mp3"
    pause 4
    

    return

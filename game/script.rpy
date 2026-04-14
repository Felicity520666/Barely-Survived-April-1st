define t = Character("Theo", color = "#ffa500")

label start:
    play music "audio/snoring-71560.mp3" fadein 1.0
    pause 3.5
    scene wake with fade
    stop music fadeout 1.0
    play music "audio/sweet-acoustic-guitar-music-311691.mp3" fadein 1.5
    play sound "audio/yawning-6096.mp3"
    pause 3.5
    t "Huh... Can't believe it's already time to wake up. I'm so tired~"

    return

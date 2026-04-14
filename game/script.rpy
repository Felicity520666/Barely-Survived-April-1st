define t = Character("Theo", color = "#ffa500")

label start:
    play music "snoring-71560.mp3" fadein 1.0
    pause 3.5
    scene wake with fade
    stop music fadeout 1.0
    play music "sweet-acoustic-guitar-music-311691.mp3" fadein 1.5
    play sound "yawning-6096.mp3"
    pause 2.5

    return

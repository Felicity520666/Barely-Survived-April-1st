define t = Character("Theo", color = "#ffa500")
define m = Character("Mom", color = "#b73176")
define j = Character("Jack", color = "#ffd621")
define b = Character("Ms.Brown", color = "#00883b")

transform smallleft:
    zoom 0.5
    xalign 0.0
    yalign 1.0

transform smallright:
    zoom 0.5
    xalign 1.1
    yalign 1.0

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
    play sound "sah.mp3" volume 4.5
    j "Ah... I wish it was just about that... But look, don't freak out, okay? Just listen to me..."
    t "Jack? You are making me really nervous... Just tell me already!"
    j "Here it goes then... Out English teacher, Ms. Brown, is..."
    t "Is what? Shecdualing a pop quiz today?"
    j "Oh no, it's not that... She's... gone..."
    scene uuu with vpunch
    play sound "way.mp3" volume 5.0
    t "Gone? You mean... she's dead...?"
    play music "old.mp3" fadein 0.9
    t "No... no! This can't be real! THis can't be hapening!"
    t "Even though I always said I hated English class, even though I argued with Ms. Brown more times than I can count...."
    play sound "freesound_community-clear-throat-85636.mp3" volume 3.0
    $ renpy.music.set_pause(True, channel = "music")
    j "Ahem, sorry to interrupt, but 12 times to be exact, you're welcome."
    t "Oh I didn't realize that many... Anyway..."
    $ renpy.music.set_pause(False, channel = "music")
    t "Deep down, I respected Ms. Brown so much.. I just... never showed it..."
    t "If I had known this day would come so fast, I swear I would never have been so mean. I would have raised my hand for evry question. I would have written every essay with my whole heart. I would have been quiet in every single class, listening to every word she said as if it were the most important lesson of my life."
    t "Oh... Ms. Brown... how could you leave us like this? You were not just an English teacher, you were a chapter in my life that I didn't know I would miss so much!"
    t "From thisn dat forward, English will be my favorite subject!"
    play sound "sad.mp3" volume 3.5
    t "Rest in peace, Ms. Brown..."
    stop music fadeout 1.0
    play sound "haha.mp3" volume 3.5
    pause 2.0
    play sound "mrstokes302-huh-sfx-418238.mp3" volume 3.5
    t "Huh?"
    t "Why are people laughing?"
    t "Wait..."
    play music "cartoon-funny-462261.mp3" 
    scene school with vpunch
    show jack smile at smallleft with moveinright
    play sound "freesound_community-clear-throat-85636.mp3" volume 3.0
    j "Ahem... Theo! That was a great speech you just gave... in front of the whole school!"
    j "Your English teacher must be sooo pround!"
    show theo sad at smallright with moveinright
    t "Jack, you... you were recording me the whole time?"
    show theo embarrassed at smallright with dissolve
    show jack laugh at smallleft with dissolve
    play sound "af.mp3" volume 9.0
    j "Hahahaha!!! April Fools!!!"
    scene 1r with hpunch
    play sound "myinstants.mp3" volume 2.5
    pause 1.0
    scene 1 with dissolve
    pause 1.0
    play music "friends.mp3" fadein 1.5
    scene empty with blinds
    show theo shy at smallright with moveinright
    t "Ah... That was sooooo embarrassing... Jack is such a jerk!"
    show theo think at smallright with dissolve
    t "Ohhoho, wait, Jack isn't here yet!"
    t "it's April Fools' right? No one is gonna blame me for having something exciting..."
    t "Just you wait Jack!"
    scene pin with dissolve
    play sound "lol.mp3" volume 3.5
    t "Hum, Jack, I'll let you have a memerable April Fools'!"
    t "I even put 520 glue so the pin stucks to the chair. Mauhahahahaha!"
    scene teacher with pixellate
    b "Okay, class! BEfore the class starts, I want to say, I know today is April Fools' Day, but I don't want any of you to pull ANY pranks in class."
    scene teacher mad with dissolve
    b "If I catch anyone pranking others, I will take off 10 points from your test grade!"
    show theo shy at smallright with dissolve
    t "Oh no... Oh no no no no no! If Jack sits on that chair he's gonna let Ms. Brown know that I pranked him!"
    t "I can't spiritually survive losing another 10 ponits from my alreadt tragic grade!"
    show theo sad at smallright with dissolve
    t "There's only one way..."
    scene talk with pushright
    play sound "u_xg7ssi08yr-cartoon-phone-babble-404405.mp3" 
    pause 2.5
    scene teacher mad with dissolve
    b "Theo! Why are you sitting beside Leon? You two keep talking! You'll distracte the whole class!"
    b "Jack's not here yet, why don't you take his seat and sut beside class monitor Lucy? She'll make sure to keep you quiet!"
    t "Yes, ma'am!"
    play sound "no-96018.mp3" volume 3.6
    t "{i}Nooooo, this is truly double damage! I have to sit on nails while pretending all's normal, and survuve an entire class sitting next to the Great Witch Lucy...{/i}"
    scene bell with squares
    play music "emg5991-school-bell-310293.mp3" 
    pause 3.5
    scene teacher with fade
    b "Okay, class is starting, move into your seats!"
    show theo sad at smallleft with moveinleft
    t "Here it goes..."
    hide theo sad with moveoutright
    scene 0r with hpunch
    play sound "myinstants.mp3" volume 2.5
    pause 1.0
    scene 0 with dissolve
    pause 1.0

    return



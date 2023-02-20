# The script of the game goes in this file.

##pick between one of the two and add an # to the other to keep it

##regular taps, medium intervals
#define sounds = ['audio/A1.ogg', 'audio/A2.ogg', 'audio/A3.ogg', 'audio/A4.ogg', 'audio/A5.ogg']

##light taps, smaller intervals
#define sounds = ['audio/B1.ogg', 'audio/B2.ogg', 'audio/B3.ogg', 'audio/B4.ogg', 'audio/B5.ogg']


##both combined
define sounds = ['audio/A1.ogg', 'audio/A2.ogg', 'audio/A3.ogg', 'audio/A4.ogg', 'audio/A5.ogg', 'audio/B1.ogg', 'audio/B2.ogg', 'audio/B3.ogg', 'audio/B4.ogg', 'audio/B5.ogg']



init python:
    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            renpy.sound.play(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            #dumb way to do it but it works, dunno if it causes memory leaks but it's almost 6AM :v



        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen")
# Characters

define Lydia = Character("Lydia",callback=type_sound)
define Moon = Character("Moon", callback=type_sound)
define Raphael = Character("Raphael", callback=type_sound)
define Kiky = Character("Kiky", callback=type_sound)
define Jerry = Character("Jerry", callback=type_sound)

# Misc

define Guru = Character("Ms. Dely", callback=type_sound)
define Narrator = Character("Narrator")
define Mama = Character("Mrs. Lily", callback=type_sound)
define UnknownKiky = Character("?", callback=type_sound)

# Declaring Background Images

image bg bus = ("bg_bus.png")
image bg kamarlydia = ("kamarlydia.png")
image bg kantorguru = ("kantorsekolah.png")
image bg kamarlydiamalam = ("kamarlydiamalam.png")
image bg dapur = ("dapurpagi.png")
image bg dapurmalam = ("dapurmalam.png")
image bg livingroommalam = ("livingroommalam.png")
image bg livingroom = ("livingroompagi.png")
image bg kantinpagi = ("kantinpagi.png")
image bg kantinmalam = ("kantinmalam.png")
image bg gerbangdepan = ("gerbangdepan.png")
image bg lorongsekolah = ("lorongpagi.png")
image bg kelas = ("kelas.png")

# Kiky Emotes

#image define kiky happy = ("kiky happy.png")
image define kiky senyum = ("kiky biasa.png")
image define kiky bingung = ("kiky bingung.png")
image define kiky marah = ("kiky marah.png")
image define kiky sedih = ("kiky sedih.png")

# Bu Lily (Ibu Lydia) Emotes

image define mama senyum = ("mama senyum.png")
image define mama bingung = ("mama bingung.png")
image define mama marah = ("mama marah.png")
image define mama sedih = ("mama sedih.png")

# Lydia School Emotes

image define lydia senyum = ("lydia senyum.png")
image define lydia bingung = ("lydia bingung.png")
image define lydia marah = ("lydia marah.png")
image define lydia sedih = ("lydia sedih.png")

# Lydia Baju Putih

image lydia2senyum = ("lydia senyum putih.png")
image lydia2bingung = ("lydia bingung putih.png")
image lydia2marah = ("lydia marah putih.png")
image lydia2sedih = ("lydia sedih putih.png")

# Lydia Baju Hitam

image lydia3senyum = ("lydia senyum hitam.png")
image lydia3bingung = ("lydia bingung hitam.png")
image lydia3marah = ("lydia marah hitam.png")
image lydia3sedih = ("lydia sedih hitam.png")

# Moon Emotes

image define moon senyum = ("moon senyum.png")
image define moon bingung = ("moon bingung.png")
image define moon marah = ("moon marah.png")
image define moon sedih = ("moon sedih.png")

# Ms Dely Emotes

image define dely senyum = ("dely senyum.png")
image define dely biasa = ("dely biasa.png")
image define dely marah = ("dely marah.png")
image define dely sedih = ("dely sedih.png")

# Jerry Images

image define jerry senyum = ("jerry senyum.png")
image define jerry biasa = ("jerry biasa.png")
image define jerry marah = ("jerry marah.png")
image define jerry sedih = ("jerry sedih.png")

# Raphael Emotes

image define raphael senyum = ("raphael senyum.png")
image define raphael biasa = ("raphael biasa.png")
image define raphael marah = ("raphael marah.png")
image define raphael sedih = ("raphael sedih.png")

# Audios

define musicintro = ("audio/ost_intro.mp3")

label start:

    play sound "audio/next_dialogue.ogg"
    centered "{color=#c842f5}Chapter 1{/color}{color=#ffffff}\nThe Beginning{/color}"
    play sound "audio/next_dialogue.ogg"
    centered "{color=#ffffff}This story is about a girl, {/color}{color=#c842f5}Lydia{/color}{color=#ffffff}, as it's her first day of going to school...{/color}"
    play sound "audio/next_dialogue.ogg"
    centered "{color=#ffffff}And it's also her {/color}{color=#c842f5}first time {/color}{color=#ffffff}to go to the school, would it be okay for her?{/color}"
    play sound "audio/next_dialogue.ogg"

    scene black with dissolve

    scene bg kamarlydia
    play music "audio/intro_ost.mp3" volume 1 fadeout 0.5

    show lydia2sedih:
        yalign 0.505
        xalign 0.5
    
    Lydia "Hmmm what should I do.."

    window hide

    label sfx_telepon1:
        scene black with dissolve
        play audio "audio/lydia_phone_ringtone.wav"
        centered "{color=#ffffff}Suddenly Lydia's phone ringing...{/color}"
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}Lydia picked up the call.{/color}"
    
    label percakapan_telepon1a:
        scene bg kantorguru
        show dely senyum:
            yalign 0.505
            xalign 0.5
        Guru "(On the call) Lydia, tomorrow is your first day of school, right?"
        jump percakapan_telepon1b
    
    label percakapan_telepon1b:
        scene bg kamarlydia
        show lydia2bingung:
            yalign 0.505
            xalign 0.5
        Lydia "Yes Miss, If you don't mind me asking, is there any specific things that I should bring?"
        jump percakapan_telepon1c

    label percakapan_telepon1c:
        scene bg kantorguru
        show dely biasa:
            yalign 0.505
            xalign 0.5
        Guru "No, just bring the things that you usually bring to school."
        jump percakapan_telepon1d

    label percakapan_telepon1d:
        scene bg kamarlydia
        show lydia2senyum:
            yalign 0.505
            xalign 0.5
        Lydia "Okay, thank you miss."
        jump percakapan_telepon1e

    label percakapan_telepon1e:
        scene bg kantorguru
        show dely biasa:
            yalign 0.505
            xalign 0.5
        Guru "Don't mention it. (hangs up)"
        jump action_1f

    label action_1f:
        play audio "audio/end_call.wav"
        hide dely with dissolve
        jump lydia_ngomongsendiri1f

    label lydia_ngomongsendiri1f:
        scene bg kamarlydia
        show lydia2sedih:
            yalign 0.505
            xalign 0.5
        Lydia "Huh, finally I’m back to school, but, I haven’t prepared for anything yet."
        Lydia "Will there be anyone that want to be friend with me??"
        Lydia "Will I be able to catch up with the subjects?"
        jump ibumasuk1g

    label ibumasuk1g:
        play sound "audio/door_open.wav"
        scene black with dissolve
        centered "{color=#ffffff}Suddenly, Lydia's mom enters Lydia's room..{/color}"
        jump ibudalamruangan1h
    
    label ibudalamruangan1h:
        scene bg kamarlydia
        show mama marah:
            yalign 0.505
            xalign 0.5
        Mama "LYDIAA!! YOUR ROOM IS LOOKING LIKE A LIVING HELL AND YOU’RE STILL MUMBLING THOSE SHITS?"
        jump jawabanlydia1i
    
    label jawabanlydia1i:
        scene bg kamarlydia
        show lydia2sedih:
            yalign 0.505
            xalign 0.5
        Lydia "Mom... don’t get mad, you’ll get old quickly."
        jump pertanyaanpertama1j

    label pertanyaanpertama1j:
        scene bg kamarlydia
        show mama marah:
            yalign 0.505
            xalign 0.5
        Mama "Too many excuses. Clean your room now. I’ve cooked your favorite fried rice downstairs."
    menu:
        extend "" # Agar muncul dialog dibawah option
    
        "Accept": # [+]
            jump jawaban_positif1h
        "Reject": # [-]
            jump jawaban_negatif1h

    # NO ------------

    label jawaban_negatif1h:
        scene bg kamarlydia
        show lydia2sedih:
            yalign 0.505
            xalign 0.5
        Lydia "Ugh, I'll do it later Mom.. I feel so exhausted today.."
        jump jawaban_lanjutannegatif1ha

    label jawaban_lanjutannegatif1ha:
        scene bg kamarlydia
        show mama marah:
            yalign 0.505
            xalign 0.5
        Mama "No more excuses. even though you're tired, you still have to eat."
        Mama "You're just chewing, does that make you tired?"
        jump jawaban_lanjutannegatif1hb

    label jawaban_lanjutannegatif1hb:
        scene bg kamarlydia
        show lydia2sedih:
            yalign 0.505
            xalign 0.5
        Lydia "Alright momm..."
        jump lydiamenghilang2a

    # NO ------ ^^^^^^^^^^

    # YES --------------------

    label jawaban_positif1h:
        scene bg kamarlydia
        show lydia2senyum:
            yalign 0.505
            xalign 0.5
        Lydia "OMG THANKS MOM!! I LOVE YOU A LOT!"
        jump jawaban_lanjutanpositif1ha

    label jawaban_lanjutanpositif1ha:
        scene bg kamarlydia
        show mama senyum:
            yalign 0.505
            xalign 0.5
        Mama "Love you more my dear daugther. Let’s clean up now, okay?"
        jump jawaban_lanjutanpositif1hb

    label jawaban_lanjutanpositif1hb:
        scene bg kamarlydia
        show lydia2senyum:
            yalign 0.505
            xalign 0.5
        Lydia "AY AY AY CAPTAIN!"
        jump lydiamenghilang2a

    # YES --------- ^^^^^^^^^^

    label lydiamenghilang2a:
        scene bg kamarlydia
        show lydia2senyum:
            yalign 0.505
            xalign 0.5
        hide lydia2 with dissolve
        jump mulaipart2_2b

    label mulaipart2_2b:
        scene black with dissolve
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}After Lydia cleaned up her room, she showered for a while...{/color}"
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}Then, she goes downstairs and goes to the dining room...{/color}"
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}The food already served in the table, and she decides to give it a try.{/color}"
        jump otwmakan2c
    
    label otwmakan2c:
        scene bg dapurmalam
        show lydia3senyum:
            yalign 0.505
            xalign 0.5
        Lydia "God bless this food, you can already run a restaurant with this taste Mom!"

    label didapur2d:
        scene bg dapurmalam
        show mama senyum:
            yalign 0.505
            xalign 0.5
        Mama "If I do so, then you have to help me with all the stuffs, promise?"
        jump didapur2e

    label didapur2e:
        scene bg dapurmalam
        show lydia3senyum:
            yalign 0.505
            xalign 0.5
        Lydia "Of course I'll help with that!"
        jump didapur2f
    
    label didapur2f:
        scene bg dapurmalam
        show mama senyum:
            yalign 0.505
            xalign 0.5
        Mama "Ehe~"
        Mama "By the way, tomorrow is gonna be your first day of school, right?"
        jump didapur2g

    label didapur2g:
        scene bg dapurmalam
        show lydia3sedih:
            yalign 0.505
            xalign 0.5
        Lydia "Yaaa. I already feel very sick to my stomach."
        jump didapur2h

    label didapur2h:
        scene bg dapurmalam
        show mama biasa:
            yalign 0.505
            xalign 0.5
        Mama "Don’t overthink yourself honey, you can do this! Just focus on your study, I’m very proud of you, Lyd."
        jump didapur2i

    label didapur2i:
        scene bg dapurmalam
        show lydia3sedih:
            yalign 0.505
            xalign 0.5
        Lydia "AAWW don’t say such things Mom, you’re making me sad."
        jump didapur2j
    
    label didapur2j:
        scene bg dapurmalam
        show mama marah:
            yalign 0.505
            xalign 0.5
        Mama "Whatever you’re saying sweetie.. At this point, maybe it’s better for me to shut up, huh?"
        jump didapur2k

    label didapur2k:
        scene bg dapurmalam
        show lydia3marah:
            yalign 0.505
            xalign 0.5
        Lydia "I'M JUST KIDDING MOMM"
        jump didapur2l

    label didapur2l:
        scene black with dissolve
        play audio "audio/crowd_laughing.wav"
        centered "{color=#ffffff}They giggles and laughed~{/color}"
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}And they finished to eat their food...{/color}"
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}They decided to go to the living room together.{/color}"
        jump diruangtamu2m
    
    label diruangtamu2m:
        scene bg livingroommalam
        show lydia3senyum:
            yalign 0.505
            xalign 0.5
        Lydia "Mom, it’s so late already, don’t you want to go to bed?"
        jump diruangtamu2n

    label diruangtamu2n:
        scene bg dapurmalam
        show mama biasa:
            yalign 0.505
            xalign 0.5
        Mama "I want to finish this drama first honey, it’s already at the end."
    menu:
        extend "" # Agar muncul dialog dibawah option
    
        "Ask Mom to stop watching.": # [+]
            jump jawaban_positif2na
        "Watch drama with Mom together": # [-]
            jump jawaban_negatif2na

    # NO ------------------------------------------- BTW BUTUH BG RUANG TAMU MALAM

    label jawaban_negatif2na:
        scene bg livingroommalam
        show lydia3senyum:
            yalign 0.505
            xalign 0.5
        Lydia "Aight then I’ll just going to wait for you."
        jump jawaban_negatif2nb

    label jawaban_negatif2nb:
        scene bg livingroommalam
        show mama marah:
            yalign 0.505
            xalign 0.5
        Mama "Don’t sweetheart, you have to go to school tomorrow, so tonight you have to sleep more."
        jump jawaban_negatif2nc

    label jawaban_negatif2nc:
        scene bg livingroommalam
        show lydia3sedih:
            yalign 0.505
            xalign 0.5
        Lydia "But it has been such a long time since the last time I’ve watched a series with you."
        jump jawaban_negatif2nd

    label jawaban_negatif2nd:
        scene bg livingroommalam
        show mama sedih:
            yalign 0.505
            xalign 0.5
        Mama "Don’t even start an argue Lyd, now go to sleep."
        jump jawaban_negatif2ne

    label jawaban_negatif2ne:
        scene bg livingroommalam
        show lydia3sedih:
            yalign 0.505
            xalign 0.5
        Lydia "..."
        Lydia "Yes mom...."
        jump balikkamar2o


    # NO -------------^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    # YES ------------------------------------------

    label jawaban_positif2na:
        scene bg livingroommalam
        show lydia3marah:
            yalign 0.505
            xalign 0.5
        Lydia "You’re only focusing on your drama Mom... what about your dearest daughter??"
        jump jawaban_positif2nb

    label jawaban_positif2nb:
        scene bg livingroommalam
        show mama sedih:
            yalign 0.505
            xalign 0.5
        Mama "Please don’t start Lyd...."
        jump jawaban_positif2nc

    label jawaban_positif2nc:
        scene bg livingroommalam
        show lydia3marah:
            yalign 0.505
            xalign 0.5
        Lydia "Don’t be too sensitive Mom, you’ll catch a high blood pressure."
        jump jawaban_positif2nd

    label jawaban_positif2nd:
        scene bg livingroommalam
        show mama marah:
            yalign 0.505
            xalign 0.5
        Mama "Lydia? Are you really trying to start a fire right now? "
        jump jawaban_positif2ne
    
    label jawaban_positif2ne:
        scene bg livingroommalam
        show lydia3marah:
            yalign 0.505
            xalign 0.5
        Lydia "BYE MOM!"
        hide lydia with dissolve
        jump balikkamar2o

    # YES ------------^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    label balikkamar2o:
        play music "audio/lagumalam.mp3" # HARUS ADA MUSIK MALAM
        play sound "audio/door_open.wav"
        scene black with dissolve
        centered "{color=#ffffff}Lydia decided go to her room....{/color}"
        jump dikamar2p

    label dikamar2p:
        scene bg kamarlydiamalam
        play sound "audio/door_close.mp3"
        show lydia3sedih:
            yalign 0.505
            xalign 0.5
        Lydia "This is crazy, I’m very excited for tomorrow... Hoping I’ll get a friend at least."
        Lydia "Ugh I miss my old school.. why do I have to transfer tho? Besides I already have pretty cool friends back there.. Ah it’s tiring already thinking about it."
        jump lydiatertidur2q
    
    label lydiatertidur2q:
        scene black with dissolve
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}After thinking, Lydia fall asleep...{/color}"
        play sound "audio/next_dialogue.ogg"
        centered "{color=#c842f5}The next day....{/color}"
        scene black with dissolve
        jump besokpagi2r

    #KEESOKAN HARINYA
    label besokpagi2r:
        play sound "audio/door_open.wav"
        scene black with dissolve
        centered "{color=#ffffff}Suddenly Lydia's mom enters her room...{/color}"
        jump besokpagi2s

    label besokpagi2s:
        play music "audio/intro_ost.mp3"
        scene bg kamarlydia
        show mama marah:
            yalign 0.505
            xalign 0.5
        Mama "LYDIA WHAT TIME IS IT NOW??? YOU CAN’T BE LATE ON YOUR FIRST DAY OF SCHOOL"
        jump besokpagi2t

    label besokpagi2t:
        scene bg kamarlydia
        show lydia3sedih:
            yalign 0.505
            xalign 0.5
        Lydia "Gosh mom... please give me 5 more minutes. I’m very tired..."
        jump besokpagi2u

    label besokpagi2u:
        scene bg kamarlydia
        show mama marah:
            yalign 0.505
            xalign 0.5
        Mama "If you don’t get up now I will splash your face with cold water. One two ..."
    menu:
        extend "" # Agar muncul dialog dibawah option
    
        "Wake up": # [+]
            jump jawaban_positif2ua
        "Stay sleeping for some minutes": # [-]
            jump jawaban_negatif2ua

    label jawaban_negatif2ua:
        scene black with dissolve
        centered "{color=#ffffff}Lydia still laying on the bed..{/color}"
        play sound "audio/next_dialogue.ogg"
        jump jawaban_negatif2ub
        
    label jawaban_negatif2ub:
        scene bg kamarlydia
        show mama marah:
            yalign 0.505
            xalign 0.5
        Mama "LYDIA!!!"
        jump jawaban_negatif2uc
        
    label jawaban_negatif2uc:
        scene black with dissolve
        play sound "audio/next_dialogue.ogg"
        play sound "audio/splash.mp3"
        centered "{color=#ffffff}Suddenly her mom splashed water to wake her up!{/color}"
        play sound "audio/next_dialogue.ogg"
        jump jawaban_negatif2ud
        
    label jawaban_negatif2ud:
        scene bg kamarlydia
        show lydia3sedih:
            yalign 0.505
            xalign 0.5
        Lydia "Omaygaddd it’s cold momm"
        jump jawaban_negatif2ue
        
    label jawaban_negatif2ue:
        scene bg kamarlydia
        show mama marah:
            yalign 0.505
            xalign 0.5
        Mama "Told ya! Why didn’t you get up when I told you to. Go take a bath. Don’t look messy on your first day."
        jump lanjutan3a

        #----------------- [+}

    label jawaban_positif2ua:
        scene bg kamarlydia
        show lydia3senyum:
            yalign 0.505
            xalign 0.5
        Lydia "Yes mom I’m getting up."
        jump jawaban_positif2ub
        
    label jawaban_positif2ub:
        scene bg kamarlydia
        show mama biasa:
            yalign 0.505
            xalign 0.5
        Mama "Good girl, go take a bath now."
        jump jawaban_positif2uc
        
    label jawaban_positif2uc:
        scene bg kamarlydia
        show lydia3senyum:
            yalign 0.505
            xalign 0.5
        Lydia "Yes mom."
        jump jawaban_positif2ud

    label jawaban_positif2ud:
        scene bg kamarlydia
        show mama biasa:
            yalign 0.505
            xalign 0.5
        Mama "I will wait downstairs and make your breakfast."
        jump jawaban_positif2ue

    label jawaban_positif2ue:
        scene bg kamarlydia
        show lydia3senyum:
            yalign 0.505
            xalign 0.5
        Lydia "WOKEE gracias ma!"
        jump jawaban_positif2uf
        
    label jawaban_positif2uf:
        scene bg kamarlydia
        show mama biasa:
            yalign 0.505
            xalign 0.5
        Mama "Lyd, it’s still an early morning, don’t make me think too much by using the language that I don’t even know..."
        jump jawaban_positif2ug
        
    label jawaban_positif2ug:
        scene bg kamarlydia
        show lydia3senyum:
            yalign 0.505
            xalign 0.5
        Lydia "he he he, it means thanks mom!"
        jump lanjutan3a
        
    label lanjutan3a:
        scene black with dissolve
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}Lydia decided to shower,{/color}"
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}Wears her new school uniform...{/color}"
        jump diruangtamu3b
        
    label diruangtamu3b:
        scene bg livingroom
        show lydia sedih:
            yalign 0.505
            xalign 0.5
        Lydia "Have you done yet, Mom?? I’m gonna be late for school.."
        jump diruangtamu3c
        
    label diruangtamu3c:
        scene bg livingroom
        show mama marah:
            yalign 0.505
            xalign 0.5
        Mama "I’ve woken you up several times, but you still won’t get up, you sleepyhead.."
        jump diruangtamu3d
        
    label diruangtamu3d:
        scene bg livingroom
        show lydia sedih:
            yalign 0.505
            xalign 0.5
        Lydia "Ya momm, I’m sorry.."
        jump diruangtamu3e

    label diruangtamu3e:
        scene bg livingroom
        show mama biasa:
            yalign 0.505
            xalign 0.5
        Mama "Are you gonna eat the breakfast now? or later?"
    menu:
        extend "" # Agar muncul dialog dibawah option
    
        "Eat breakfast now": # [+]
            jump jawaban_positif3ea
        "Eat breakfast later": # [-]
            jump jawaban_negatif3ea

    label jawaban_positif3ea:
        scene bg livingroom
        show lydia biasa:
            yalign 0.505
            xalign 0.5
        Lydia "I’m gonna eat this now, I’m afraid that I won’t have time to eat it at school.."
        jump jawaban_positif3eb
        
    label jawaban_positif3eb:
        scene bg livingroom
        show mama marah:
            yalign 0.505
            xalign 0.5
        Mama "Hurry and eat it then, don’t focus on your phone anymore."
        jump jawaban_positif3ec
        
    label jawaban_positif3ec:
        scene bg livingroom
        show lydia sedih:
            yalign 0.505
            xalign 0.5
        Lydia "But I didn’t play my phone at all Mom...."
        jump jawaban_positif3ed
        
    label jawaban_positif3ed:
        scene bg livingroom
        show mama biasa:
            yalign 0.505
            xalign 0.5
        Mama "You’re still holding it tho.."
        jump jawaban_positif3ee
        
    label jawaban_positif3ee:
        scene bg livingroom
        show lydia senyum:
            yalign 0.505
            xalign 0.5
        Lydia "Okayyyy mom.. I’ll put it off."
        jump jawaban_positif3ef

    label jawaban_positif3ef:
        play sound "audio/sfx_makan.mp3" ## BUTUH SFX MAKAN
        scene black with dissolve
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}Lydia is eating her favourite food as her breakfast{/color}"
        play sound "audio/next_dialogue.ogg"
        jump jawaban_positif3eg
        
    label jawaban_positif3eg:
        scene black with dissolve
        centered "{color=#ffffff}She finished her meal..{/color}"
        play sound "audio/next_dialogue.ogg"
        jump jawaban_positif3eh

    label jawaban_positif3eh:
        scene bg livingroom
        show lydia senyum:
            yalign 0.505
            xalign 0.5
        Lydia "Mom I'm done now, I'm going to school now!"
        jump lanjutan3f
        
    label jawaban_negatif3ea:
        scene bg livingroom
        show lydia sedih:
            yalign 0.505
            xalign 0.5
        Lydia "I’m just gonna eat it in the class."
        jump lanjutan3f

    label lanjutan3f:
        scene bg livingroom
        show mama senyum:
            yalign 0.505
            xalign 0.5
        Mama "Alright, please be careful on your way and focus on listening to your teacher’s lesson, okay?"
        jump lanjutan3g
    
    label lanjutan3g:
        scene bg livingroom
        show lydia sedih:
            yalign 0.505
            xalign 0.5
        Lydia "Definitely Mom! You should also have to be careful!! Goodbye Mom!"
    
    # LYDIA OTW KE HALTE NAIK BIS MAU KE SEKOLAH

    label lanjutan3h:
        play audio "audio/sfx_lari.mp3"
        scene black with dissolve
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}Lydia running in hurry to catch the bus at the bus stop..{/color}"
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}She almost late, but she managed to enter the bus.{/color}"
        jump lanjutan3i
    
    label lanjutan3i:
        play audio "audio/bus_sound_effect.mp3"
        scene bg bus
        show lydia sedih:
            yalign 0.505
            xalign 0.5
        Lydia "Thank God I still have lots of time.."
        jump lanjutan3j

    label lanjutan3j:
        play music "audio/disclaimer_song.mp3"
        scene bg bus
        show lydia sedih:
            yalign 0.505
            xalign 0.5
        Lydia "It’s so quite in here, listening to my favorite song is gonna help..."
        jump introsekolah4a
    
    label introsekolah4a:
        scene black with dissolve
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}After 15 minutes, she arrived on her new school...{/color}"
        play sound "audio/next_dialogue.ogg"
        jump showcasedepansekolah4b
    
    label showcasedepansekolah4b:
        scene bg gerbangdepan with dissolve
        jump lanjutan4c

    label lanjutan4c:
        scene bg gerbangdepan
        show lydia biasa:
            yalign 0.505
            xalign 0.5
        Lydia "Didn’t expect that this school is gonna be this huge.... May God always be by my side so at least I won’t get lost.."
        jump kedebuk4d

    label kedebuk4d:
        scene black with dissolve
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}But suddenly..{/color}"
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}Ouch....{/color}"
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}Someone accidentally hit her!{/color}"
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}But, the guy who hitted her, seemed to just pass away as easy as that.{/color}"
        scene bg gerbangdepan
        show kiky biasa:
            yalign 0.505
            xalign 0.5
        hide kiky with dissolve
        jump kedebuk4e

    label kedebuk4e:
        scene bg gerbangdepan
        show lydia marah:
            yalign 0.505
            xalign 0.5
        Lydia "The hell, watch where you’re going bro, DON’T YOU WANT TO APOLOGIZE?"
        jump kedebuk4f
    
    label kedebuk4f:
        scene bg gerbangdepan
        show lydia marah:
            yalign 0.505
            xalign 0.5
        scene black with dissolve
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}He seemed to ignored what Lydia said..{/color}"
        play sound "audio/next_dialogue.ogg"
        jump kedebuk4g

    label kedebuk4g:
        scene bg gerbangdepan
        show lydia marah:
            yalign 0.505
            xalign 0.5
        Lydia "ARE YOU DEAF OR SOMETHING?"
        jump masuklorong4h
    
    label masuklorong4h:
        scene black with dissolve
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}Lydia decided to go inside the school, and walking across the corridor..{/color}"
        play sound "audio/next_dialogue.ogg"
        jump masuklorong4i

    label masuklorong4i:
        play music "audio/intro_ost.mp3"
        scene bg lorongsekolah
        show lydia biasa:
            yalign 0.505
            xalign 0.5
        Lydia "Where is the faculty lounge... the room is crowded... I think I will just ask someone..."
        jump samperinorang4j

    label samperinorang4j:
        scene black with dissolve
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}Lydia approached a random boy.{/color}"
        play sound "audio/next_dialogue.ogg"
        jump samperinorang4k

    label samperinorang4k:
        scene bg lorongsekolah
        show lydia biasa:
            yalign 0.505
            xalign 0.5
        Lydia "Hi... I’m Lydia, transfer student. May I ask where the faculty lounge is?"
        jump samperinorang4l

    label samperinorang4l:
        scene bg lorongsekolah
        show kiky senyum:
            yalign 0.505
            xalign 0.5
        UnknownKiky "Go straight, left, then turn right..."
        jump samperinorang4m

    label samperinorang4m:
        scene bg lorongsekolah
        show lydia marah:
            yalign 0.505
            xalign 0.5
        Lydia "What? Go straight, left, right??"
        jump samperinorang4n

    label samperinorang4n:
        scene bg lorongsekolah
        show kiky sedih:
            yalign 0.505
            xalign 0.5
        UnknownKiky "Uhm.."
        jump samperinorang4o

    label samperinorang4o:
        scene bg lorongsekolah
        show lydia sedih:
            yalign 0.505
            xalign 0.5
        Lydia "Ohh.. ok thanks..."
        jump pergidarisini4p

    label pergidarisini4p:
        scene black with dissolve
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}Lydia leave that weird person in hurry..{/color}"
        play sound "audio/next_dialogue.ogg"
        centered "{color=#c842f5}(Lydia) {/color}{color=#ffffff}I think I know that person... He's so weird..{/color}"
        play sound "audio/next_dialogue.ogg"
        play audio "audio/sfx_jalan.mp3"
        centered "{color=#ffffff}Lydia walks in front of the teacher's office, she sees a teacher in front of the teacher's office{/color}"
        play sound "audio/next_dialogue.ogg"
        jump ngomongsamaguru4q
    
    label ngomongsamaguru4q:
        scene bg lorongsekolah
        show lydia biasa:
            yalign 0.505
            xalign 0.5
        Lydia "Excuse me I’m looking for Miss Dely. May I know where she is?"
        jump ngomongsamaguru4r

    label ngomongsamaguru4r:
        scene bg lorongsekolah
        show dely senyum:
            yalign 0.505
            xalign 0.5
        Guru "Oh are you Lydia? Come with me."
        jump ngomongsamaguru4s

    label ngomongsamaguru4s:
        scene bg lorongsekolah
        show lydia biasa:
            yalign 0.505
            xalign 0.5
        Lydia "Okay Miss!"
        jump masukkelas5a

    # ADEGAN MASUK KELAS

    label masukkelas5a:
        scene bg kelas
        play audio "audio/sfx_jalan.mp3"
        scene black
        centered "{color=#ffffff}Lydia follows the teacher to her classroom...{/color}"
        play sound "audio/next_dialogue.ogg"
        jump masukkelas5b

    label masukkelas5b:
        scene bg kelas
        play audio "audio/door_open.wav"
        show dely senyum:
            yalign 0.505
            xalign 0.5
        Guru "Good morning students! We have a transfer student here. Lydia introduce yourself."

    label masukkelas5c:
        scene bg kelas
        play audio "audio/door_close.mp3"
        show lydia biasa:
            yalign 0.505
            xalign 0.5
        Lydia "Good morning everyone! I’m Lydia, I hope we can get along well. Nice meeting you guys!"
        jump perkenalan5d
    
    label perkenalan5d:
        play audio "audio/sfx_tepuktangan.wav"
        scene black with dissolve
        centered "{color=#ffffff}Everybody applaused at her!\nAnd also there's some students talking about her as well...{/color}"
        play sound "audio/next_dialogue.ogg"
        jump dudukdikelas5e

    label dudukdikelas5e:
        scene bg kelas
        show dely senyum:
            yalign 0.505
            xalign 0.5
        Guru "Nice to meet you too Lydia, go sit on the empty seat beside Kiky."
        jump dudukdikelas5f

    label dudukdikelas5f:
        scene bg kelas
        show lydia biasa:
            yalign 0.505
            xalign 0.5
        Lydia "Ok Miss!"
        jump dudukdikelas5g
    
    label dudukdikelas5g:
        play audio "audio/sfx_jalan.mp3"
        scene black with dissolve
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}Lydia walks to the seats that reserved to her.{/color}"
        play sound "audio/next_dialogue.ogg"
        jump dudukdikelas5h

    label dudukdikelas5h:
        scene bg kelas
        show lydia biasa:
            yalign 0.505
            xalign 0.5
        Lydia "Heyy, I'm Lydia. You're Kiky right? The teacher just told your name"
        jump lydiaberpikir5i

    label lydiaberpikir5i:
        scene bg kelas
        show lydia biasa:
            yalign 0.505
            xalign 0.5
        Lydia "(Eh, wasn't he is the boy before?)"
        jump dudukdikelas5j

    label dudukdikelas5j:
        scene bg kelas
        show kiky biasa:
            yalign 0.505
            xalign 0.5
        Kiky "yes"
        jump lydiaberpikir5k

    label lydiaberpikir5k:
        scene black
        play sound "audio/next_dialogue.ogg"
        centered "{color=#c842f5}(Lydia) {/color}{color=#ffffff}He's so arrogant..{/color}"
        play sound "audio/next_dialogue.ogg"
        jump dudukdikelas5k

    label dudukdikelas5k:
        scene bg kelas
        show lydia biasa:
            yalign 0.505
            xalign 0.5
        Lydia "By the way, you bumped into me and you didn’t say sorry at all."
        jump dudukdikelas5l

    label dudukdikelas5l:
        scene bg kelas
        show kiky sedih:
            yalign 0.505
            xalign 0.5
        Kiky "Oh sorry."
        jump lydiaberpikir5m

    label lydiaberpikir5m:
        scene black
        play sound "audio/next_dialogue.ogg"
        centered "{color=#c842f5}(Lydia) {/color}{color=#ffffff}He's so damn cold.. Idk if I'm fine to sit with him for long time..{/color}"
        play sound "audio/next_dialogue.ogg"
        jump tibatiba5n

    label tibatiba5n:
        scene black with dissolve
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}Suddenly, there's a girl behind Lydia introduced herself.{/color}"
        play sound "audio/next_dialogue.ogg"
        jump ngomongsamacewe5o

    label ngomongsamacewe5o:
        scene bg kelas
        play audio "audio/teacherexplaining.wav" volume 0.1
        show moon senyum:
            yalign 0.505
            xalign 0.5
        Moon "Hey Lydia! I’m Moon. Nice to meet you."
        jump ngomongsamamoon5p
    
    label ngomongsamamoon5p:
        scene bg kelas
        show moon senyum:
            yalign 0.505
            xalign 0.5
        Moon "Oh ya, this is Tom and Jerry."
        jump jerryngomong5q

    label jerryngomong5q:
        scene bg kelas 
        show jerry marah:
            yalign 0.505
            xalign 0.5
        Jerry "Tom and Jerry? Who the heck is Tom? Please don’t mess with me Moon, you’re gonna regret it later"
        jump dibalasmoon5r
    
    label dibalasmoon5r:
        scene bg kelas 
        show moon senyum:
            yalign 0.505
            xalign 0.5
        Moon "Tom and Jerry is still a cute name tho. And it’s not me who started all this things, you’re the one who messed with me first."
        jump dibalasjerry5s

    label dibalasjerry5s:
        scene bg kelas 
        show jerry marah:
            yalign 0.505
            xalign 0.5
        Jerry "That’s because you always-"
        jump dibalaslydia5t

    label dibalaslydia5t:
        scene bg kelas
        show lydia biasa:
            yalign 0.505
            xalign 0.5
        Lydia "Calm down guys, so is it Tom or Jerry?"
        jump dibalasjerry5u

    label dibalasjerry5u:
        scene bg kelas 
        show jerry senyum:
            yalign 0.505
            xalign 0.5
        Jerry "It’s Jerry, don’t listen to Moon, Lyd."
        jump dibalasjerry5ub

    label dibalasjerry5ub:
        scene bg kelas 
        show jerry biasa:
            yalign 0.505
            xalign 0.5
        Jerry "Oh! And this is Raphael."
        jump samaraphael5v

    label samaraphael5v:
        scene bg kelas
        play audio "audio/teacherexplaining.wav" fadein 10.0 fadeout 3.0
        show dely marah:
            yalign 0.505
            xalign 0.5
        Guru "Raphael! You’re still talking while I’m in class now?"
        jump pertengahanpengecualian1

    label pertengahanpengecualian1:
        play sound "audio/next_dialogue.ogg"
        scene black
        centered "{color=#ffffff}The class keep going like usual after the teacher felt interrupted by Raphael.{/color}"
        jump kelydia5w

    label kelydia5w:
        scene bg kelas
        show lydia biasa:
            yalign 0.505
            xalign 0.5
        Lydia "Ki, can you help me? How can this X turns into Y?"
        jump kekiky5x

    label kekiky5x:
        scene bg kelas
        show kiky marah:
            yalign 0.505
            xalign 0.5
        Kiky "Sstt! Can’t you see that the teacher is explaining it now?"
        jump kelydia5y

    label kelydia5y:
        scene bg kelas
        show lydia marah:
            yalign 0.505
            xalign 0.5
        Lydia "Why are you mad? I’m only asking tho"
        jump kelydia5z

    label kelydia5z:
        scene black with dissolve
        play sound "audio/next_dialogue.ogg"
        centered "{color=#c842f5}(Lydia) {/color}{color=#ffffff}This guy is stressing me out.....{/color}"
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}The subject ended, and now it's lunch time. But then Moon asked Lydia to have lunch together.{/color}"
        play sound "audio/next_dialogue.ogg"
        jump selesai6a

    label selesai6a:
        scene bg kelas 
        show moon bingung:
            yalign 0.505
            xalign 0.5
        Moon "Lyd! Let’s have lunch together! We'll go the cafeteria you might see what you like there!"
    menu:
        extend "" # Agar muncul dialog dibawah option
    
        "Sure let's go!": # [+]
            jump jawaban_positif6aa
        "I have my lunch box here with me, Moon.": # [-]
            jump jawaban_negatif6aa

    label jawaban_negatif6aa:
        scene bg kelas
        show lydia sedih:
            yalign 0.505
            xalign 0.5
        Lydia "I have my lunch box here with me, Moon."
        jump jawaban_negatif6ab

    label jawaban_negatif6ab:
        scene bg kelas
        show jerry senyum:
            yalign 0.505
            xalign 0.5
        Jerry "You can bring it to the canteen Lyd, so we can eat together."
        jump jawaban_negatif6c
    
    label jawaban_negatif6c:
        scene bg kelas
        show lydia senyum:
            yalign 0.505
            xalign 0.5
        Lydia "That’s a great idea! Let’s go!"
        jump kekantin6b

    label jawaban_positif6aa:
        scene bg kelas
        show lydia biasa:
            yalign 0.505
            xalign 0.5
        Lydia "Sure, Let's go!"
        jump kekantin6b

    label kekantin6b:
        play audio "audio/sfx_jalan.mp3"
        scene black with dissolve
        centered "{color=#ffffff}Moon, Lydia, Raphael, Jerry went to the cafeteria together..{/color}"
        play sound "audio/next_dialogue.ogg"
        jump kekantin6c
    
    label kekantin6c:
        scene bg kantinpagi
        show moon senyum:
            yalign 0.505
            xalign 0.5
        Moon "Guys! Let’s just sit here!"
        jump kekantin6d
    
    label kekantin6d:
        scene bg kantinpagi
        show jerry senyum:
            yalign 0.505
            xalign 0.5
        Jerry "Alrightyyyyy.."
        jump kekantin6e

    label kekantin6e:
        play audio "audio/sfx_chatter.mp3"
        scene black with dissolve
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}They decided to sit together with the meal they prepared.{/color}"
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}They eat together..{/color}"
        play sound "audio/next_dialogue.ogg"
        jump kekantin6f

    label kekantin6f:
        scene bg kantinpagi
        show lydia biasa:
            yalign 0.505
            xalign 0.5
        Lydia "Umm is that Kiky?"
        jump kekantin6g
    
    label kekantin6g:
        scene bg kantinpagi
        show lydia marah:
            yalign 0.505
            xalign 0.5
        Lydia "Hey you come here!"
        jump tambahanpengecualian

    label tambahanpengecualian:
        scene black with dissolve
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}Lydia tried to call Kiky, but Kiky seemed to ignore her.{/color}"
        jump kekantin6h

    label kekantin6h:
        scene bg kantinpagi
        show lydia marah:
            yalign 0.505
            xalign 0.5
        Lydia "Damn is he really deaf? I think he needs to check his ears."
        jump kekantin6i

    label kekantin6i:
        scene bg kantinpagi
        show moon bingung:
            yalign 0.505
            xalign 0.5
        Moon "Lydia, you are close with Kiky?"
        jump kekantin6j

    label kekantin6j:
        scene bg kantinpagi
        show moon senyum:
            yalign 0.505
            xalign 0.5
        Moon "WOOHOOO it’s your first day and you already have someone that you like!"
        jump kekantin6k

    label kekantin6k:
        scene bg kantinpagi
        show lydia marah:
            yalign 0.505
            xalign 0.5
        Lydia "What are you talking about? we are not close at all. He doesn’t want to talk to me, way too arrogant."
        jump dikantin6l

    label dikantin6l:
        scene bg kantinpagi
        show moon senyum:
            yalign 0.505
            xalign 0.5
        Moon "Aaa yes he is hella cold. He never have a close kind of relationship with anyone."
        jump dikantin6m
    
    label dikantin6m:
        scene bg kantinpagi
        show lydia biasa:
            yalign 0.505
            xalign 0.5
        Lydia "Oh really? Does he not feel lonely?"
        jump dikantin6n

    label dikantin6n:
        scene bg kantinpagi
        show moon senyum:
            yalign 0.505
            xalign 0.5
        Moon "It’s normal for him to be lonely."
        jump dikantin6o

    label dikantin6o:
        scene bg kantinpagi
        show raphael senyum:
            yalign 0.505
            xalign 0.5
        Raphael "By the way Lyd, where are you from? Was interrupted by miss Dely."
        jump dikantin6p

    label dikantin6p:
        scene bg kantinpagi
        show jerry biasa:
            yalign 0.505
            xalign 0.5
        Jerry "Oh ya, where are you from?"
        jump dikantin6q

    label dikantin6q:
        scene bg kantinpagi
        show lydia senyum:
            yalign 0.505
            xalign 0.5
        Lydia "I’m from somewhere in your heart"
        jump dikantin6r
    
    label dikantin6r:
        play audio "audio/crowd_laughing.wav"
        scene black with dissolve
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}They all laughed because of that.{/color}"
        play sound "audio/next_dialogue.ogg"
        jump dikantin6s

    label dikantin6s:
        scene bg kantinpagi
        show raphael senyum:
            yalign 0.505
            xalign 0.5
        Raphael "Seriously pretty.."
        jump dikantin6t
    
    label dikantin6t:
        scene bg kantinpagi
        show moon senyum:
            yalign 0.505
            xalign 0.5
        Moon "Ew, gross, Lyd you better not fall to Ael’s trap ya, he’s such a player"
        jump dikantin6u
    
    label dikantin6u:
        scene bg kantinpagi
        show raphael marah:
            yalign 0.505
            xalign 0.5
        Raphael "Mumun, you better shut up."
        jump dikantin6v
    
    label dikantin6v:
        scene bg kantinpagi
        show raphael biasa:
            yalign 0.505
            xalign 0.5
        Raphael "Now seriously Lyd, where do you come from?"
        jump dikantin6w
    
    label dikantin6w:
        scene bg kantinpagi
        show lydia biasa:
            yalign 0.505
            xalign 0.5
        Lydia "I’m from Surabaya, you guys are like really from Jakarta?"
        jump dikantin6x

    label dikantin6x:
        scene bg kantinpagi
        show moon senyum:
            yalign 0.505
            xalign 0.5
        Moon "Me and Jerry both were born in here, Jakarta, but Raphael is from Jogja."
        jump dikantin6y

    label dikantin6y:
        scene bg kantinpagi
        show lydia biasa:
            yalign 0.505
            xalign 0.5
        Lydia "Ohh i see.. then do you know where Kiky comes from?"
        jump dikantin6z

    label dikantin6z:
        scene bg kantinpagi
        show moon senyum:
            yalign 0.505
            xalign 0.5
        Moon "Such a curious one, Lydddd, are you like starting things??"
        jump dikantin6aa

    label dikantin6aa:
        scene bg kantinpagi
        show lydia sedih:
            yalign 0.505
            xalign 0.5
        Lydia "Starting what things? What are you even talking about sist.."
        jump dikantin6ab

    label dikantin6ab:
        scene bg kantinpagi
        show moon senyum:
            yalign 0.505
            xalign 0.5
        Moon "Starting to have those interests babe."
        jump dikantin6ac

    label dikantin6ac:
        scene bg kantinpagi
        show lydia biasa:
            yalign 0.505
            xalign 0.5
        Lydia "Duh, never gonna fall for that kind of guy.."
        jump dikantin6ad

    label dikantin6ad:
        scene bg kantinpagi
        show jerry senyum:
            yalign 0.505
            xalign 0.5
        Jerry "You’ll never know, Lyd.."
        jump lorong7a
    
    label lorong7a:
        play audio "audio/sfx_bellringing.wav"
        scene black with dissolve
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}Suddenly, the bell rings for the next class..{/color}"
        play sound "audio/next_dialogue.ogg"
        jump lorong7b
    
    label lorong7b:
        scene bg lorongsekolah
        play audio "audio/sfx_lari.mp3"
        Narrator "Everyone went to their class.."
        jump lorong7c

    label lorong7c:
        scene bg lorongsekolah
        show lydia biasa:
            yalign 0.505
            xalign 0.5
        Lydia "Hey Moon! You haven’t answered my question yet!"
        jump lorong7d

    label lorong7d:
        scene bg lorongsekolah
        show moon bingung:
            yalign 0.505
            xalign 0.5
        Moon "What kind of questions huh??"
        jump lorong7e

    label lorong7e:
        scene bg lorongsekolah
        show lydia senyum:
            yalign 0.505
            xalign 0.5
        Lydia "About that Kiky one."
        jump lorong7f

    label lorong7f:
        scene bg lorongsekolah
        show moon senyum:
            yalign 0.505
            xalign 0.5
        Moon "You’re really interested in him, huh, Lyd??"
        jump lorong7g

    label lorong7g:
        scene bg lorongsekolah
        show lydia marah:
            yalign 0.505
            xalign 0.5
        Lydia "MOON!"
        jump lorong7h

    label lorong7h:
        scene bg lorongsekolah
        play audio "audio/sfx_lari.mp3"
        Narrator "Moon runs, Lydia catching Moon..."
        jump ending7i

    label ending7i:
        scene black with dissolve
        play sound "audio/next_dialogue.ogg"
        centered "{color=#c842f5}To be continued..{/color}{color=#ffffff}\nChapter 2 is coming soon! A great rating for this game will be push us to continue the journey of this game as soon as possible!{/color}"
        play sound "audio/next_dialogue.ogg"
        centered "{color=#ffffff}By clicking this, Will end the game temporarily. Thanks for playing our game! :){/color}"

    return # WAJIB ADA



# The game starts here.

#label start:

    ### -------------- MAIN GAME SCRIPT - INTRO ---------------------#

#    scene bg kamar_lydia

#    play music "audio/ost_intro.mp3" volume 1.0 fadeout 0.5

#    play sound "audio/lydia_phone_ringtone.wav"

    
    ### ------------- MULAI DEMO SCRIPT ------------- ###

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    #play sound "audio/running_catch_bus.mp3"

    #window hide
    #pause

    #centered "{color=#ffffff}Moon and you seemed to miss the bus at the but stop, so you and her decided to run..{/color}"

    #stop music

    #window show

    #play sound "audio/next_dialogue.ogg"
    #Moon "Wait for me!!"

    #stop sound

    #scene bg bus with dissolve

    #show moon sedih:
    #    yalign 0.505
    #    xalign 0.5

    #play sound "audio/next_dialogue.ogg"
    #Moon "How dare you left me just like that..."

    #show moon senyum:
    #    yalign 0.505
    #    xalign 0.5

    #play sound  "audio/next_dialogue.ogg"
    #Moon "Anyways we made it to bus now!"


    #label ditanya:
    #    show moon bingung:
    #        yalign 0.505
    #        xalign 0.5

    #    play sound "audio/next_dialogue.ogg"
    #    Moon "Good thing there are some seats remaining, now where do we have to sit?"
    #menu:
    #    extend "" # Agar muncul dialog dibawah option
    #
    #    "How about we sit at the back seat? Seems comfy enough.":
    #        jump opsi1_a
    #    "Why don't you decide this time?":
    #        jump opsi1_b

    #label opsi1_a:
    #    show moon senyum:
    #        yalign 0.505
    #        xalign 0.5
    #    Moon "Ah that sounds great for me! Let's go."     
    #    jump opsi1_ngomong

    #label opsi1_b:
    #    show moon marah:
    #        yalign 0.505
    #        xalign 0.5
    #    play sound "audio/next_dialogue.ogg"
    #    Moon "You just leave me and now you asked me to decide where we sit? Ugh.."
    #    play sound "audio/next_dialogue.ogg"
    #    Moon "Ughh fine let's sit at the back seat, I like that spot."   
    #    jump opsi1_ngomong   

    #label opsi1_ngomong:
    #    scene black with dissolve
        
    #    play sound "audio/next_dialogue.ogg"
    #    centered "{color=#ffffff}You and Moon decided to sit together at the back seat.{/color}"

    #play sound "audio/next_dialogue.ogg"
    #play sound "audio/bus_sound_effect.mp3" fadein 2 fadeout 2
    #centered "{color=#ffffff}Right on time, the bus finally starts to move..{/color}"
    
    #scene bg bus with dissolve

    #show moon bingung:
    #    yalign 0.505
    #    xalign 0.5
    #play sound "audio/next_dialogue.ogg"
    #Moon "I feel so sleepy... I'm going to take a quick nap... See you later!"

    #stop sound

    #scene black with dissolve
    #play sound "audio/next_dialogue.ogg"
    #centered "{color=#ffffff}Moon falls asleep...{/color}"
    #play sound "audio/next_dialogue.ogg"
    #centered "{color=#ffffff}To be continued..\nPlease not, this is not the final content of this game. Yet we need time to implement our scripts on it. \nStay tuned!{/color}"

    #return

# Intro


    #return

# Disclaimer Image

image splash = ("Disclaimer.jpg")
image menuv5 = ("MenuV5.png")

label splashscreen:
    scene black
    with Pause(1)

    play sound "audio/disclaimer_song.mp3"

    show splash with dissolve
    with Pause(8)

    stop sound

    show menuv5 with dissolve
    with Pause(0.75)

    return
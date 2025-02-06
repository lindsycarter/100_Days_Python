import time

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`." |` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island!")
time.sleep(1)

print("Your Mission is to find the treasure.")
time.sleep(1)

print("Good Luck!")
time.sleep(1)

print("After bushwhacking through the jungle for hours, you find yourself at a clearing with two distinct footpaths. \n"
      "You are really scratched up and ready for an easy pace and decide to continue down one path.")
time.sleep(2)

path_choice = input("Which path would you like to take? Type [left] or [right]: \n").lower()

if path_choice == "left":
    wait_swim = input("You come to a wide lake and see an island in the middle of the lake. \n"
                      "After reviewing your maps and notes, you are sure that's the location \n"
                      "you've been searching for. \n"
                      "Type [wait] to wait for the boat. Type [swim] to attempt to swim across. \n").lower()
    if wait_swim == "wait":
        time.sleep(0.5)
        print('''
              __________
             /________ /|
            |   XII , | |
            |     ,'  | |
            |IX  * III| |
            |     `.  | |
            |____VI___| |
            |    |    | |
            |    |    | |
            |    |    | |
            |   ( )   | |
            |_________|/
        ''')
        print("tick")
        time.sleep(0.5)

        print('''
              __________
             /________ /|
            |   XII , | |
            |     ,'  | |
            |IX  * III| |
            |     `.  | |
            |____VI___| |
            |    |    | |
            |    |    | |
            |    |    | |
            |   ( )   | |
            |_________|/
        ''')
        print("tock")
        time.sleep(0.5)

        print('''
              __________
             /________ /|
            |   XII , | |
            |     ,'  | |
            |IX  * III| |
            |     `.  | |
            |____VI___| |
            |    |    | |
            |    |    | |
            |    |    | |
            |   ( )   | |
            |_________|/
        ''')

        print("tick")
        time.sleep(0.5)

        print('''
              __________
             /________ /|
            |   XII , | |
            |     ,'  | |
            |IX  * III| |
            |     `.  | |
            |____VI___| |
            |    |    | |
            |    |    | |
            |    |    | |
            |   ( )   | |
            |_________|/
        ''')
        print("tock")
        time.sleep(0.5)

        print('''
              __________
             /________ /|
            |   XII , | |
            |     ,'  | |
            |IX  * III| |
            |     `.  | |
            |____VI___| |
            |    |    | |
            |    |    | |
            |    |    | |
            |   ( )   | |
            |_________|/
        ''')
        print("tick")
        time.sleep(0.5)

        print('''
              __________
             /________ /|
            |   XII , | |
            |     ,'  | |
            |IX  * III| |
            |     `.  | |
            |____VI___| |
            |    |    | |
            |    |    | |
            |    |    | |
            |   ( )   | |
            |_________|/
        ''')
        print("tock \n")
        time.sleep(1)

        print("After waiting for what feels like hours, you finally see the boat leave the island and you \n"
              "impatiently wait. Once on the boat, you are able to cross the lake safely and reach the other side.")
        time.sleep(2)

        door_choice = input("Venturing deep into the island, you come across a house with three (3) doors. \n"
                            "One [yellow], one [blue], and one [red]. Which door would you like to open? \n").lower()

        if door_choice == "yellow":
            print('''
                X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X
                |                           ,,'``````````````',,                            |
                X                        ,'`                   `',                          X
                |                      ,'                         ',                        |
                X                    ,'          ;       ;          ',                      X
                |       (           ;             ;     ;             ;     (               |
                X        )         ;              ;     ;              ;     )              X
                |       (         ;                ;   ;                ;   (               |
                X        )    ;   ;    ,,'```',,,   ; ;   ,,,'```',,    ;   ;               X
                |       (    ; ',;   '`          `',   ,'`          `'   ;,' ;              |
                X        )  ; ;`,`',  _--~~~~--__   ' '   __--~~~~--_  ,'`,'; ;     )       X
                |       (    ; `,' ; :  /       \~~-___-~~/       \  : ; ',' ;     (        |
                X  )     )   )',  ;   -_\  o    /  '   '  \    o  /_-   ;  ,'       )   (   X
                | (     (   (   `;      ~-____--~'       '~--____-~      ;'  )     (     )  |
                X  )     )   )   ;            ,`;,,,   ,,,;',            ;  (       )   (   X
                | (     (   (  .  ;        ,'`  (__ '_' __)  `',        ;  . )     (     )  |
                X  )     \/ ,".). ';    ,'`        ~~ ~~        `',    ;  .(.", \/  )   (   X
                | (   , ,'|// / (/ ,;  '        _--~~-~~--_        '  ;, \)    \|', ,    )  |
                X ,)  , \/ \|  \\,/  ;;       ,; |_| | |_| ;,       ;;  \,//  |/ \/ ,   ,   X
                |",   .| \_ |\/ |#\_/;       ;_| : `~'~' : |_;       ;\_/#| \/| _/ |.   ,"  |
                X#(,'  )  \\\#\ \##/)#;     :  `\/       \/   :     ;#(\##/ /#///  (  ',)# ,X
                || ) | \ |/ /#/ |#( \; ;     :               ;     ; ;/ )#| \#\ \| / | ( |) |
                X\ |.\\ |\_/#| /#),,`   ;     ;./\_     _/\.;     ;   `,,(#\ |#\_/| //.| / ,X
                | \\_/# |#\##/,,'`       ;     ~~--|~|~|--~~     ;       `',,\##/#| #\_// \/|
                X  ##/#  #,,'`            ;        ~~~~~        ;            `',,#  #\##  //X
                |####@,,'`                 `',               ,'`                 `',,@####| |
                X#,,'`                        `',         ,'`                        `',,###X
                |'                               ~~-----~~                               `' |
                X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X
            ''')

            print("You have entered a room with a snarling beast man that rips you to shreds as soon as you enter.")
            time.sleep(1)
            print("GAME OVER, MAN. TRY AGAIN!")

        if door_choice == "blue":
            print('''
            ⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠻⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⡇⠠⣄⡉⠙⠛⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢸⣿⣷⣌⠻⣿⣿⣿
            ⣿⣿⣿⣿⣧⠀⣿⣿⣷⣦⣄⡀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⠀⢿⣿⣿⣷⣌⠻⣿
            ⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⣠⡿⠋⠙⢷⣄⠙⠛⠿⠿⢠⣿
            ⣿⣿⣿⣿⣿⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⠟⠁⠀⡠⠀⠀⣹⣿⣿⣿⣷⣿⣿
            ⣿⣿⣿⣿⣿⡆⢸⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⢀⣴⠟⠀⢀⡾⠛⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⠋⠀⢀⣴⠟⠁⢀⣴⡟⠀⠀⠈⢿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⡇⠘⣿⣿⣿⣿⠟⠁⢀⣴⠟⠁⠀⣠⣾⣿⣷⡄⠀⠀⠈⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣷⠀⣿⣿⡟⠁⢀⣴⠟⠁⢀⣤⣾⣿⣿⣿⣿⣿⣆⠀⠀⢻⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⠀⡿⠋⢀⣴⠟⠁⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠸⣿⣿⣿
            ⣿⣿⣿⣿⣿⡿⠀⢀⣴⠟⠁⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⢿⣿⣿
            ⣿⣿⣿⣿⠟⠀⠀⠘⠁⠀⠚⠛⠛⠻⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣆⠘⣿⣿
            ⣿⣿⠟⠁⠀⠀⢀⣤⣾⣿⣿⣿⣶⣶⣶⣶⣶⣶⣦⣤⣤⣤⣤⣤⣤⣀⣉⣀⣸⣿
            ⣿⣧⡀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ''')

            print("You chose poorly. This door was rigged with a crossbow. As soon as you opened the door you felt a "
                  "stabbing pain as the heavy bolt slams into your chest and your world goes dark. Game Over.")

        if door_choice == "red":
            print("As you open the door, you can see candle light flickering and distinct gleam of shiny things. \n"
                  "As your eyes adjust to the low light you realize the shiny things are piles and piles of \n"
                  "gold pieces and jewels. You have found the treasure that no one else has ever been able to. \n")
            time.sleep(2)

            print('''
            *******************************************************************************
                      |                   |                  |                     |
             _________|________________.=""_;=.______________|_____________________|_______
            |                   |  ,-"_,=""     `"=.|                  |
            |___________________|__"=._o`"-._        `"=.______________|___________________
                      |                `"=._o`"=._      _`"=._                     |
             _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
            |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
            |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                      |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
             _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
            |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
            |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
            ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
            /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
            ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
            /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
            ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
            /______/______/______/______/______/______/______/______/______/______/_____ /
            *******************************************************************************
            ''')
            time.sleep(1)
            print("You Win! Now go swim in the loot like Scrooge McDuck!")

    if wait_swim == "swim":
        print("You enter the ice cold water and start to swim to the island. After about 5 minutes, you notice \n"
              "something touch your leg. As you start to swim faster, you feel a 2nd and 3rd somethings touching you.\n"
              "You search the water frantically but it's so dark you can't even see the thing that just chomped down \n"
              "on your leg. You are dragged below the water.\n")
        time.sleep(1)
        print('''
                       ______
                    .-"      "-.
                   /            \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \__)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)
        ''')

        print("GAME OVER")

if path_choice == "right":
    print("After about 50 feet you are quickly swept up with an expertly hidden net. As you dangle, squished in the\n"
          "net, you see a group of men coming towards you. They are wearing grass skirts, no shirts or shoes and \n"
          "have white painted symbols over their bodies. You are 100% sure this is the Tribe Called Grue and \n"
          "they are likely to eat you.\n")
    time.sleep(1)

    print('''
                \\\\\//////                                          
    .-""-.     \\\\\\//////                                          
   / _  _ \   [[[[[[[]]]]]]]]                                        
   |(_)(_)|   /////////\\\\\\                                        
   (  /\  )  //// ~0 ( 0~ \\\\    I THINK HUMAN FLESH IS DELICIOUS   
    L====J   //(,  8-_\-8 ,)\\                                       
    `-..-`    //|\ .===. /|\\     THEREFORE I WILL LIKELY DIE OF     
     \\//        \ '===' /*       SOME HORRIBLE TRANSMISSABLE DISEASE
      ||          \__.__/                                            
   _.=||=._   .---'@   @'---.                                        
   /| || |\  /     '@ @'     \                                       
     _||_   /    .   Y   .  _/\                                      
    /  _))-'  /|'---{@}---'|\_/\                                     
    |  _)  _.' |   --:--   | \  \                                    
    \___)-'    |   --:--   |  \  \                            
''')

    print("GAME OVER. That was " + "\x1B[3m" + "gruesome." + "\x1B[0m" + " Try again!")

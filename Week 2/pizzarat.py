import pyglet
import time
import os


catFX = pyglet.media.load( "/Users/johnyvino/Desktop/Sounds/cat.wav", streaming=False)
subwayFX = pyglet.media.load("/Users/johnyvino/Desktop/Sounds/subway.wav", streaming=False)
pizzaFX = pyglet.media.load("/Users/johnyvino/Desktop/Sounds/pizza.wav", streaming=False)
ratFX = pyglet.media.load( "/Users/johnyvino/Desktop/Sounds/rat.wav", streaming=False)
cockroachFX = pyglet.media.load("/Users/johnyvino/Desktop/Sounds/cockroach.wav", streaming=False)
gameoverFX = pyglet.media.load("/Users/johnyvino/Desktop/Sounds/gameover.wav", streaming=False)
endcreditsFX = pyglet.media.load("/Users/johnyvino/Desktop/Sounds/endcredits.wav", streaming=False)  
snackFX = pyglet.media.load("/Users/johnyvino/Desktop/Sounds/snack.wav", streaming=False)    


userInput = ""


# def playFile(filePath):
    
#     music = pyglet.media.load(filePath, streaming=False)
#     music.play()

def getInput(text):
    
    str = raw_input(text)
    return str
    
    
    ##########
    #
    # MAIN
    #
    ##########


    # INTRO


def printintro ():
    print "PROLOGUE\n\n"    
    print "IT AINT EASY BEING THE INFAMOUS PIZZA RAT." 
    print "You humans have marginalized and reduced me to a pathetic MEME.\n\n"
    print "I LOVE PIZZA! Is that so wrong? You don't see me posting images of you, mocking you when you hungrily scarf down $12 avocado toast and $6 sustainable shade grown coffee.\n\n"
    print "Perhaps if you step into my dirty furry rodent paws, you will see the struggles I got through in search of that perfect discarded slice.\n\n"
    print "READY TO PLAY?"

    startstory()


def printtitle ():
    print "title"
    myTitle = """


$$$$$$$\ $$$$$$\ $$$$$$$$\ $$$$$$$$\  $$$$$$\        $$$$$$$\   $$$$$$\ $$$$$$$$\ $$\ 
$$  __$$\\_$$  _|\____$$  |\____$$  |$$  __$$\       $$  __$$\ $$  __$$\\__$$  __|$$ |
$$ |  $$ | $$ |      $$  /     $$  / $$ /  $$ |      $$ |  $$ |$$ /  $$ |  $$ |   $$ |
$$$$$$$  | $$ |     $$  /     $$  /  $$$$$$$$ |      $$$$$$$  |$$$$$$$$ |  $$ |   $$ |
$$  ____/  $$ |    $$  /     $$  /   $$  __$$ |      $$  __$$< $$  __$$ |  $$ |   \__|
$$ |       $$ |   $$  /     $$  /    $$ |  $$ |      $$ |  $$ |$$ |  $$ |  $$ |       
$$ |     $$$$$$\ $$$$$$$$\ $$$$$$$$\ $$ |  $$ |      $$ |  $$ |$$ |  $$ |  $$ |   $$\ 
\__|     \______|\________|\________|\__|  \__|      \__|  \__|\__|  \__|  \__|   \__|
"""
    print myTitle
                                                                                      

def printpizza ():
    myPizza = """
          // ""--.._
         ||  (_)  _ "-._
         ||    _ (_)    '-.
         ||   (_)   __..-'
          \\__..--""

      """

    print myPizza


def printrat ():
    myRat = """
         __             _,-"~^"-.
       _// )      _,-"~`         `.
     ." ( /`"-,-"`                 ;
    / 6                             ;
   /           ,             ,-"     ;
  (,__.--.      \           /        ;
   //'   /`-.\   |          |        `._________
     _.-'_/`  )  )--...,,,___\     \-----------,)
   ((("~` _.-'.-'           __`-.   )         //
     jgs ((("`             (((---~"`         //
                                            ((________________
                                            `----""""~~~~^^^```"""

    print myRat


def printbagel ():
    myBagel = """

                  ````````              
            `.-/oo+syooy+ooo/-          
         ./+sssysoy+ss++hs++/:`         
      `-ssyssyy+o+yso++oyso//:`         
     .oohsssss++++++os+oss+:-:-         
    :ss+soshdyydoooss+oo+s+-..-.        
   +yyhmyyyyyyys+ydyssoyyosy.``..````` `
  :ysyssyysyhssshyhssyysshs++/.-.../o/ `
 `dhhhysssshdyyss/    -os+ssssooysysos: 
 `yyhsooshyyyhyh.      `y+sysy++yyhhso.`
  yydyyyyyhsdhy-        /sssossysoosso `
  +yysyhyhhyyhsh:      .yoys+syhhssyhs  
  -ssshoodyshssyo+o/.:++ososyssyhhmmh:  
  `+hhdhsyyoso+ooyyso++ssosooyyhdhhhs`  
   `yhdshssso+shss++/++ss+oyyyhhddmh.   
    `ohhsyyyyhssssss+/sssyyyyymmdy:`    
      -ymhdhhyyyhdddyyssyyhyhhdy.       
       `+hdddyddhdmmhhddhdNNyo.         
          .:oshhddmdddyso+.`            
                  `             
                  """  
    print myBagel      


def printskull ():
    mySkull = """                                            
                                              .:///`                                                
                                         .+ymmhsssyyhddho-                                          
                                      -sdy+-`          `:ohy-                                       
                                    :hs-                   .sh-                                     
                                   sy` -                   .--m+                                    
                                  y+ .ms                   oN``m+                                   
                                 sh  h+                     m: :N`                                  
                                -M:  M-                     mo  N:                                  
                                /M` .M/ `-/osso.   `:/++/.  mh `M-                                  
                                 o/ :M:yMMMMMMMN- hMMMMMMMm:hN`hs                                   
                                  :shooMMMMMMMMMy`NMMMMMMMMMsMm:                                    
                                   sy NMMMMMMMMd. -dMMMMMMMMNoh                                     
                       `.          o+ mMMMMMms:+NNs`:yNMMMMMN`N                                     
                     `ydydh:       /N+.++/-`  :MMMMs   -/oyy:om         .ohs`                       
                    `dm`  /mmo.     +MMmy/`   +MMMM+    .+shNy`       -hh--so                       
                    sh      -+hdy+.  -NMMMN:   :++-   `hMMMN:   `-/ohmh/   :h-                      
                     :dddddds/. .:oys+oMMMMN----------hMMMM::+ymdyo:.`-:/:.:oN.                     
                            ./shy+-  ./dMMMMyNoMhyMoMymMMMNy+:. ./shmmhsooo+/.                      
                                `:sdds/oMNMM-d N//N M:yMMMy-/syhy+:.                                
                                     -sNM-+syddmmmmddddh/MMd/.                                      
                                 `:ohmdoN/              `M/+ydo-                                    
                        -+oo+oshmdy+:-/smm+-.``  ``..-/ohdmy/`-shs:`                                
                       :Mo-://:/oyddho:. `:+shhdddddhyo:   -oddo-.+yyo++`                           
                       `dM/  /mho:`                           .omNs`  `s.                           
                         odydh.                                  -yNo-m`                            
                           .`                                       -/.                             
                                                                           
                                                                           """
    print mySkull      




def printhotdog ():
    myHotdog = """

                                                                      
                                                       `......`       
                                                 `.-::/:::::::/:      
                                           `..-:::::::://oososo+/.    
                                    `..--::::////+ssyyhhhhhhhhsoo++:  
       ``.....................---::::::/++yhhhhhhhhhhyyyyyyys/-/s++o+ 
   .-:::::::::::///:::::///+++++osyyyhhhhhhhhhhhhhyo:---:://////++ooo.
 `/////osssyyyyhhhhyyyyhhhhhhhhhhhhhhhhhhysooooo+/:::///:::::::::::os.
 /+hhhhhhhhhhhhhhhhhhhhhhhhhhhhyysssyyso:-.--::://::::::::::::::::::+ 
`oohhysooyyhhhys+/:::/+osssso/:-----:::::///::::::::::::::::::::::::+ 
+o+os+++::/+++/////////////////////:::::::::::::::::::::::::::::::::/ 
s++++oo+/::::::::::::::::::::::::::::::::::::::::::::::::::::::::::/` 
:o+++s/:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::-`  
 -+++o::::::::::::::::::::::::::::::::::::::::::::::::::::::::::-`    
   .-o:::::::::::::::::::::::::::::::::::::::::::::::::::::::-.       
     -/::::::::::::::::::::::::::::::::::::::::::::::::::-.`          
      .:::::::::::::::::::::::::::::::::::::::::::--..`               
        `.-:::::::::::::::::::::::::::::::--...`                      
             `....------------.....```                                
                                                                      
                                                  """             


def printcat ():
    myCat = """


      ( \
       \ \
       / /                |\\
      / /     .-`````-.   / ^`-.
      \ \    /         \_/  {|} `o
       \ \  /   .---.   \\ _  ,--'
        \ \/   /     \,  \( `^^^
         \   \/\      (\  )
          \   ) \     ) \ \
           ) /__ \__  ) (\ \___
          (___)))__))(__))(__))) """



    print myCat

def printavocado ():
    myAvocado = """

     -.-/+////-/++.`...://++/-:+:o+yhhy+-          
/osyhosNhhomoyhhyNmmNMNNNmmNMMMNMdNMNMMNNd+.      
Nos+oddsy+-dhshyhhho/:-:-..:/ohNMNNMMMNNdy+m.     
mhhhhhomm+.+hdmmdh-..``:-```.``+odMMMMNdd+/+h.    
hmdo//ydo-/hNNNNm/..-:/o:oyyyo+/:+hmMMMNMNs/om    
mdmyoy-./ms//:/:--smNNMNoydmNMMMNMMMMMMMMNhyyM-   
ohddos-yMdo--.-+hdNMMNMy.....-/+sdNMMMMMMNh/dMo   
:dhhoymh:``-sshMmy++dy:-:+:://::--/oNMMMMMmsMMd   
.hhm+h+.-/::+mmssh+oyyhyyysymMmmmNmmmNMMMMMMMMm   
.ym+d/:.--:sNmmdhhNMNMMN+`.`.-..-+oymMNMMMMMMM+   
`o+oo..:/:hNhhsmmmmNNNdo---/:---:--+:sdM   d    
`--..`..smyhydmMMMdm+.-:ohhdhydhdmdddddNMMMMMo    
``````-ddo+dNMMhmmmhhyhhddy:----.-.:/smMMMMMMN.   
 `-`..ss+hmdds/+ohNdso//-//...-....-.-:smNMMMMd`  
.:-h-:omds/:/-/omMNho:/+/-+.:+ooos:-::::/ymMMMMs  
`.o/-/y+:-/:-:hMNh-.-.::s+ymNMMMmmmmssdmMMMMMMMM- 
 -m///---o--:sd+..````-+mddMms+:/shyydNNMMMMMNMMo 
 `++-/ooyhdhh+-/-.`-`shmydhs///+yo+/-++dNMMMMMMMy 
  hNdddMMN++:..:-`.-ymmdhoymh+/ohhyyhydNMMmNMMMMy 
  /+yh//m+---::--/oyhmds///odyshmMNNNNmMNNMMMMMMo 
  /sdNs:::.:/ohmddo+s:/-/-/ydNMMNdshso/ydNMMMMMm` 
  ++dhs+ymmmNNdmo::./-./ymmNNdyys//++//dMMMMMMd.  
  :+ymymmdsh/oNs/:/..:ohmdhy+o/:+--:odNMMMd+dy    
  ..oos/hyyhsddNhosdNMNdo//::+:--odMMMMMMmhm/     
  `//+ysmyddmdmmNMMMMdd//:/::oymMMMMMsdNhs/       
  `+mNmmddddmMmddNMNNmdhsoymMMMMNdyyso-`          
   `.://+oyo:/o++///:/:-:--:/:.`      """

def printkindbar ():
    myKindbar = """


NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNdoo+:`             
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNd/:oN/             
NNNNNNNmhhhmNdhhdmhhhmmhhhNmhhhmdhhhhhhdmNNNNdhhhhhhdNNNNmhhhdNNNdhhhhhhdNNNNNNNNd` -ddo`           
NNNNNNNd   hm-  /d   hd   sh   h+       .mNNN/       -NNNy   -NNN/       -NNNNNNNd`   -dd/-..----.  
NNNNNNNd   hy  `dd   hd   .y   h+  .yo   mNNN/  -ho  `NNN:    dNN/  -ho  `mNNNNNNd`    `:osssssssdd.
NNNNNNNd   h-  +Nd   hd    :   h+  -Nh   mNNN/  :Ny  `NNd`    +NN/  :Ny  `mNNNNNNd`              -No
NNNNNNNd   -   mNd   hd        h+  -Nh   mNNN/  ./-  /NNo  /  .mN/  :Ny  `mNNNNNNd`              `dd
NNNNNNNd   :   sNd   hd        h+  -Nh   mNNN/  ./-  `mN.  y-  yN/   ``  `mNNNNNNd`               hm
NNNNNNNd   h:  -md   hd  `/    h+  -Nh   mNNN/  :Ny  `dh   s:  /N/  .-  -hNNNNNNNd`               yN
NNNNNNNd   hy   yd   hd  `d`   h+  .o+   mNNN/  -o/  `d+       `m/  :h   yNNNNNNNd`               hm
NNNNNNNd   hm.  :d   hd  `m+   h+      `/NNNN/      `/m`  omm`  s/  :N+  .mNNNNNNd`              `mh
NNNNNNNNmmmNNNmmNNmmmNNmmNNNmmmNNmmmmmmNNNNNNNmmmmmmNNNmmmNNNNmmNNmmNNNmmmNNNNNNNd````...``      :N+
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNd+hhyyyyhhhddddddh`
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNd`                 
"""

    print myKindbar

def printcockroach ():
    myCockroach = """


                  ``..--:/:                       
                                    .s.                     
                                      s                     
                                      ::                    
                                      .o                    
                      `o              .s                    
                      y-              /o                    
                     /s               s/                    
                     h:              `m.                    
                     d+        .-:::::o  `.-:/::::::-:::-`  
                     hd`  `-+yddmNNNmmh::o+:..``       `.// 
                     +Nh:sdmNNNNNNNNNNNm/                 ./
      ``.--:////::--.-hdmNNNNNNNNNNNNNNNy                  /
     `..----:::/+osyyhhyooyhmNNNNNNNNNNNs                  -
              `.-::///+shddyoydNNNNNNNNN:                  `
          .:ohdmmNNNNNmdysshmdssmNNNNNNs                    
       `:syhs++yyyssyhmNNNmhoymdoyNNNNh`                    
     `/so-.  -dNNNNmdysshmNNNh+hmsomNm-`      `.:/-         
   `:+-`    -mNNNNNNNNNmyohNNNm/sNs+dmhyso+++++/-`          
  .:.      .mNNNNNNNNNNNNmsomNNm.sNo..----..`               
 .`        hNNNNNNNNNNNNNNNh/mNN+`ym-                       
          :NNNNNNNNNNNNNNNNNsoNNs .ms                       
          oNNNNNNNNNNNNNNNNNm/NN+  om                       
          +NNNNNNNNNNNNNNNds-/Nm.  .N.                      
          `hNNNNNNNNNNmds:`  yN/    d-                      
           `/ydmmmdyo/-     :m+     y.                      
                `          -d:      +                       
                          :s.       `                       
                        `/:                                 
                       .-                  """

    print myCockroach


def eattingRat ():
    eatingrat = """
         ____
        |    |
        |____|
       _|____|_                                          _
        /  ee`.     
      .<     __O  -----> " Great! You are Master Of Pizza finder "
     /\ \.-.' \    
    J  `.|`.\/ \             
    | |_.|  | | |
     \__.'`.|-' /
     L   /|o`--'\ 
     |  /\/\/\   \           
     J /      `.__\
     |/         /  \     
      \\      .'`.  `.                                            .'
    ____)_/\_(____`.  `-._______________________________________.'/
   (___._/  \_.___) `-.________________________________________.-'
"""

    print eatingrat


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def startstory():
  print "PROLOGUE\n\n"    
  print "IT AINT EASY BEING THE INFAMOUS PIZZA RAT." 
  print "You humans have marginalized and reduced me to a pathetic MEME.\n\n"
  print "I LOVE PIZZA! Is that so wrong? You don't see me posting images of you, mocking you when you hungrily scarf down $12 avocado toast and $6 sustainable shade grown coffee.\n"
  print "Perhaps if you step into my dirty furry rodent paws, you will see the struggles I got through in search of that perfect discarded slice.\n"
  print "READY TO PLAY?\n"
  
  subwayFX.play()
  userInput = getInput("Where you want to go? \n\n1.Downtown  \n\n2.Uptown\n\n")


  #------------uptown-------------------------------------------------------------------------------------


  if (userInput == "2"):
      cls()
      print ("You chose uptown")
      printcat()
      print ("you see cat!")
      catFX.play()

      userInput1 = getInput("How you are going to attack the cat? \n\n1.Bite\n2.Trangle\n\n")


      if (userInput1 == "1"):
          print ("Ohhhh!!!!!!! Yeaa....... Cat ran away")
      
      
      elif (userInput1 == "2"):
          print ("cat dies")


      else:
          print ("sorry try again")   

          print ("you reached uptown!\n")

      
      userInput3 = getInput("\nChoose one discarded snack: \n\n1.Bagel\n2.Hot dog\n\n")


      if (userInput3 == "1"):
          cls()
          printbagel()
          print ("not bad but wish it was pizza")
      
      
      elif (userInput3 == "2"):
          printhotdog()
          print ("pretty good but wish it was pizza")


      else:
          print ("sorry try again")   




      userInput4 = getInput("Uptown is a pizza dead zone. Lets go south! \n\n1.Yes\n2.No\n\n")


  #------------head south---------------------------------------------------------------------



      if (userInput4 == "1"):
          cls()
          print ("Great! There are 3 subway lines going south.  Which one wil it be?  Only one has pizza.  The other two are dangerous.\n")
      
      
      elif (userInput4 == "2"):
          print ("You quitter. No pizza for you!")

      


      userInput5 = getInput("choose one subway line: \n\n(a).ACE\n(b).123\n(c).456\n\n")


      if (userInput5 == "a"):
          cls()
          printskull()
          print ("Bad choice! Poison everywhere.  Rest In Peace!")
          gameoverFX.play()
          userInput9 = getInput("Want to play again? \n\n1.Yes \n2.No\n\n")
          if (userInput9 == "1"):
             startstory()
          else:
           return()


      elif (userInput5 == "b"):
          cls()
          print ("Tough luck! Oncoming train maims you!")
          subwayFX.play()
          time.sleep(5)
          print ("Nice try. Play again? yes or no\n")


      elif (userInput5 == "c"):
          cls()
          print ("Congratulations! Pizza heaven in Nolita!") 
          printpizza()
          eattingRat ()
          endcreditsFX.play()
          time.sleep(10)


      else:
          print ("sorry try again")   


  #------------head downtown---------------------------------------------------------------------

      
      
  elif (userInput == "1"):
      print ("you chose downtown")


      cls()
      print ("You see Giant Cockroach")
      printcockroach()
      cockroachFX.play()
      time.sleep(3)


      userInput6 = getInput("How you are going to attack? \n\n1.Squash  \n2.Run\n\n")


      if (userInput6 == "1"):
          cls()
          print ("\nThat was not pleasant. Who knows if it is even dead? Those things can survive anything. Stay focused. PIZZA!\n")
      
      
      elif (userInput6 == "2"):
          print ("Now I know how humans feel about me. Yikes.")


      else:
          print ("sorry try again")   


          print ("You reached downtown!\n")

      snackFX.play()
      userInput7 = getInput("choose one discarded snack: \n\n1.Avocado toast \n2.Kind Bar\n\n")



      if (userInput7 == "1"):
          printavocado()
          print ("Good but overrated and too healthy! Plus, its not pizza!")
      
      
      elif (userInput7 == "2"):
          cls()
          printkindbar()
          print ("Cured my rumbling tummy but its not quite pizza!")


      else:
          print ("sorry try again")

      cls()
      print ("In the tunnel...")
      printrat()
      ratFX.play()

      userInput8 = getInput(" You run into your buddy Bagel Rat.\n He tells you there's good p's Lombardi's, Rubirosa,\n Prince Street Pizza plus school just started and lots of drunk students out tonnight.\n  Do you want to head to Spring St?\n\n1.Yes \n2.No?\n\n")
        
      

      if (userInput8 == "1"):
          cls()
          print ("Pizza Heaven! So much pizza so little time!")
          printpizza()
          eattingRat ()
          endcreditsFX.play()
          time.sleep(10)
      
      
      elif (userInput7 == "2"):
          print ("GAME OVER. I guess you don't really want pizza!")
          playFile(gameoverSound)
          time.sleep(5)        


def intro():
  printtitle()
  printintro()



def main():
  intro()
      
main()
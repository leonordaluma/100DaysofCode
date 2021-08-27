print('''  
***********************************************
                c==o
              _/____\_
       _.,--'" ||^ || "`z._
      /_/^ ___\||  || _/o\ "`-._
    _/  ]. L_| || .||  \_/_  . _`--._
   /_~7  _ . " ||. || /] \ ]. (_)  . "`--.
  |__7~.(_)_ []|+--+|/____T_____________L|
  |__|  _^(_) /^   __\____ _   _|
  |__| (_){_) J ]K{__ L___ _   _]
  |__| . _(_) \v     /__________|________
  l__l_ (_). []|+-+-<\^   L  . _   - ---L|
   \__\    __. ||^l  \Y] /_]  (_) .  _,--'
     \~_]  L_| || .\ .\\/~.    _,--'"
      \_\ . __/||  |\  \`-+-<'"
        "`---._|J__L|X o~~|[\\      
               \____/ \___|[// 
                `--'   `--+-'
***********************************************
''')
print("Welcome! You're in the Millennium Falcon.")
print("Your mission is to find Han Solo. Keep a sharp eye out for the Imperial Military. ")

direction = input('Search the galaxy. Where do you start? Type "Tatooine" or "Corellia"\n')
if direction == "Tatooine" or direction == "tatooine":
    search = input('''There's no one here. Type "search" to continue searching. Type "wait" to wait for something  to happen.\n''')
    if search == "Wait" or search == "wait":
        door = input("After minutes of waiting you stumbled upon 3 doors. One red, one yellow and blue. Which door do you open? Type the color\n")
        if door == "Yellow" or door == "yellow":
            print("You found Han Solo! You win.")
        elif door == "Blue" or door == "blue":
            print("Meesa Jarjar Binks! Game over!")
        elif door == "Red" or door == "red":
            print("Hello There :) General Kenobi??? Game Over!")
        else:
            print("I'm afraid you're not following the rules. Get out!")
    elif search == "Search" or search == "search":
        print("The search is over. This is not a big ship. Game over!")
    else:
        print("That's not how the game works. Game over!")
else:
    print("Why are you going out of the ship? Game over!")

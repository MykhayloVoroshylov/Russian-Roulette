from random import randint
import time

# Global variables
score = 0
dishonorable = False  # Track dishonorable status
reason = "nothing"
deserts = 0

def computer_turn(deadly_number, count):
    global score, dishonorable, reason, deserts
    print("Computer's turn...")
    print("Putting muzzle to head...")
    time.sleep(2)
    print("Taking risks...")
    time.sleep(1)
    print("Pulling trigger...\n")
    count += 1

    if count == deadly_number:
        print("BANG! Computer is eliminated.")
        score += 1  # Add score when the player wins the round
        print("Your current score: ", score)
        return "computer", count, False
    else:
        print("CLICK! Your turn.")
        if deadly_number == 6 and count == 5:
            # Final chamber scenario
            print("You had a chance to desert, yet the drum reached the last chamber, and it has a bullet.")
            print("Make your choice:")
            print("1. Shoot the computer (Dishonorable, but you survive).")
            print("2. Take the shot yourself (Honorable, but you are dead).")
            
            # Single choice prompt
            choice = input("Enter 1 to shoot the computer, or 2 to take the shot yourself: ")

            if choice == "1":
                print("You chose dishonor by shooting the computer.")
                print("You survive, but you are marked as Dishonorable. Redemption will be required.")
                reason = "murder"
                score += 1
                dishonorable = True
                return "player", count, False  # End game for this round
            elif choice == "2":
                print("You chose to take the honorable path. Prepare for the final shot...")
                print("Rolling the drum...")
                time.sleep(2)
                print("BANG! You are eliminated. An honorable end.")
                return "player", count, False  # Player loses
            else:
                print("Invalid choice. You hesitated, and the computer shoots you out of impatience!")
                return "player", count, False  # Player loses due to invalid choice
        else:
            # Default choice for normal game play
            choice = input("Perhaps you don't want to lose. Do you want to stay alive and desert? (Yes/No): ").lower()
            if choice == "yes":
                print("You deserted and are alive! However, for unsportsmanlike behavior, your score is set to 0.")
                desert()  # Track desertions
                score = 0
                return "player", count, False
            elif choice == "no":
                return "player", count, True
            else:
                print("Invalid choice. The computer doesn't understand gibberish and eliminates you.")
                return "player", count, False
                
def desert():
    global deserts, dishonorable, reason, score
    deserts += 1  # Increment desert count
    if deserts == 3:
        print("You have deserted 3 times! You are now dishonored!")
        reason = "desertion"
        dishonorable = True  # Mark as dishonorable after 3 desertions
        print("You are now dishonorable for desertion. Redemption will be required.")
    else:
        print(f"You have deserted {deserts} time(s). You better stop it before it's too late.")
    score = 0  # Reset score when the player deserts


def player_turn(deadly_number, count):
    global score
    print("Your turn...")
    print("Putting muzzle to head...")
    time.sleep(2)
    print("Taking risks...")
    time.sleep(1)
    print("Pulling trigger...\n")
    count += 1
    if count == deadly_number:
        print("BANG! You are eliminated.")
        print(f"Your final score: {score}")  # Show score at the end if the player loses
        score = 0  # Reset score when the player dies
        return "player", count, False
    else:
        print("CLICK! Computer's turn.")  # <-- This can be the only place the "Computer's turn" message is printed.
        score += 1  # Add score when the player survives the round
        return "computer", count, True


def dishonorable_round(deadly_number, count):
    print("It's time to play again player, I mean Bastard. This time, it would be harder to survive than usually.")
    response2 = input(("Unlike you, coward, I have conscience and honesty, without saying anything about honor.\nTherefore I give you the chance, before the round begins.\n Do you want to redeem yourself, and have a fair game? (Yes/No)")).lower()
    if response2 == "yes":
        print("Ok, it's a wise choice.")
        seek_forgiveness(dishonorable, score)
    elif response2 == "no":
        print("I know there are dumb people, but you... you weren't even in line when God was giving out brains. Your choice...")
        # Pass deadly_number and count to dishonorable_game_loop
        dishonorable_game_loop(deadly_number, count)


def seek_forgiveness(dishonorable, score):
    if dishonorable:
        print("You are marked as Dishonorable. Redemption is possible, but it will not be easy.")
        print("You must complete a forgiveness task to erase your dishonor.")
        
        while True:
            print("Choose your path to forgiveness:")
            print("1. Survive 5 honorable turns.")
            print("2. Take the Forgiveness Challenge.")
            print("3. Face execution.")
            choice = input("Enter 1, 2, or 3: ")

            if choice == "1":
                print("Survive 5 turns honorably. Each turn, the drum is rolled.")
                honor_turns = 0
                deadly_number = randint(1, 6)

                while honor_turns < 5:
                    print("Rolling Drum")
                    turn, count, game_on = player_turn(deadly_number, 0)

                    if not game_on:
                        print("You failed to meet the forgiveness criteria. Try again later.")
                        return dishonorable
                    
                    honor_turns += 1  # Increment after player's turn
                    
                    if honor_turns < 5:  # Only proceed to computer's turn if player survived
                        print("Rolling Drum")
                        turn, count, game_on = computer_turn(deadly_number, 0)

                        if not game_on:
                            print("You failed to meet the forgiveness criteria. Try again later.")
                            return dishonorable

                print("Your bravery has redeemed you. You are forgiven!")
                return False

            elif choice == "2":
                print("You must face the Forgiveness Challenge.")
                print("Spin the drum and take two shots in one turn. Or desert and be executed immediately.")
                response = input("What is your choice? Execution/Challenge: ").lower()
                if response == "challenge":
                    for i in range(2):  # Two shots
                        print("Drum rolling...")
                        time.sleep(2)
                        deadly_number = randint(1, 6)
                        print("Pulling trigger...")
                        time.sleep(2)
                        count = randint(1, 6)

                        if count == deadly_number:
                            print("BANG! You lost during the Forgiveness Challenge.")
                            return dishonorable
                        else:
                            print(f"CLICK! You survived shot {i + 1}")

                    # After the loop ends, the player has survived both shots
                    print("Incredible bravery! You are forgiven!")
                    return False
                else:
                    print("Execution it is... Goodbye, dishonorable one!")
                    return dishonorable
            
            else:
                print("Execution it is...")
                time.sleep(3)
                print("SQUAD!!!")
                time.sleep(1)
                print("AIM!!!")
                time.sleep(1)
                print("FIRE!!!!")
                print("You were executed for the unsportsmanlike behaviour of", reason)
                print(f"Your final score is: {score}")
                score = 0  # Reset score after execution
                return False


    print("You are not marked as Dishonorable. Play honorably!")
    return dishonorable


def dishonorable_game_loop(deadly_number, count):
    global score, dishonorable
    bullets_in_chamber = 2  # Player has 2 bullets in the chamber when dishonorable
    while True:
        print(f"\nYou have {bullets_in_chamber} bullets left.")
        print("Rolling the drum...")

        # Increment count and check for a bullet in the chamber
        count += 1
        if count == deadly_number:
            print("BANG! You are eliminated. Perhaps it would have been better to not be such a weak coward.")
            print(f"Your final score: {score}")
            score = 0  # Reset score after death
            return "player", count, False  # End game if the player is eliminated
        else:
            print("CLICK! You survived this shot. Wonder how you did it.")
            bullets_in_chamber -= 1  # Reduce bullets left

            if bullets_in_chamber == 0:  # After 2 shots, the player must choose to desert or proceed
                print("You have 0 bullets left!")
                choice = input("Do you want to seek redemption or continue playing dishonorably? (Redeem/Continue): ").lower()

                if choice == "redeem":
                    print("Wise choice")
                    seek_forgiveness()
                elif choice == "continue":
                    print("You continue dishonorably... Be careful!")
                    bullets_in_chamber = 2  # Refill bullets
                else:
                    print("Invalid choice. No one survives when they hesitate.")
                    return "player", count, False



def game():
    global score, dishonorable
    while True:
        answer = input("Would you like to play? (Yes/No): ").lower()
        if answer == "yes":
            score = 0  # Reset score for a new game
            game_on = True
            deadly_number = randint(1, 6)
            count = 0
            turn = "player" if randint(1, 2) == 1 else "computer"

            print("Inserting bullet...")
            time.sleep(2)
            print("Rolling the drum...")
            time.sleep(2)

            while game_on:
                if turn == "player":
                    if dishonorable:  # Trigger dishonorable round if player is dishonorable
                        dishonorable_round(deadly_number, count)
                    else:
                        turn, count, game_on = player_turn(deadly_number, count)
                elif turn == "computer":
                    turn, count, game_on = computer_turn(deadly_number, count)

                # Check dishonorable state after each round
                if not game_on and dishonorable:
                    print("\nYou are marked as Dishonorable.")
                    redeem_choice = input("Would you like to seek redemption? (Yes/No): ").lower()
                    if redeem_choice == "yes":
                        dishonorable = seek_forgiveness(dishonorable, score)
                        if not dishonorable:
                            print("You are redeemed! Your honor is restored and you can play normally.")
                            response = input("Do you want to play again, and continue with your score? (Yes/No): ").lower()
                            if response == "yes":
                                game_on = True  # Allow the player to rejoin the game
                            elif response == "no":
                                game_on = False
                            else:
                                while response not in ["yes", "no"]:
                                    print("Stop your gibberish, or I may rethink forgiving you.")
                                    response = input("Do you want to play again, and continue with your score? (Yes/No): ").lower()
                    else:
                        print("You chose not to seek redemption. Very bad choice of yours")
                        dishonorable_round(deadly_number, count)    
                        break  # Exit current game loop

            print(f"Game over. Your final score is: {score}")
        elif answer == "no":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please type 'Yes' or 'No'.")


print("Let's play Russian roulette!")
print("There are 6 slots for a bullet, 1 is loaded. Try not to be shot by the bullet. Good Luck!")
game()

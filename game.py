import sys
import random
import file_handling

def create_life_score():
    "This function will create random life score"
    return random.randint(1, 50)

def create_numbers(attempt):
    "This function will create random numbers for play"
    if 1 <= attempt <= 5:
        return [random.randint(15, 100) for _ in range (5)]
    elif 6 <= attempt <= 10:
        return [random.randint(250, 2000) for _ in range (5)]
    elif 11 <= attempt <= 15:
        return [random.randint(3000, 10000) for _ in range (5)]
    else:
        return [random.randint(20000, 100000) for _ in range (5)]
    
    
def game_status(player_name, attempt, life_score, numbers):
    "This function will show your game status"
    print ("")
    print ("*** Game status ***")
    print (f"Player name : {player_name}\n")
    print (f"Total attempts : {attempt}\n")
    print (f"Final life score : {life_score}\n")
    if attempt == 20:
        print (f"{player_name} has successfully completed 20 attempts!")
    else:
        print (f"{player_name} was defeated!!!")


def game_play():
    "This function for game start and"
    if len(sys.argv) > 1:
        player_name = sys.argv[1]
    else:
        player_name = input ("Enter your name : ")

    life_score = create_life_score()
    attempts = 0
    end_game_stats = []

    while attempts < 20:
        attempts += 1
        numbers = create_numbers(attempts)

        print (f"\nAttempt : {attempts}")
        print (f"{player_name}'s life score is : {life_score}")
        print (" ".join(map(str, numbers)))

        try:
            selected_number = int(input("Select a number to fight : "))
        except ValueError:
            print ("Invalid input! Game over.")
            game_status(player_name, attempts, life_score, numbers)
            end_game_stats.append(attempts, numbers, "Invalid Input", "LOST", life_score)
            file_handling.game_save(player_name, attempts, end_game_stats)
            break

        if selected_number not in numbers:
            print ("No such enemy! Game over.")
            game_status(player_name, attempts, life_score, numbers)
            end_game_stats.append((attempts, numbers, selected_number, "LOST", life_score))
            file_handling.game_save(player_name, attempts, end_game_stats)
            break

        if selected_number <= life_score:
            life_score += selected_number
            print (f"{player_name} killed {selected_number}")
        
        else:
            print (f"{selected_number} defeated {player_name}! Game over.")
            game_status(player_name, attempts, life_score, numbers)
            end_game_stats.append((attempts, numbers, selected_number, "LOST", life_score))
            file_handling.game_save(player_name, attempts, end_game_stats)
            break

        end_game_stats.append ((attempts, numbers,selected_number, "WON", life_score))

        if attempts == 20:
            game_status(player_name, attempts, life_score, numbers)
            file_handling.game_save(player_name, attempts, end_game_stats)
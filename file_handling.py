import datetime
import random

def game_save(player_name, attempts, end_game_stats):
    "This function will save your game status"
    current_date = datetime.datetime.now().strftime("%Y_%m_%d")
    current_time = datetime.datetime.now().strftime("%H_%M_%S")
    random_number = random.randint(0, 9999)
    file_name = f"{current_date}_{current_time}_{random_number:04d}.txt"

    with open(file_name, "w") as file:
        for attempt, enemies, user_input, status, life_score in end_game_stats:
            enemies_str = " ".join(map(str, enemies))
            file.write (f"Total attempts: {attempt}\n")
            file.write (f"Presented Enemies : {enemies_str}\n")
            file.write(f"User input : {user_input}\n")
            file.write(f"Status : {status}\n")
            file.write(f"Life score : {life_score}\n\n")
        file.write(f"End Game Status : {end_game_stats}\n")
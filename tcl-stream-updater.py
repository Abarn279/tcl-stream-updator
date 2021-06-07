import os
import math

def write_line(path, line):
    with open(path, 'w') as f:
        f.write(line)

def create_if_not_exists(paths):
    for path in paths:
        if not os.path.exists(path):
            open(path, 'w').close()

wd = os.getcwd()

# File paths
home_score_path = f"{wd}\\Text\\homescore.txt" # Home and away. used for title screen
away_score_path = f"{wd}\\Text\\awayscore.txt" # --
blue_score_path = f"{wd}\\Text\\bluescore.txt" # Red and blue. used for in-game
red_score_path = f"{wd}\\Text\\redscore.txt"   # --
stream_title_path = f"{wd}\\Text\\streamtitle.txt"
caster_1_path = f"{wd}\\Text\\caster1.txt"
caster_2_path = f"{wd}\\Text\\caster2.txt"

# Create all the files if they don't exist
create_if_not_exists([home_score_path, away_score_path, blue_score_path, red_score_path, stream_title_path, caster_1_path, caster_2_path])

# Scores, updated as we go
home_current_score = 0
away_current_score = 0

# Input from streamer
stream_title = input("Stream title? (eg: TCL Quarterfinals Day 1): ")
home_name = input("What is the home team's 3 letter name?: ")
away_name = input("What is the away team's 3 letter name?: ")
bestof = int(input("Best of? (odd number): "))
caster1 = input("Caster 1?: ")
caster2 = input("Caster 2?: ")

wins_needed = math.ceil(bestof / 2)

# Check if teams are swapped sides (every other match)
teams_swapped = lambda blue: blue == away_name

# Arg checking
if bestof <= 0 or bestof % 2 != 1: 
    raise Exception("Best of must be odd and postive")

if len(home_name) != 3 and len(away_name) != 3:
    raise Exception("Names must be length 3")

# Get first blue-side
curr_blue = input(f"Who is blue team first game? ({home_name}, {away_name}): ")
if curr_blue not in [home_name, away_name]: 
    raise Exception("Bad input. Run script again.")

# Initial file writes (pre-match)
write_line(home_score_path, f"{home_name} - {home_current_score}")
write_line(away_score_path, f"{away_name} - {away_current_score}")
write_line(stream_title_path, stream_title)
write_line(caster_1_path, caster1)
write_line(caster_2_path, caster2)

if not teams_swapped(curr_blue):
    write_line(blue_score_path, f"{home_name} - {home_current_score}")
    write_line(red_score_path, f"{away_name} - {away_current_score}")
else:
    write_line(red_score_path, f"{home_name} - {home_current_score}")
    write_line(blue_score_path, f"{away_name} - {away_current_score}")

print("\nOkay, go stream now. Come back and update me once games have completed.")

while True:
    if home_current_score >= wins_needed or away_current_score >= wins_needed:
        print("\n Match over!")
        break

    # Get inputs, don't do anything until they're verified
    winner = input(f"Who won the last game? ({home_name}, {away_name}): ")
    if winner not in [home_name, away_name]: 
        print("Bad input. try again")
        continue

    curr_blue = input(f"Who is blue team this next game? ({home_name}, {away_name}): ")
    if curr_blue not in [home_name, away_name]: 
        print("Bad input. try again")
        continue

    if winner == home_name:
        home_current_score += 1
    else:
        away_current_score += 1

    print(f"Current score: {home_name}: {home_current_score}, {away_name}: {away_current_score}")

    write_line(home_score_path, f"{home_name} - {home_current_score}")
    write_line(away_score_path, f"{away_name} - {away_current_score}")

    if not teams_swapped(curr_blue):
        write_line(blue_score_path, f"{home_name} - {home_current_score}")
        write_line(red_score_path, f"{away_name} - {away_current_score}")
    else:
        write_line(red_score_path, f"{home_name} - {home_current_score}")
        write_line(blue_score_path, f"{away_name} - {away_current_score}")

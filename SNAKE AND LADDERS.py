
import random

# Snakes and Ladders positions
snakes = {13: 9, 25: 4, 29: 10, 33: 27, 42: 19, 64: 24, 70: 49, 84: 65, 95: 47, 99: 78}
ladders = {2: 23, 8: 14, 26: 35, 38: 44, 41: 60, 56: 77, 69: 90, 79: 81, 88: 94}

player = 0
computer = 0

def roll_dice():
    return random.randint(1, 6)

def move_player(position, dice):
    position += dice
    if position > 100:
        return position - dice  # cannot move beyond 100
    
    if position in snakes:
        print(f" Snake at {position} → down to {snakes[position]}")
        return snakes[position]
    elif position in ladders:
        print(f" Ladder at {position} → up to {ladders[position]}")
        return ladders[position]
    return position

while True:
    input("\n Your turn! Press Enter to roll...")
    dice = roll_dice()
    print(f"You rolled: {dice}")
    player = move_player(player, dice)
    print(f"➡ Your position: {player}")

    if player == 100:
        print("\n YOU WON!")
        break

    print("\nComputer rolling...")
    dice = roll_dice()
    print(f"Computer rolled: {dice}")
    computer = move_player(computer, dice)
    print(f"➡ Computer position: {computer}")

    if computer == 100:
        print("\n Computer WON!")
        break
    
    
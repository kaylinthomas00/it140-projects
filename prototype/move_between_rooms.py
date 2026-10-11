"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}
# Set the player's starting room
current_room = 'Great Hall'

# Gameplay loop
while True:
    # 1. Display the current room
    print(f"\nYou are in the {current_room}.")
    
    # 2. Prompt for a movement command or 'exit'
    command = input("Enter your move (or 'exit' to quit): ").strip().lower()
    
    # 3. Branch for exit, valid move, or invalid input
    if command == 'exit':
        print("Thanks for playing!")
        break
    
    # Check if the command is a valid direction for the current room
    elif command in rooms[current_room]:
        # 4. Update the room only after a valid movement command
        current_room = rooms[current_room][command]
    else:
        # Input validation error message
        print("Invalid move! You can't go that way.")

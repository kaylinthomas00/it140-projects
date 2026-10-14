# Kaylin L Thomas
# IT-140 Project Two: Text-Based Adventure Game

def show_instructions():
    """Display the game objective and available commands."""
    print("Welcome to the Text Adventure Game!")
    print("Collect all items to win, or enter the villain's room and lose.")
    print("Move commands: go north, go south, go east, go west")
    print("Add to Inventory: get 'item name'")
    print("--------------------------------------------------")

def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    print(f"\nYou are in the {current_room}")
    print(f"Inventory: {inventory}")
    if 'item' in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")
    print("-" * 50)

def main():
    """Run the main gameplay loop."""
    # Dictionary linking rooms to one another and their items
    rooms = {
        'Start Room': {'north': 'Hallway', 'east': 'Library'},
        'Hallway': {'south': 'Start Room', 'north': 'Vault', 'item': 'Key'},
        'Library': {'west': 'Start Room', 'east': 'Laboratory', 'item': 'Scroll'},
        'Laboratory': {'west': 'Library', 'item': 'Potion'},
        'Vault': {'south': 'Hallway', 'item': 'Villain'}  # Villain room
    }
    
    current_room = 'Start Room'
    inventory = []
    total_items = 3
    
    show_instructions()
    
    # Gameplay loop
    while True:
        show_status(current_room, inventory, rooms)
        
        command = input("Enter your move: ").strip().lower()
        command_words = command.split()
        
        if not command_words:
            print("Invalid command. Try again.")
            continue
            
        action = command_words[0]
        
        if action == 'go':
            if len(command_words) > 1:
                direction = command_words[1]
                if direction in rooms[current_room]:
                    current_room = rooms[current_room][direction]
                else:
                    print("You can't go that way!")
            else:
                print("Specify a direction (north, south, east, west).")
                
        elif action == 'get':
            if len(command_words) > 1:
                item_name = " ".join(command_words[1:]).title()
                if 'item' in rooms[current_room] and rooms[current_room]['item'].lower() == item_name.lower():
                    inventory.append(rooms[current_room]['item'])
                    print(f"Picked up {rooms[current_room]['item']}!")
                    del rooms[current_room]['item']
                else:
                    print(f"Can't get {item_name}!")
            else:
                print("Specify an item to get.")
        else:
            print("Invalid command. Use 'go [direction]' or 'get [item]'.")
            
        # Check for lose or win condition if entering the villain room
        if 'item' in rooms[current_room] and rooms[current_room]['item'] == 'Villain':
            if len(inventory) < total_items:
                print("\nNOM NOM...GAME OVER!")
                print("You encountered the villain before collecting all items.")
                print("Thanks for playing the game. Hope you enjoyed it.")
                break
            else:
                print("\nCongratulations! You collected all items and defeated the villain!")
                print("Thanks for playing the game. Hope you enjoyed it.")
                break
                
        if len(inventory) == total_items:
            if 'item' in rooms[current_room] and rooms[current_room]['item'] == 'Villain':
                print("\nCongratulations! You collected all items and defeated the villain!")
                print("Thanks for playing the game. Hope you enjoyed it.")
                break

if __name__ == "__main__":
    main()

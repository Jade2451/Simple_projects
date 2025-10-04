import time

def play_adventure():
    """
    Main function to run the text-based adventure game.
    """

    # --- Game Data ---
    game_map = {
        'start': {
            'description': "You are in a dark cave. There is a path to the north and a path to the east.",
            'choices': {'north': 'troll_bridge', 'east': 'quiet_stream'}
        },
        'troll_bridge': {
            'description': "You come to a rickety bridge guarded by a grumpy troll. 'Answer my riddle!' he grunts.",
            'choices': {'answer': 'treasure_room', 'flee': 'start'}
        },
        'quiet_stream': {
            'description': "You find a quiet, underground stream. The water looks fresh. A small key glints at the bottom.",
            'choices': {'take key': 'start', 'go back': 'start'}
        },
        'treasure_room': {
            'description': "You outsmarted the troll! You enter a room filled with glittering gold and jewels.",
            'choices': {'win': 'end'}
        },
        'end': {
            'description': "Congratulations! You found the treasure. Thanks for playing!",
            'choices': {}
        }
    }

    current_room = 'start'

    print("🧭 Welcome to the Tiny Text Adventure! 🧭")
    print("Type your choice from the options provided to navigate.\n")

    while True:
        room = game_map[current_room]
        print(room['description'])

        if current_room == 'end':
            break

        # --- Display Choices ---
        available_choices = room['choices'].keys()
        print(f"\nChoices: [ {' | '.join(available_choices)} ]")

        # --- Get Player Input ---
        player_choice = input("> ").lower()

        # --- Update Game State ---
        if player_choice in room['choices']:
            current_room = room['choices'][player_choice]
            print("\n" + "-"*30 + "\n")
            time.sleep(1) # Add a small delay for dramatic effect
        else:
            print("\nThat's not a valid choice. Try again.\n")
            time.sleep(1)

# --- Main execution block ---
if __name__ == "__main__":
    play_adventure()

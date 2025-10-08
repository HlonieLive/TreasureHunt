# Terminal Treasure Hunt - A Linux command game
import os
import sys
import subprocess
import time
import random

class TreasureHuntGame:
    """Main game class for the terminal treasure hunt"""

    def __init__(self):
        self.current_level = 1
        self.maximum_level = 8
        self.treasure_found = False
        self.setup_game_environment()

    def setup_game_environment(self):
        """Create the game environment with hidden files and directories"""

        # Game directory structure
        os.makedirs("treasure_hunt", exist_ok=True)
        os.chdir("treasure_hunt")

        # Level 1: Hidden file
        with open(".secret_note.txt", "w") as secret_file:
            secret_file.write(
                "The treasure is hidden where files are listed with details.\nNext clue: Use 'ls -l'"
            )

        # Level 2: Directory with files
        os.makedirs("forest", exist_ok=True)
        with open("forest/map.txt", "w") as map_file:
            map_file.write(
                "Follow the river to the cave.\nNext clue: Use 'cat forest/map.txt'"
            )
        with open("forest/river.txt", "w") as river_file:
            river_file.write(
                "The cave entrance is hidden behind waterfall.\nNext clue: Use 'grep cave forest/*.txt'"
            )

        # Level 3: Permissions challenge
        os.makedirs("cave", exist_ok=True)
        with open("cave/locked_chest.txt", "w") as chest_file:
            chest_file.write(
                "The key is hidden in the mountain.\nNext clue: Use 'chmod +x cave/locked_chest.txt' then './cave/locked_chest.txt'"
            )
        os.chmod("cave/locked_chest.txt", 0o644)  # Not executable initially

        # Level 4: Process challenge
        os.makedirs("mountain", exist_ok=True)
        with open("mountain/lookout.sh", "w") as lookout_script:
            lookout_script.write(
                '#!/bin/bash\necho "From the peak, I see the ocean!"\necho "Next clue: Use \'ps aux | grep lookout\'"\n'
            )
        os.chmod("mountain/lookout.sh", 0o755)

        # Level 5: File size challenge
        os.makedirs("ocean", exist_ok=True)
        # Create files of different sizes
        with open("ocean/small_pearl.txt", "w") as small_pearl:
            small_pearl.write("Small but precious.\n")
        with open("ocean/large_pearl.txt", "w") as large_pearl:
            large_pearl.write(
                "This is the largest pearl in the ocean!\nNext clue: Use 'ls -lS ocean/' to sort by size\n"
            )
        with open("ocean/tiny_pearl.txt", "w") as tiny_pearl:
            tiny_pearl.write("Tiny pearl.\n")

        # Level 6: Text manipulation
        os.makedirs("desert", exist_ok=True)
        with open("desert/sand_dunes.txt", "w") as sand_dunes:
            sand_dunes.write(
                "The oasis is NORTH of here.\nThe ruins are SOUTH.\nThe mountains are EAST.\nThe sea is WEST.\nNext clue: Use 'head -n 1 desert/sand_dunes.txt' to find the oasis\n"
            )

        # Level 7: Archiving challenge
        os.makedirs("ruins", exist_ok=True)
        with open("ruins/ancient_scroll.txt", "w") as ancient_scroll:
            ancient_scroll.write(
                "The final treasure is buried under X marks the spot!\n"
            )
        # Create a zip file
        subprocess.run(
            ["zip", "-r", "ruins/scrolls.zip", "ruins/ancient_scroll.txt"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        os.remove("ruins/ancient_scroll.txt")

        # Level 8: Final treasure
        with open("x_marks_the_spot.txt", "w") as treasure_file:
            treasure_file.write("CONGRATULATIONS! You found the treasure!\n")
            treasure_file.write("You've mastered these Linux commands:\n")
            treasure_file.write("- ls, ls -a, ls -l, ls -lS\n")
            treasure_file.write("- cat, grep\n")
            treasure_file.write("- chmod, ./\n")
            treasure_file.write("- ps, head\n")
            treasure_file.write("- zip, unzip\n")
            treasure_file.write("- pwd, cd\n")
            treasure_file.write("\nKeep practicing and exploring the terminal!\n")

    def clear_terminal_screen(self):
        """Clear the terminal screen"""
        os.system('clear' if os.name == 'posix' else 'cls')

    def display_introduction(self):
        """Display the game introduction"""
        self.clear_terminal_screen()
        print("=" * 60)
        print("    TERMINAL TREASURE HUNT: Linux Command Adventure")
        print("=" * 60)
        print("\nWelcome, adventurer! You seek the legendary terminal treasure.\nTo find it, you must solve challenges using terminal commands.\n\nInstructions:")
        print("\n- Read each clue carefully.\n- Execute the suggested command in your terminal.\n- Use the output to find the next clue.\n- Type 'hint' for a hint, 'quit' to exit\nYour journey begins now! Good luck!")
        print("=" * 60)
        input("\nPress Enter to start your adventure...")

    def run_game(self):
        """Main game loop"""
        self.display_introduction()
        print("Game structure ready.")


def main():
    """Main entry point for the treasure hunt game"""
    game_instance = TreasureHuntGame()
    game_instance.run_game()


if __name__ == "__main__":
    main()

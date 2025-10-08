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
        # Create game directory structure
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
        os.system("clear" if os.name == "posix" else "cls")

    def get_level_hint(self, level_number):
        """Return hints for each level"""
        hints_dictionary = {
            1: "Hidden files start with a dot (.) - try 'ls -a'",
            2: "You need to read the contents of a file - use 'cat'",
            3: "The file needs to be executable - use 'chmod +x'",
            4: "You need to find a running process - use 'ps aux | grep'",
            5: "Sort files by size - 'ls -lS' shows largest first",
            6: "Show only the first line of a file - 'head -n 1'",
            7: "You need to extract files from an archive - 'unzip'",
            8: "The treasure is in a file named 'x_marks_the_spot.txt'",
        }
        return hints_dictionary.get(level_number, "No hint available")

    def get_level_description(self, level_number):
        """Return description for each level"""
        descriptions_dictionary = {
            1: "You stand at the entrance of a mysterious directory. Something hidden catches your eye...",
            2: "You enter a dense forest. There might be a map hidden among the trees.",
            3: "You find a cave with a locked chest. The chest seems to need special handling.",
            4: "You climb a mountain. From the peak, you might spot something important.",
            5: "You reach the ocean shore. Pearls of different sizes are scattered around.",
            6: "You're lost in a vast desert. A message in the sand might guide you.",
            7: "You discover ancient ruins. A scroll is hidden in an archive.",
            8: "You've reached the final location! The treasure is buried here.",
        }
        return descriptions_dictionary.get(level_number, "Unknown level")

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

    def play_current_level(self):
        """Play the current level"""
        self.clear_terminal_screen()
        print(f"\n{'='*20} LEVEL {self.current_level} {'='*20}")
        print(self.get_level_description(self.current_level))
        print("\nCurrent directory:", os.getcwd())
        print("\nWhat command will you use? (Type 'hint' for help or 'quit' to exit)")

        while True:
            user_command = input("\n$ ").strip()

            if user_command.lower() == "quit":
                return False
            elif user_command.lower() == "hint":
                print(f"\nHint: {self.get_level_hint(self.current_level)}")
                continue
            elif user_command.lower() == "pwd":
                print(os.getcwd())
                continue
            elif user_command.startswith("cd "):
                try:
                    target_directory = user_command[3:].strip()
                    if target_directory == "..":
                        os.chdir("..")
                    else:
                        os.chdir(target_directory)
                    print(f"Changed directory to: {os.getcwd()}")
                except FileNotFoundError:
                    print("Directory not found")
                except NotADirectoryError:
                    print("Not a directory")
                continue
            elif user_command == "ls":
                print("\n".join(sorted(os.listdir("."))))
                continue
            elif user_command == "ls -a":
                items_list = sorted(
                    os.listdir("."),
                    key=lambda item_name: (item_name.startswith("."), item_name),
                )
                print("\n".join(items_list))
                continue
            elif user_command == "ls -l":
                try:
                    command_result = subprocess.run(
                        ["ls", "-l"], capture_output=True, text=True
                    )
                    print(command_result.stdout)
                except:
                    # Fallback for systems without ls command
                    for file_name in sorted(os.listdir(".")):
                        print(f"-rw-r--r-- 1 user group 0 Jan 1 00:00 {file_name}")
                continue

            # For other commands, try to execute them
            try:
                if user_command:  # Only execute non-empty commands
                    command_parts = user_command.split()
                    command_result = subprocess.run(
                        command_parts, capture_output=True, text=True, timeout=5
                    )
                    if command_result.returncode == 0:
                        print(command_result.stdout)
                    else:
                        print(command_result.stderr)
            except subprocess.TimeoutExpired:
                print("Command timed out")
            except FileNotFoundError:
                print("Command not found")
            except Exception as error_message:
                print(f"Command failed: {error_message}")

    def run_game(self):
        """Main game loop"""
        self.display_introduction()

        while self.current_level <= self.maximum_level and not self.treasure_found:
            should_continue = self.play_current_level()
            if not should_continue:
                break
            # For now, just increment level after each play session
            self.current_level += 1

        self.end_game()

    def end_game(self):
        """Handle game ending"""
        self.clear_terminal_screen()
        print("\nThanks for playing Terminal Treasure Hunt!")
        print("Come back anytime to practice your Linux skills!")

        # Clean up game files
        os.chdir("..")
        import shutil

        shutil.rmtree("treasure_hunt", ignore_errors=True)


def main():
    """Main entry point for the treasure hunt game"""
    game_instance = TreasureHuntGame()
    game_instance.run_game()


if __name__ == "__main__":
    main()

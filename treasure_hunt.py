# Terminal Treasure Hunt - A Linux command game
import os
import sys
from time import sleep

def main():
    """Main entry point for the treasure hunt game"""
    print("\nStarting the Terminal Treasure Hunt Game...\n")
    sleep(3)
    print("==================================================================================")
    print("\n                   Welcome to Terminal Treasure Hunt Game!\nThis is a command-line game that will help you understand basic terminal commands.\n")
    print("===================================================================================")
    sleep(2)
    print("\n\nInstructions:")
    print("\n1. You will be given a series of tasks to complete using terminal commands.\n2. Each task will guide you to the next step until you find the treasure.\n3. Follow the prompts carefully and enjoy the game!")
    sleep(1)
    print("\n\nLet's begin the adventure...")
    sleep(1)
    print("\nFirst Task:\n\nFind the hidden treasure!\nUse the 'ls' command to list the files in the current directory.\nOnce you find the treasure file, use the 'cat' command to read it.\nGood luck!\n")


if __name__ == "__main__":
    main()
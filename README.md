# Terminal Treasure Hunt

![Terminal Treasure Hunt](https://img.shields.io/badge/Linux-Commands-Practice?style=for-the-badge&logo=linux&color=orange)

An interactive terminal-based treasure hunt game designed to help you practice essential Linux commands in a fun and engaging way!

## 🎯 Objective

Solve a series of challenges by using the correct Linux commands to find the hidden treasure. Each level teaches you a different command or concept.

## 🚀 Features

- **8 Progressive Levels** covering essential Linux commands
- **Interactive Gameplay** with real command execution
- **Built-in Hints** when you get stuck
- **Real File System** manipulation (all files are safely contained)
- **Educational** - Learn by doing!

## 📚 Commands You'll Practice

- `ls`, `ls -a`, `ls -l`, `ls -lS` (listing files)
- `cat`, `grep` (file content viewing/searching)
- `chmod`, `./` (file permissions and execution)
- `ps`, `head` (process management and text manipulation)
- `zip`, `unzip` (archiving)
- `pwd`, `cd` (navigation)

## 🛠️ Requirements

- Python 3.6+
- Linux or macOS (Windows Subsystem for Linux recommended for Windows users)
- Basic terminal knowledge

## 🎮 How to Play

1. **Clone this repository:**
   ```bash
   git clone https://github.com/HlonieLive/terminal-treasure-hunt.git
   cd terminal-treasure-hunt

2. **Make the script executable:**
   ```bash
   chmod +x treasure_hunt.py

3. **Start your adventure:**
   ```bash
   ./treasure_hunt.py
4. **Follow the clues!**
   Each level will present you with a scenario and challenge you to use the appropriate Linux command.
5. **Use hints** by typing hint if you get stuck.
6. **Quit anytime** by typing quit.

## 🗺️ Game Structure

**Level 1:** Find hidden files (ls -a)

**Level 2:** Read file contents (cat) and search text (grep)

**Level 3:** Manage file permissions (chmod)

**Level 4:** Work with processes (ps)

**Level 5:** Sort files by size (ls -lS)

**Level 6:** Extract specific lines (head)

**Level 7:** Handle archives (unzip)

**Level 8:** Find the final treasure!

## 💡 Tips for Success

*Read each clue carefully.*

*Pay attention to file and directory names.*

*Remember that hidden files start with a dot (.).*

*Use pwd to see your current location.*

*Use cd to navigate between directories*

*Don't be afraid to experiment with commands!*

## 🧹 Cleanup

**The game automatically cleans up all created files when you finish or quit. No manual cleanup required!**

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

# What is this repository about?
I am going to share some small scripts/config files I use in my daily life.

# What can be found in this repository?
* BASHRC
  - mkcd function      :  creates a folder and gets into it.
  - lastedited function:  gets into the last edited folder inside a folder.
  - checktext function :  checks a text for duplicates and clears them after backing up the original file.
  - scripts function   :  gets into ~/Documents/script/[$1 if specified]
  - =========================================================================================
  - changes the terminal title to USERNAME@HOSTNAME: PWD when there isn't any commands running.
  - changes the terminal title to PWD:{COMMAND} when there is a command running.
  - PS1= user@host: PWD$
* VIMRC
  - my personal settings nothing recommended. good for Python3 coding.
* NO-SPACE-BLANK
  - Gnome3 turns display off when locked by default. If you want display to stay on even when locked use this extension. Great for showing off lock screen wallpaper.
* BGCHANGER
  - this script changes the wallpaper when we enter a new period of day(night/day). so you can have a dark wallpaper at night while having Mt.Everest wallpaper at day.
* TRANSLATOR
  - this script translates everything you copied after pressing \` key. it translates to Turkish by default but it can be changed very easily. uses notify-send to show the translated version of word.
* GIOX
  - this script downloads the currently opened YouTube page. its great when you get bored of Ctrl+C,Ctrl+V to download YouTube videos. script also works with a given YouTube link too. script saves the mp4 files to ~/Videos and mp3 files ~/Music but this can be changed with `giox -musicpath/-videopath`.
  - usage1: download the currently opened YouTube page as mp3. `giox -mp3 -ytc`
  - usage2: download the given link as mp4. `giox -mp4 -yt <LINK>`
  - usage3: download the given link as mp4+mp3. `giox -both -yt <LINK>`
* SYNTAXCHECK
  - this script finds the true writing of a word. this code belongs to Peter Nolvig. i just added sys.argv
* MDREADER
  - a small script to visualize .md files in terminal
  
# Anything to do before using?
You need to change the profile path in giox.py to use giox                                                                          
You need to change the paths in the variable section in bgchanger to use bgchanger                                                  
                                                                                                                                                                                                                                                                   
NOTE: bgchanger is designed to work at boot and keep working until computer turns off. so you can make it a startup application.       
NOTE: pytranslator is designed to work at boot and keep working until computer turns off. so you can make it a startup application.                                   
NOTE: put your day/night wallpapers in the folders you specified in bgchanger 
                                                                                                                                                                                                                                                                                                                                                                                                                                                
# BIGGEST NOTE:
bgchanger and pytranslator only works under Gnome3.
                                                                                                                                                                                                                                                                                      
# CONTACT
berkkuzgil@protonmail.com

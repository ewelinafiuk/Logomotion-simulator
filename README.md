# Logomotion-simulator
Logomotion simulator project for University

Logomotion simulator it's an easy programm working in three 
Logomotion simulator it is the program using to draw simple pictures with the help of a turtle moving around the screen.

1. the program works in two modes: batch and interactive
2. In batch mode, the program reads the command list from a text file.
3. In interactive mode, the user enters a command and the turtle draws it on the screen.
4. The supported commands are limited to: "podnies", "opusc", "obrot", "naprzod".
5. The "podnies" command causes the turtle to be picked up and move around the screen without drawing lines.
6. Command "opusc" causes the turtle to lower and move on the screen drawing lines.
7. The command "obrot" rotates the turtle clockwise by the number of degrees specified by the user as
traffic value. Initially, the turtle looks right on the screen.
8. The "naprzod" command moves the turtle towards the side that is rotated by the number of pixels specified by
use in traffic value.
9. The starting point of the turtle was created in the center of the board with dimensions (800x600). 
10. Program has also a GUI mode. 

### Interactive mode
python main.py „file to save .png”

### Batch mode
Python main.py „file to read .txt” „file to save .png”

### GUI mode
Python MainGui.py ‘nazwa_pliku_do_zapisania.png’

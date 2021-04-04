from Turtle import Turtle
from Paint import Paint
from Interactivemode import InteractiveModule
import sys
from Readingmode import ReadModule


def main():

    """turtle's start position"""
    turtle1 = Turtle([400, 300], 0)

    width_of_paint = 7
    color_of_draw = 'black'
    x_length = 800
    y_length = 600

    """reading from files"""
    if len(sys.argv) == 3:
        file_to_read = sys.argv[1]
        file_to_save = sys.argv[2]
        paint = Paint(x_length, y_length, color_of_draw,
                      width_of_paint, file_to_save)
        file = ReadModule(file_to_read, turtle1, paint, x_length, y_length)
        file.reading_file()

        """interactive program"""
    elif len(sys.argv) == 2:
        file_to_save = sys.argv[1]
        if len(file_to_save.split('.')) == 2:
            if file_to_save.split('.')[1] == 'png':
                paint = Paint(x_length, y_length, color_of_draw,
                              width_of_paint, file_to_save)
                interactive = InteractiveModule(paint, turtle1,
                                                x_length, y_length)
                interactive.interactive_mode()
            else:
                print(f'Niepoprawny format pliku')
        else:
            print(f'Niepoprawny format pliku')


if __name__ == '__main__':
    main()

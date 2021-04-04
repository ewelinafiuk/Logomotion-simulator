from Move import Move


class ReadModule:
    """
    Class ReadModule
    :param file_path: Stores file_path
    :type file_path: str

    :param turtle: object from Turtle class
    :type turtle: Turtle

    :param paint: object from Paint class
    :type heads: Paint

    :param x_length: width of painting background
    :type x_length: int

    :param y_length: height of painting background
    :type y_length: int

    """

    def __init__(self, file_path, turtle, paint, x_length, y_length):
        """Constructor method"""
        self.file_path = file_path
        self.turtle = turtle
        self.paint = paint
        self.x_length = x_length
        self.y_length = y_length

    def reading_file(self):
        """
        For comennds in file_path draw and move turtle.
        """
        try:
            with open(self.file_path, 'r') as file:
                leave = 0
                try:
                    for line in file:
                        if len(line.split()) == 1:
                            move = Move(line.split()[0], 0)
                            if move.how_to_move == 'opusc':
                                leave += 1
                            elif move.how_to_move == 'podnies':
                                leave -= 1
                        elif len(line.split()) == 2:
                            move = Move(line.split()[0], line.split()[1])

                            if move.how_to_move == "naprzod" and leave == 1:
                                move.straight_and_paint(self.turtle,
                                                        self.paint,
                                                        self.x_length,
                                                        self.y_length)
                            elif move.how_to_move == 'naprzod' and leave == 0:
                                move.straight_move(self.turtle,
                                                   self.x_length,
                                                   self.y_length)
                            elif move.how_to_move == "obrot":
                                move.turn_move(self.turtle)

                except UnicodeDecodeError as e:
                    print(f'{e}: niepoprawny format pliku')

            self.paint.saving_picture()
            self.paint.show_picture()

        except FileNotFoundError as e:
            print(f'{e}: nipoprawny plik wejsciowy')

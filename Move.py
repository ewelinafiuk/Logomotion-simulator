from math import sin, cos, radians


class Move:
    """
    Class Move
    :param how_to_move: Stores way of move
    :type how_to_move: str

    :param value_of_move: Stores value of move
    :type value_of_move: int

    """
    def __init__(self, how_to_move, value_of_move):
        """Constructor method"""
        self.how_to_move = how_to_move
        self.value_of_move = value_of_move

    def straight_move(self, turtle, x_length, y_length):
        """
        Move turtle from start position to end position.
        """
        try:
            self.movement(turtle)
            turtle.position_now()
            self.check_if_move_on_bacground(turtle, x_length, y_length)
        except TypeError as e:
            print(f'{e}: niepoprawny format')

    def straight_and_paint(self, turtle, paint, x_length, y_length):
        """
        Moving turtle from start position to end position.
        Drawing line from start position to end position.
        """
        try:
            start_position = turtle.position_now()
            self.movement(turtle)
            end_position = turtle.position_now()
            paint.drawing([start_position[0], start_position[1],
                          end_position[0], end_position[1]])
            turtle.position = end_position
            self.check_if_move_on_bacground(turtle, x_length, y_length)
        except TypeError as e:
            print(f'{e}: niepoprawny format')

    def turn_move(self, turtle):
        """ changing turtle's turn value"""
        try:
            turtle.turn += int(self.value_of_move)
        except ValueError as e:
            print(f'{e}: niepoprawna wartość')

    def movement(self, turtle):
        """ returning new turtle position with turn"""
        if turtle.turn != 0:
            x0, y0 = turtle.position[0], turtle.position[1]
            cos_theta = cos(radians(int(turtle.turn)))
            sin_theta = sin(radians(int(turtle.turn)))
            end_point = [(turtle.position[0] + int(self.value_of_move)),
                         turtle.position[1]]
            x, y = (int(end_point[0])-x0), (int(end_point[1])-y0)
            new_x = x * cos_theta - y * sin_theta
            new_y = x * sin_theta + y * cos_theta
            turtle.position = [x0 + new_x, y0 + new_y]
        else:
            end_point = [(turtle.position[0] + int(self.value_of_move)),
                         turtle.position[1]]
            turtle.position = end_point

    def check_if_move_on_bacground(self, turtle, x_length, y_length):
        '''
        Checking if move is on a background and
        if is not returning turtle position to background
        '''
        if turtle.position[0] > x_length:
            turtle.position[0] = x_length
            self.when_move_out_of_background()

        elif turtle.position[0] < 0:
            turtle.position[0] = 0
            self.when_move_out_of_background()

        elif turtle.position[1] < 0:
            turtle.position[1] = 0
            self.when_move_out_of_background()

        elif turtle.position[1] > y_length:
            turtle.position[1] = y_length
            self.when_move_out_of_background()

    def when_move_out_of_background(self):
        print('Ruch poza polem')

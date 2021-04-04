from math import sin, cos, radians


class Move:
    """
    Class Move
    :param how_to_move: Stores way of move
    :type how_to_move: str

    :param leave: chech if turtle is up or down
    :type leave: bool

    """
    def __init__(self, value_of_move, leave):
        """Constructor method"""
        self.value_of_move = value_of_move
        self.leave = leave

    def straight_move(self, turtle):
        """
        Move turtle from start position to end position.
        """
        try:
            self.movement(turtle)
            turtle.position_now()
        except TypeError as e:
            print(f'{e}: niepoprawny format')

    def straight_and_paint(self, turtle, canvas):
        """
        Moving turtle from start position to end position.
        Drawing line from start position to end position.
        """
        try:
            start_position = turtle.position_now()
            self.movement(turtle)
            end_position = turtle.position_now()
            canvas.create_line(start_position[0], start_position[1],
                               end_position[0], end_position[1], fill='black',
                               width=5)
            turtle.position = end_position
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

    def back_move(self, canvas, turtle):
        '''
        back move for single move of turtle
        '''
        try:
            start_position = turtle.position_now()
            turtle.turn += 180
            self.straight_move(turtle)
            end_position = turtle.position_now()
            canvas.create_line(start_position[0], start_position[1],
                               end_position[0], end_position[1], fill='white',
                               width=5)
            turtle.position = end_position
            turtle.turn += 180
        except TypeError as e:
            print(f'{e}: niepoprawny format')

    def go_forward(self, canvas, turtle):
        if self.leave:
            self.straight_and_paint(turtle, canvas)
        elif not self.leave:
            self.straight_move(turtle)

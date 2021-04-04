from Move import Move


class InteractiveModule:
    """
    Class InteractiveModule:
    :param paint: object from Paint class
    :type paint: Paint

    :param turtle: object from Turtle class
    :type turtle: Turtle

    :param x_length: width of painting background
    :type x_length: int

    :param y_length: height of painting background
    :type y_length: int
    """

    def __init__(self, paint, turtle, x_length, y_length):
        """Constructor method"""
        self.paint = paint
        self.turtle = turtle
        self.x_length = x_length
        self.y_length = y_length

    def ending_game(self, game):
        """ ending interactive mode of game """
        answer = (input('czy chcesz zapisać obraz? tak/nie: '))
        while answer != 'tak' and answer != 'nie':
            answer = (input('czy chcesz zapisać obraz? tak/nie: '))
        if answer == 'tak':
            self.paint.saving_picture()
            self.paint.show_picture()
            not game
            print('Do widzenia')
        elif answer == 'nie':
            not game
            print('Do widzenia')

    def creating_move(self):
        """ creating move from player choice """
        print('Ruchy, które możesz wybrać: naprzod, obrot, opusc, podnies')
        first_choice = input('wprowadź ruch: ')

        while (first_choice != 'naprzod' and first_choice != 'obrot'
                and first_choice != 'opusc' and first_choice != 'podnies'):
            print('Wybór nie istnieje')
            print('Ruchy, które możesz wybrać: naprzod, obrot, opusc, podnies')
            first_choice = input('wprowadź ruch: ')

        if first_choice == 'naprzod' or first_choice == 'obrot':
            second_choice = (input('wprowadź wartość ruchu: '))
            while not second_choice.isdigit():
                print('wartość musi być liczba')
                second_choice = (input('wprowadź wartość ruchu: '))

        elif first_choice == 'opusc' or first_choice == 'podnies':
            second_choice = 0

        move = Move(first_choice, second_choice)
        return move

    def interactive_mode(self):
        """ For players commands moving and painting with turtle."""
        print('Witaj w symulatorze logomcja')
        answer = input('wybierz numer: 1.zacznij 2.zakoncz \n')
        game = True

        while answer != '1' and answer != '2':
            print('Wybór nie istnieje')
            answer = input('wybierz numer: 1.zacznij 2.zakoncz \n')

        while game:
            if answer == '1':
                play = True
                leave = False
                while play:
                    choice = input('wybierz numer: 1.nowy ruch  '
                                   '2.pokaż obraz  3.zakończ \n')
                    while choice != '1' and choice != '2' and choice != '3':
                        print('Wybór nie istnieje')
                        choice = input('wybierz numer: 1.nowy ruch  '
                                       '2.pokaż obraz  3.zakończ \n')

                    if choice == '1':
                        move = self.creating_move()

                        if move.how_to_move == 'opusc':
                            leave = True

                        elif move.how_to_move == 'podnies':
                            leave = False

                        elif move.how_to_move == 'naprzod' and leave:
                            move.straight_and_paint(self.turtle, self.paint,
                                                    self.x_length,
                                                    self.y_length)

                        elif move.how_to_move == 'naprzod' and not leave:
                            move.straight_move(self.turtle,
                                               self.x_length, self.y_length)

                        elif move.how_to_move == 'obrot':
                            move.turn_move(self.turtle)

                    elif choice == '2':
                        self.paint.show_picture()

                    elif choice == '3':
                        self.ending_game(game)
                        return game

            elif answer == '2':
                self.ending_game(game)
                return game

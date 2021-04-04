from PIL import ImageDraw, Image


class Paint:
    '''
    class Paint. Contains attributes:

        :param x_length: width of painting background
        :type x_length: int

        :param y_length: height of painting background
        :type y_length: int

        :param colour_fill: colour of lines
        :type colour_fill: str

        :param width: width of lines
        :type width: int

        :param file_name: name of file to save painting
        :type file_name: str

    '''

    def __init__(self, x_length, y_length, colour_fill, width, file_name):
        """
        Constructs a painting with a given colour,
        width and a name of file.

        """
        self.x_length = x_length
        self.y_length = y_length
        self.background = Image.new('RGB', (self.x_length,
                                    self.y_length), 'white')
        self.colour_fill = colour_fill
        self.width = width
        self.file_name = file_name

    def drawing(self, xy=[]):
        '''
        getting a drawing handle.
        drawing on image(background)
        '''
        draw = ImageDraw.Draw(self.background)
        draw.line(xy, fill=self.colour_fill, width=self.width)
        return self.background

    def saving_picture(self):
        '''saving painting to file'''
        try:
            return self.background.save(self.file_name)
        except ValueError as e:
            print(f'{e}: niepoprawny format pliku')

    def show_picture(self):
        ''' showing user's painting'''
        return self.background.show()

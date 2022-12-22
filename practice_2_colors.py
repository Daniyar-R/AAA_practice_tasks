class Color:
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, red_ch, green_ch, blue_ch):
        self.red_ch = red_ch
        self.green_ch = green_ch
        self.blue_ch = blue_ch

    def __repr__(self):
        return f'{self.START};{self.red_ch};{self.green_ch};{self.blue_ch}' \
               f'{self.MOD}●{self.END}{self.MOD}'

    @staticmethod
    def _is_correct_ch(channel):
        if not isinstance(channel, int):
            raise ValueError(f'{type(channel)} != int')

        if not 0 <= channel <= 255:
            raise ValueError('channel value must be between 0 and 255')

    @property
    def red_ch(self):
        return self.red_ch_

    @property
    def green_ch(self):
        return self.green_ch_

    @property
    def blue_ch(self):
        return self.blue_ch_

    @red_ch.setter
    def red_ch(self, channel):
        Color._is_correct_ch(channel)
        self.red_ch_ = channel

    @blue_ch.setter
    def blue_ch(self, channel):
        Color._is_correct_ch(channel)
        self.blue_ch_ = channel

    @green_ch.setter
    def green_ch(self, channel):
        Color._is_correct_ch(channel)
        self.green_ch_ = channel

    def __eq__(self, other):
        # if self is other:
        #     return True
        return (
            self.red_ch == other.red_ch
            and self.green_ch == other.green_ch
            and self.blue_ch == other.blue_ch
        )

    def __add__(self, other):
        return Color(
            self.red_ch + other.red_ch,
            self.green_ch + other.green_ch,
            self.blue_ch + other.blue_ch,
        )

    def __hash__(self):
        color_tuple = (self.red_ch, self.green_ch, self.blue_ch)
        return hash(color_tuple)

    def __mul__(self, other):
        if other < 0 or other > 1:
            raise ValueError('Contrast value must be between 0 and 1')
        cl = -256 * (1 - other)
        f = 259 * (cl + 255) / (255 * (259 - cl))
        r = int(f * (self.red_ch - 128) + 128)
        g = int(f * (self.green_ch - 128) + 128)
        b = int(f * (self.blue_ch - 128) + 128)
        return Color(r, g, b)

    def __rmul__(self, other):
        return self.__mul__(other)


if __name__ == '__main__':
    orange_1 = Color(255, 165, 0)
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    orange_2 = Color(255, 165, 0)
    color_list = [orange_1, red, green, orange_2]
    print(set(color_list))
    print(red * 0.5)

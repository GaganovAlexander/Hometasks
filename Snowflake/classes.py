class Snowflake:
    def __init__(self, size: int, thickness: int, color: str = 'turquoise') -> None:
        """Size and thickness must be an odd numbers. Available colors are:\
        black, red, green, yellow, blue, purple and turquoise"""
        if not (isinstance(size, int) and isinstance(thickness, int) and isinstance(color, str)):
            raise TypeError(f'\033[31mSize and thickness MUST be an integers and color MUST be a string\033[0m')
        if not size % 2:
            raise ValueError(f'\033[31mSize MUST be an ODD number\033[0m')
        if not thickness % 2:
            raise ValueError(f'\033[31mThickness MUST be an ODD number\033[0m')
        self.__colors = {'black': 30,
                         'red': 31,
                         'green': 32,
                         'yellow': 33,
                         'blue': 34,
                         'purple': 35,
                         'turquoise': 36}
        if color.lower() not in self.__colors.keys():
            raise ValueError(f'\033[31mColor {color.lower()} is NOT avaliable. Available colors are: black, red, green, yellow, blue, purple and turquoise\033[0m')
        self.__thickness = thickness
        self.__size = size
        self.__color = self.__colors[color.lower()]
        self.__creating_structure()
        
    def __creating_structure(self) -> None:
        self.__structure = [[' ' for _ in range(self.__size)] for _ in range(self.__size)]
        self.__structure[self.__size//2 - (self.__thickness-1)//2:self.__size//2 + (self.__thickness-1)//2 + 1] = [['*' for _ in range(self.__size)] for _ in range(self.__thickness)]
        for j in range(self.__size):
            self.__structure[j][self.__size//2 - (self.__thickness-1)//2:self.__size//2 + (self.__thickness-1)//2 + 1] = ['*' for _ in range(self.__thickness)]
            for i in range(self.__size):
                if abs(i - j) <= (self.__thickness-1)//2 or self.__size - 1 - (self.__thickness-1)//2 <= i + j <= self.__size - 1 + (self.__thickness-1)//2:
                    self.__structure[j][i] = '*'  
        self.__structure[0][0] = f'\033[{self.__color}m' + self.__structure[0][0]
        self.__structure[self.__size-1][self.__size-1] += f'\033[0m'

    def get_view(self) -> None:
        """Prints showflake view"""
        for i in self.__structure:
            print(' '.join(i))
    
    def add_thickness(self, added_thickness: int) -> None:
        """Adds added_thickness to the shoflake thickness. added_thickness must be even;\
        if it's negative - will reduse thickness"""
        if not isinstance(added_thickness, int):
            raise TypeError('\033[31mAdded thickness MUST be an integer\033[0m')
        if added_thickness % 2:
            raise ValueError(f'\033[31mAdded thickness MUST be an EVEN number\033[0m')
        if self.__thickness + added_thickness < 0:
            raise ValueError(f'\033[31mThickness cannot go under zero. Lowest available added thicknes is -{self.__thickness - 1}\033[0m')
        self.__thickness += added_thickness
        self.__creating_structure()
    
    def resize(self, added_size: int) -> None:
        """Adds added_size to the shoflake size. added_size must be even;\
        if it's negative - will reduse size"""
        if not isinstance(added_size, int):
            raise TypeError('\033[31mAdded size MUST be an integer\033[0m')
        if added_size % 2:
            raise ValueError(f'\033[31mAdded size MUST be an EVEN number\033[0m')
        if self.__size + added_size < 0:
            raise ValueError(f'\033[31mSize cannot go under zero. Lowest available added size is -{self.__size - 1}\033[0m')
        self.__size += added_size
        self.__creating_structure()
    
    def change_color(self, color: str = 'turquoise'):
        """Changes snowflake's color, if no arguments entered - will change color to default turquoise.\
        Available colors are: black, red, green, yellow, blue, purple and turquoise"""
        if not isinstance(color, str):
            raise TypeError('\033[31mColor MUST be a string\033[0m')
        if color.lower() not in self.__colors.keys():
            raise ValueError(f'\033[31mColor {color.lower()} is NOT avaliable. Available colors are: black, red, green, yellow, blue, purple and turquoise\033[0m')
        self.__color = self.__colors[color.lower()]
        self.__creating_structure()
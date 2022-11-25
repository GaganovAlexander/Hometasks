class Student:
    def __init__(self, name: str, age: int) -> None:
        self.__name = name 
        self.__age = age
    
    def get_info(self) -> None:
        print(f'{self.__name}: {self.__age} years old')


class Snowflake:
    def __init__(self, size: int, thickness: int) -> None:
        '''Size and thickness must be an odd numbers'''
        self.__thickness = thickness
        self.__size = size
        self.__creating_structure()
        
    def __creating_structure(self) -> None:
        self.__structure = [[' ' for _ in range(self.__size)] for _ in range(self.__size)]
        self.__structure[self.__size//2 - (self.__thickness-1)//2:self.__size//2 + (self.__thickness-1)//2 + 1] = [[f'\033[34m*' for _ in range(self.__size)] for _ in range(self.__thickness)]
        for j in range(self.__size):
            self.__structure[j][self.__size//2 - (self.__thickness-1)//2:self.__size//2 + (self.__thickness-1)//2 + 1] = [f'\033[34m*' for _ in range(self.__thickness)]
            for i in range(self.__size):
                if abs(i - j) <= (self.__thickness-1)//2 or self.__size - 1 - (self.__thickness-1)//2 <= i + j <= self.__size - 1 + (self.__thickness-1)//2:
                    self.__structure[j][i] = f'\033[34m*'  
        self.__structure[self.__size-1][self.__size-1] += f'\033[0m'     

    def get_view(self) -> None:
        '''Prints showflake view'''
        for i in self.__structure:
            print(' '.join(i))
    
    def add_thickness(self, added_thickness: int) -> None:
        '''Adds added_thickness to the shoflake thickness. added_thickness must be even; if it's negative - will reduse thickness'''
        self.__thickness += added_thickness
        self.__creating_structure()
    
    def resize(self, added_size: int) -> None:
        '''Adds added_size to the shoflake size. added_size must be even; if it's negative - will reduse size'''
        self.__size += added_size
        self.__creating_structure()
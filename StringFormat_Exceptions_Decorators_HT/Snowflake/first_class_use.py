from classes import *


def main():
    s1 = Better_Snowflake(13, 3, 'red')
    s1.get_view()
    s1.resize(-2)
    s1.change_sign('0')
    s1.add_thickness(-2)
    s1.change_color()
    s1.get_view()
    print(calls)

if __name__ == '__main__':
    main()

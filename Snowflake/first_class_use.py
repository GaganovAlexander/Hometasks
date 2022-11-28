from classes import Snowflake


def main():
    s1 = Snowflake(13, 3, 'red')
    s1.get_view()
    s1.resize(-2)
    s1.add_thickness(-2)
    s1.change_color()
    s1.get_view()

if __name__ == '__main__':
    main()

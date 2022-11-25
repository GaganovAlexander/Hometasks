from classes import Snowflake


def main():
    s1 = Snowflake(21, 5)
    s1.get_view()
    s1.resize(-2)
    s1.add_thickness(-2)
    s1.get_view()

if __name__ == '__main__':
    main()

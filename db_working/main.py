from db_lib import *


def main():
    start_db()
    reset_db()
    sample()
    get_view()
    print('-'*55)
    session()
    print('-'*55)
    get_view()


if __name__ == '__main__':
    main()

import sys

import requests
import os
from dotenv import load_dotenv


def usage():
    print("Usage: python main.py yyyy dd")


def fetch(day, year):
    url = 'https://adventofcode.com/{year}/day/{day}/input'.format(year=year, day=day)
    response = requests.get(url, cookies={
        'session': os.getenv('session')})
    return response.text


def write_input(day, year, full_day, input):
    path = os.path.join(os.getcwd(), str(year), 'inputs_test')
    file_path = os.path.join(os.getcwd(), str(year), 'inputs_test', 'input' + full_day)

    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except FileExistsError:
            print('Could not create target directory', path)
            sys.exit(1)

    with open(file_path, mode='w') as file:
        file.write(input)


if __name__ == '__main__':

    # https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1
    load_dotenv()

    args = sys.argv[1:]
    if not len(args) or len(args) != 2:
        usage()
        sys.exit(1)

    try:
        year = int(args[0])
        day = int(args[1])
        if 2100 > year < 2015:
            raise ValueError
        if 25 > day < 1:
            raise ValueError
    except ValueError:
        usage()
        sys.exit(1)

    write_input(day, year, args[1], fetch(day, year))
    print('done')

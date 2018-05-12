import os
import sys

from app import Application


def main():
    """
    Main module that loads application with
    configurations and executes it's command line
    version
    """

    configuration = {}

    app = Application(configuration)
    app.run_from_commandline()


if __name__ == '__main__':
    main()

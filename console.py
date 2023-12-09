#!/usr/bin/python3
"""Command interpreter for the AirBnB Clone project"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class for the AirBnB clone console"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Command to ensure clean exit from the console"""

        return True

    def postloop(self):
        """Print an empty line before exiting the console"""

        print()

    def emptyline(self):
        """Method called when an empty line is entered in
        response to the prompt
        """

        pass

    def default(self, line):
        """Method called on an input line when the command
        prefix is not recognized.
        """

        print("Command not defined:", line)

    def do_quit(self, line):
        """To exit the program"""

        exit()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

#!/usr/bin/env python3
"""
Module for the HBNB command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    The HBNBCommand class defines the attributes and methods
    of the command interpreter.
    """
    
    prompt = '(hbnb) '
    
    def do_quit(self, arg):
        """
        Exit the program.
        """
        return True
    
    def do_EOF(self, arg):
        """
        Exit the program.
        """
        print()
        return True
    
    def emptyline(self):
        """
        Do nothing if an empty line is entered.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()


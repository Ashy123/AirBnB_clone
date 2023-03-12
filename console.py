#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = '(hbnb) '

    def do_create(self, args):
        """Create a new instance of BaseModel"""
        if not args:
            print("** class name missing **")
            return
        try:
            instance = eval(args)()
            instance.save()
            print(instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        try:
            args = args.split()
            instance = storage.all()[args[0] + '.' + args[1]]
            print(instance)
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        try:
            args = args.split()
            instance = storage.all()[args[0] + '.' + args[1]]
            del storage.all()[args[0] + '.' + args[1]]
            storage.save()
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name"""
        try:
            args = args.split()
            if args[0]:
                instances = [str(v) for k, v in storage.all().items() if k.split('.')[0] == args[0]]
            else:
                instances = [str(v) for k, v in storage.all().items()]
            print(instances)
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        if not args:
            print("** class name missing **")
            return
        try:
            args = args.split()
            instance = storage.all()[args[0] + '.' + args[1]]
        except IndexError:
            print("** instance id missing **")
            return
        except KeyError:
            print("** no instance found **")
            return
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute = args[2]
        value = args[3]
        if hasattr(instance, attribute):
            value_type = type(getattr(instance, attribute))
            setattr(instance, attribute, value_type(value))
            instance.save()
        else:
            setattr(instance, attribute, value)
            instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

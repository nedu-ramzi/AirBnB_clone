#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
from models.base_model import BaseModel
from models import storage
import json
import re



class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter."""
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it (to the JSON file) and print id"""
        if arg == "" or arg == None:
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[arg]()
            b.save()
            print(b.id)


    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name id"""

        if arg == "" or arg == None:
            print("** class name missing **")
        else:
            word = arg.split(' ')
            if word[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(word) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(word[0], word[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])


    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if arg == "" or arg == None:
            print("** class name missing **")
        else:
            word = arg.split(' ')
            if word[0] not in storage.all():
                print("** class doesn't exist **")
            elif len(word) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(word[0], word[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()


    def do_all(self, arg):
        """Prints all string representation of all instances."""
        if arg != "":
            word = arg.split(' ')
            if word[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                nl = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == words[0]]
                print(nl)
        else:
            all_list = [str(obj) for key, obj in storage.all().items()]
                print(all_list)


def do_update(self, arg):
    """Updates an instance by adding or updating attribute.
    """
    if arg == "" or arg is None:
        print("** class name missing **")
        return

    rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
    match = re.search(rex, arg)
    classname = match.group(1)
    uid = match.group(2)
    attribute = match.group(3)
    value = match.group(4)
    if not match:
        print("** class name missing **")
    elif classname not in storage.classes():
        print("** class doesn't exist **")
    elif uid is None:
        print("** instance id missing **")
    else:
        key = "{}.{}".format(classname, uid)
        if key not in storage.all():
            print("** no instance found **")
        elif not attribute:
            print("** attribute name missing **")
        elif not value:
            print("** value missing **")
        else:
            cast = None
            if not re.search('^".*"$', value):
                if '.' in value:
                    cast = float
                else:
                    cast = int
            else:
                value = value.replace('"', '')
            attributes = storage.attributes()[classname]
            if attribute in attributes:
                value = attributes[attribute](value)
            elif cast:
                try:
                    value = cast(value)
                except ValueError:
                    pass  # fine, stay a string then
            setattr(storage.all()[key], attribute, value)
            storage.all()[key].save()


    def do_EOF(self, arg):
        """Handles End Of File character"""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exits the program"""
        return True

    def emptyline(self, arg):
        """Doesn't do anything on ENTER"""
        pass

    def help_help(self):
        """Help command"""
        print("Print a list of available commands or help for a specific command")



if __name__ = '__main__':
    HBNBCommand().cmdloop()

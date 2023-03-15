#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import re


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """a class that contains the entry point of the command interpreter.
    """
    prompt = '(hbnb) '
    class_list = {'BaseModel', 'User', 'State', 'City', 'Amenity', 'Place',
                  'Review'}

    def do_EOF(self, args):
        """EOF command to exit the program.
        """
        print()
        return True

    def do_quit(self, args):
        """ Quit command to exit the program.
        """
        return True

    def emptyline(self):
        """method to do nothing when an empty line is inputed.
        """
        pass

    def postloop(self):
        """method to do nothing after each console loop.
        """
        pass

    def do_create(self, args):
        """Create command to create a new instance of BaseModel, save it in a
        JSON file and prints the id.

        Attributes:
            args (str): inputted line in command prompt.
        """
        line = parse(args)
        if not self.verify_class(line):
            return
        instance = eval(line[0] + '()')
        if isinstance(instance, BaseModel):
            instance.save()
            print(instance.id)
        return

    def do_show(self, args):
        """Show command that prints the string representation of an instance
        based on the class name and id.

        Attributes:
           args (str): inputted line in command prompt.
        """
        line = parse(args)
        if len(line) == 0:
            print('** class name missing **')
            return False
        elif line[0] not in HBNBCommand.class_list:
            print('** class doesn\'t exist **')
            return False
        elif len(line) < 2:
            print('** instance id missing **')
            return False
        key = '{}.{}'.format(line[0], line[1])
        objects = storage.all()
        if key not in objects.keys():
            print('** no instance found **')
            return False
        print(objects[key])

    def do_count(self, args):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        line = parse(args)
        count = 0
        for obj in storage.all().values():
            if line[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_destroy(self, args):
        """Destroy command that deletes an instance based on the class name
        and id. Save the change in JSON file.

        Attributes:
            args (str): inputted line in command prompt.
        """
        line = parse(args)
        if not self.verify_class(line):
            return
        if not self.verify_id(line):
            return
        key = '{}.{}'.format(line[0], line[1])
        objects = storage.all()
        del objects[key]
        storage.save()

    def do_all(self, args):
        """
        Prints all string representation of all instances based
        or not on the class name.
        """
        line = parse(args)
        objects = storage.all()
        to_print = []
        if len(line) == 0:
            for v in objects.values():
                to_print.append(str(v))
        elif line[0] in HBNBCommand.class_list:
            for k, v in objects.items():
                if line[0] in k:
                    to_print.append(str(v))
        else:
            print("** class doesn't exist **")
            return False
        print(to_print)

    def do_update(self, args):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        """
        line = parse(args)
        if not self.verify_class(line):
            return
        if not self.verify_id(line):
            return
        if not self.verify_attribute(line):
            return
        objects = storage.all()
        key = '{}.{}'.format(line[0], line[1])
        if len(line) == 4:
            obj = objects[key]
            if line[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[line[2]])
                obj.__dict__[line[2]] = valtype(line[3])
            else:
                obj.__dict__[line[2]] = line[3]

        elif type(eval(line[2])) == dict:
            obj = objects[key]
            for k, v in eval(line[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def default(self, args):
        """Default method that is called when the inputted command starts
        with a class name or when the input is invalid

        Attributes:
            args (str): The inputted line string
        """
        methoddict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", args)
        if match is not None:
            line = [args[:match.span()[0]], args[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", line[1])
            if match is not None:
                command = [line[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in methoddict.keys():
                    call = "{} {}".format(line[0], command[1])
                    return methoddict[command[0]](call)
        print("*** Unknown syntax: {}".format(args))
        return False

    @classmethod
    def verify_class(cls, line):
        """Static method to verify inputed class"""
        if len(line) == 0:
            print('** class name missing **')
            return False
        elif line[0] not in HBNBCommand.class_list:
            print('** class doesn\'t exist **')
            return False
        return True

    @staticmethod
    def verify_id(line):
        """Static method to verify the id.
        """
        if len(line) == 1:
            print('** instance id missing **')
            return False
        objects = storage.all()
        key = '{}.{}'.format(line[0], line[1])
        if key not in objects.keys():
            print('** no instance found **')
            return False
        return True

    @staticmethod
    def verify_attribute(line):
        """Static method to verify the attribute in inputted line.
        """
        if len(line) < 3:
            print("** attribute name missing **")
            return False
        elif len(line) < 4:
            print("** value missing **")
            return False
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

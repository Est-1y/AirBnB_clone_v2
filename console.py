#!/usr/bin/python3
"""The Console Module. """
import cmd
import sys
from models.amenity import Amenity
from models.user import User
from models.review import Review
from models.place import Place
from models.state import State
from models.base_model import BaseModel
from models.__init__ import storage
from models.city import City


class HBNBCommand(cmd.Cmd):
    """functionality for the BNB console."""

    # determines prompt for different modes.
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
        'number_rooms': int, 'number_bathrooms': int,
        'max_guest': int, 'price_by_night': int,
        'latitude': float, 'longitude': float
    }

    def preloop(self):
        """preloop"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """
        Reformation of a command line
        """
        _cmd = _cls = _id = _args = ''  # initialize line elements

        # scan for formating.
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:
            pline = line[:]

            _cls = pline[:pline.find('.')]

            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in HBNBCommand.dot_cmds:
                raise Exception

            # parsing parenthesis
            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                pline = pline.partition(', ')  # pline convert to tuple

                _id = pline[0].replace('\"', '')

                pline = pline[2].strip()  # pline is now str
                if pline:
                    # checking for arguments
                    if pline[0] == '{' and pline[-1] == '}'\
                            and type(eval(pline)) is dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')
            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """postcmd"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, command):
        """exiting the HBNB console"""
        exit()

    def help_quit(self):
        """  """
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """ Handles EOF """
        print()
        exit()

    def help_EOF(self):
        """ Prints help documentation """
        print("Exits the program without formatting\n")

    def emptyline(self):
        """ """
        pass

    def do_create(self, args):
        """ Create objects"""
        try:
            if not args:
                raise SyntaxError()
            arg_list = args.split(" ")
            kw = {}
            for arg in arg_list[1:]:
                arg_splited = arg.split("=")
                arg_splited[1] = eval(arg_splited[1])
                if type(arg_splited[1]) is str:
                    arg_splited[1] = arg_splited[1].replace(
                        "_", " ").replace('"', '\\"')
                kw[arg_splited[0]] = arg_splited[1]
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        new_instance = HBNBCommand.classes[arg_list[0]](**kw)
        new_instance.save()
        print(new_instance.id)

    def help_create(self):
        """ Help information. """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """ Method """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        # guard.
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """ Help information """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """ """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id

        try:
            del (storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
        print_list = []

        if args:
            args = args.split(' ')[0]  # remove possible trailing args
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage.all(HBNBCommand.classes[args]).items():
                print_list.append(str(v))
        else:
            for k, v in storage.all().items():
                print_list.append(str(v))
        print(print_list)

    def help_all(self):
        """ Help informatio """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """Count number instances"""
        count = 0
        for k, v in storage._FileStorage__objects.items():
            if args == k.split('.')[0]:
                count += 1
        print(count)

    def help_count(self):
        """ """
        print("Usage: count <class_name>")

    def do_update(self, args):
        """ Updates """
        c_name = c_id = att_name = att_val = kwargs = ''

        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        else:
            print("** class name missing **")
            return
        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        else:
            print("** instance id missing **")
            return

        # generating key
        key = c_name + "." + c_id

        # determining key presence
        if key not in storage.all():
            print("** no instance found **")
            return

        # determine types of arguments
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:
            args = args[2]
            if args and args[0] == '\"':
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            if not att_name and args[0] != ' ':
                att_name = args[0]

            if args[2] and args[2][0] == '\"':
                att_val = args[2][1:args[2].find('\"', 1)]

            if not att_val and args[2]:
                att_val = args[2].partition(' ')[0]

            args = [att_name, att_val]

        new_dict = storage.all()[key]

        for i, att_name in enumerate(args):

            if (i % 2 == 0):
                att_val = args[i + 1]
                if not att_name:
                    print("** attribute name missing **")
                    return
                if not att_val:
                    print("** value missing **")
                    return

                if att_name in HBNBCommand.types:
                    att_val = HBNBCommand.types[att_name](att_val)

                new_dict.__dict__.update({att_name: att_val})

        new_dict.save()

    def help_update(self):
        """ """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()

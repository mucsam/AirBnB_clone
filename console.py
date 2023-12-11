#!/usr/bin/python3
"""Command interpreter for the AirBnB Clone project"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """Class for the AirBnB clone console"""

    prompt = "(hbnb) "

    def do_EOF(self, arg):
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

    def default(self, arg):
        """Method called on an input line when the command
        prefix is not recognized.
        """

        print("Command not defined:", arg)

    def do_quit(self, arg):
        """To exit the program"""

        exit()

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it
        and prints the id
        """
        if not arg:
            print("** class name missing **")
            return
        
        class_name = globals().get(arg)
        if class_name:
            new_inst = class_name()
            new_inst.save()
            print(new_inst.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name
        and id
        """

        if not arg:
            print("** class name missing **")
            return

        arg_list = arg.split(' ')
        class_name = arg_list[0]
        class_obj = globals().get(class_name)

        if class_obj:
            if len(arg_list) < 2:
                print("** instance id missing **")
            else:
                ins_id = arg_list[1]
                data = storage.all()
                for key, value in data.items():
                    if key == class_name + "." + ins_id:
                        obj1 = class_obj(value)
                        print(obj1)
                        return
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """

        if not arg:
            print("** class name missing **")
            return
        
        arg_list = arg.split(' ')
        class_name = arg_list[0]
        class_obj = globals().get(class_name)

        if class_obj:
            if len(arg_list) < 2:
                print("** instance id missing **")
            else:
                ins_id = arg_list[1]
                data = storage.all()
                for key, value in data.items():
                    if key == class_name + "." + ins_id:
                        del data[key]
                        storage.save()
                        return
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on
        the class name
        """

        instances_list = []
        if arg:
            arg_list = arg.split(' ')
            class_name = arg_list[0]
            class_obj = globals().get(class_name)

            if class_obj:
                data = storage.all()
                for key, value in data.items():
                    instances_list.append(str(value))
                print(instances_list)

            else:
                print("** class doesn't exist **")
        else:
            data = storage.all()
            for key, value in data.items():
                instances_list.append(str(value))
            print(instances_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save change into the
        JSON file)
        """

        if not arg:
            print("** class name missing **")
            return

        arg_list = arg.split(' ')
        class_name = arg_list[0]
        class_obj = globals().get(class_name)
        if class_obj:
            if len(arg_list) < 2:
                print("** instance id missing **")
            else:
                ins_id = arg_list[1]
                data = storage.all()
                for key, value in data.items():
                    if key == class_name + "." + ins_id:
                        if len(arg_list) < 3:
                            print("** attribute name missing **")
                        else:
                            if len(arg_list) < 4:
                                print("** value missing **")
                            else:
                                attr_name = arg_list[2]
                                attr_value = arg_list[3]
                                attr_type = type(getattr(value, attr_name))
                                if attr_type is str:
                                    attr_value = str(attr_value)
                                elif attr_type is int:
                                    attr_value = int(attr_value)
                                elif attr_type is float:
                                    attr_value = float(attr_value)
                                setattr(value, attr_name, attr_value)
                                storage.save()
                        return
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()

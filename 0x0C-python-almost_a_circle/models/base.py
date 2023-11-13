#!/usr/bin/python3
"""This Python file is used to define a Base Model Class."""
import turtle
import csv
import json


class Base:
    """A class that is used to represent
    the Base Model.

    Attributes:
        __nb_objects (int): It represents the number
        of bases which are instantiated.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """A function used to initialize a NEW Base.

        Args:
            id (int): The NEW base's identity.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """A function that is used to return
        JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): represents list of dicts.
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """A function used to write the JSON
        Serialization of list of objects to a file.

        Args:
            list_objs (list): represents list of Base instances
            which are inherited.
        """

        FileName = cls.__name__ + ".json"

        with open(FileName, "w") as jsf:
            if list_objs is None:
                jsf.write("[]")
            else:
                dict_list = [i.to_dictionary() for i in list_objs]
                jsf.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """A function used to return the
        a JSON string's deserialization.

        Args:
            json_string (str): A JSON str that represents
            a list of dictitionaries.
        Returns:
            Empty list - if json_string is None or empty.
            The Python list represented by json_string - otherwise.
        """

        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """A function that returns a class
        from a dictionary of attributes that
        have been instantiated.

        Args:
            **dictionary (dict): represents Key/value pairs
            of attributes to initialize.
        """

        if dictionary and dictionary != {}:

            if cls.__name__ == "Rectangle":
                New = cls(1, 1)
            else:
                New = cls(1)
            New.update(**dictionary)
            return New

    @classmethod
    def load_from_file(cls):
        """A function that is used to return a list
        of classes from a file of JSON strings that
        have been instantiated.

        It reads from the file `<cls.__name__>.json`.

        Returns:
            Empty list - if it doesn't exist.
            List of instantiated classes - Otherwise.
        """

        FileName = str(cls.__name__) + ".json"

        try:
            with open(FileName, "r") as jsf:
                dict_list = Base.from_json_string(jsf.read())
                return [cls.create(**dic) for dic in dict_list]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """A function that is used to write the CSV
        Serialization of list of Objects to file.

        Args:
            list_objs (list): represents list of Base instances
            which are inherited..
        """

        FileName = cls.__name__ + ".csv"

        with open(FileName, "w", newline="") as csvf:
            if list_objs is None or list_objs == []:
                csvf.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    Field_Names = ["id", "width", "height", "x", "y"]
                else:
                    Field_Names = ["id", "size", "x", "y"]
                Dic_writer = csv.DictWriter(csvf, fieldnames=Field_Names)

                for Obj in list_objs:
                    Dic_writer.writerow(Obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """A function that is used to return a list
        of classes from CSV file that
        have been instantiated.

        It reads from the file `<cls.__name__>.csv`.

        Returns:
             Empty list - if it doesn't exist.
            List of instantiated classes - Otherwise.
        """

        FileName = cls.__name__ + ".csv"

        try:
            with open(FileName, "r", newline="") as csvf:
                if cls.__name__ == "Rectangle":
                    Field_Names = ["id", "width", "height", "x", "y"]
                else:
                    Field_Names = ["id", "size", "x", "y"]
                dict_list = csv.DictReader(csvf, fieldnames=Field_Names)
                dict_list = [dict([l, int(c)] for l, c in dic.items())
                              for dic in dict_list]
                return [cls.create(**dic) for dic in dict_list]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """A function that is used to draw Rectangles
        and Squares by using the module called turtle.

        Args:
            list_rectangles (list): represents a list of Rectangle 
            objects.
            list_squares (list): represents a list of Square
            objects.
        """

        Tur = turtle.Turtle()
        Tur.screen.bgcolor("#b7312c")
        Tur.pensize(3)
        Tur.shape("turtle")

        Tur.color("#ffffff")

        for Rec in list_rectangles:
            Tur.showturtle()
            Tur.up()
            Tur.goto(Rec.x, Rec.y)
            Tur.down()

            for k in range(2):
                Tur.forward(Rec.width)
                Tur.left(90)
                Tur.forward(Rec.height)
                Tur.left(90)
            Tur.hideturtle()

        Tur.color("#b5e3d8")

        for Sq in list_squares:
            Tur.showturtle()
            Tur.up()
            Tur.goto(Sq.x, Sq.y)
            Tur.down()
            for k in range(2):
                Tur.forward(Sq.width)
                Tur.left(90)
                Tur.forward(Sq.height)
                Tur.left(90)
            Tur.hideturtle()

        turtle.exitonclick()

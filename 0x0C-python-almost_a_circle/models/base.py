#!/usr/bin/python3
"""
This module defines the Base class.
"""
import csv
import json


class Base:
    """Represents the base class for other shapes.

    Attributes:
        id (int, optional): The unique id for the shape.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base instance with
        a given id or auto-incremented one.

        Args:
            id (int, optional): The id of the shape.
                                Defaults to auto-incremented.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): The list of dictionaries.

        Returns:
            str: The JSON representation of 'list_dictionaries'.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation to a file.

        Args:
            list_objs (list): A list of instances who inherits of Base.
        """
        filename = f"{cls.__name__}.json"
        json_str = "[]"
        if list_objs:
            list_dict = [obj.to_dictionary() for obj in list_objs]
            json_str = Base.to_json_string(list_dict)

        with open(filename, "w") as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation.

        Args:
            json_string (str): A string representation a list of dictionaries.

        Returns:
            The list represented by 'json_string'.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with all attributes already set.

        Args:
            dictionary (dict): Used as '**kwargs' of the method 'update'.

        Returns:
            (Rectangle or Square): The created instance.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load a list of instances from a file.

        Returns:
            list: The list of loaded instances.
        """
        filename = f"{cls.__name__}.json"
        instances = []

        try:
            with open(filename, "r") as file:
                list_of_dicts = Base.from_json_string(file.read())
                for dictionary in list_of_dicts:
                    instances.append(cls.create(**dictionary))
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV string representation of
        a list of instances to a file.

        Args:
            list_objs (list): A list of instances who inherits of Base.
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)

            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y]
                    )
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Load a list of instances from a CSV file."""
        filename = f"{cls.__name__}.csv"
        instances = []

        try:
            with open(filename, "r") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        id, width, height, x, y = row
                        dictionary = {
                            "id": int(id),
                            "width": int(width),
                            "height": int(height),
                            "x": int(x),
                            "y": int(y),
                        }
                    elif cls.__name__ == "Square":
                        id, size, x, y = row
                        dictionary = {
                            "id": int(id),
                            "size": int(size),
                            "x": int(x),
                            "y": int(y),
                        }
                    instances.append(cls.create(**dictionary))
            return instances
        except FileNotFoundError:
            return []

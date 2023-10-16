#!/usr/bin/python3
"""
Module: base
Contains the Base class.
"""
import os
import json
import csv


class Base:
    """
    Base class for all other classes in the project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a file in JSON format.
        """

        filename = cls.__name__ + ".json"

        if list_objs is None:
            list_objs = []

        list_dicts = [obj.to_dictionary() for obj in list_objs]

        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.
        """

        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new instance of the class using a dictionary of attributes.
        """

        if cls.__name__ == "Rectangle":
            new_obj = cls(1, 1)
        elif cls.__name__ == "Square":
            new_obj = cls(1)
        else:
            new_obj = None

        new_obj.update(**dictionary)

        return new_obj

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of objects from a file in JSON format.
        """

        filename = cls.__name__ + ".json"

        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**dict) for dict in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes and saves instances to a CSV file.
        """

        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    row_data = [obj.id, obj.width, obj.height, obj.x, obj.y]
                    writer.writerow(row_data)
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes and returns instances from a CSV file.
        """

        filename = cls.__name__ + ".csv"
        if not os.path.exists(filename):
            return []

        instances = []
        with open(filename, "r") as file:
            reader = csv.reader(file)
            csv_list = list(reader)

            for csv_elem in csv_list:
                if cls.__name__ == "Rectangle":
                    instance = cls.create(
                        id=int(csv_elem[0]),
                        width=int(csv_elem[1]),
                        height=int(csv_elem[2]),
                        x=int(csv_elem[3]),
                        y=int(csv_elem[4])
                    )
                elif cls.__name__ == "Square":
                    instance = cls.create(
                        id=int(csv_elem[0]),
                        size=int(csv_elem[1]),
                        x=int(csv_elem[2]),
                        y=int(csv_elem[3])
                    )

                instances.append(instance)

        return instances

"""DictObject represents a deeply nested json hash as objects with properties."""

import json


def dictobject(value):
    """Wrap value into a DictObject if needed."""
    if isinstance(value, dict):
        return DictObject(**value)
    if isinstance(value, list):
        return list(map(dictobject, value))
    return value


class DictObject:
    """DictObject class."""

    def __init__(self, *args, **kwargs):
        """Initialize the instance."""
        if len(args) == 0:
            self.__data = kwargs
            return

        if len(args) > 1:
            raise TypeError

        if not isinstance(args[0], dict):
            print(args)
            raise TypeError

        self.__data = {**args[0], **kwargs}

    def __getattr__(self, name):
        """Return item."""
        if name not in self.__data:
            raise AttributeError

        return dictobject(self.__data[name])

    def __getitem__(self, name):
        """Return item."""
        return dictobject(self.__data[name])

    def __repr__(self):
        """Represent object as string."""
        return f"<DictOBject data={json.dumps(self.__data, indent=4) }>"

from abc import ABC, abstractmethod


class Validator (ABC):
    def __set_name__(self, instance: object, name: str) -> None:
        self.protected_name: str = "_" + name

    def __get__(self, instance: object, owner: object = None) -> object:
        return getattr(instance, self.protected_name)

    def __set__(self, instance: object, value: object) -> None:
        if not self.validate(value):
            pass
        setattr(instance, self.protected_name, value)

    @abstractmethod
    def validate(self, value: object) -> None:
        pass


class Number (Validator):
    def __init__(self,
                 value_type: type,
                 min_value: int,
                 max_value: int) -> None:
        self._value_type = value_type
        self._min_value = min_value
        self._max_value = max_value

    def validate(self, value: int) -> None:
        if not isinstance(value, self._value_type) :
            raise TypeError("Quantity should be integer")
        if value < self._min_value or value > self._max_value:
            raise ValueError("Quantity should not be less than "
                             f"{self._min_value} and greater than "
                             f"{self._max_value}")
        return


class OneOf (Validator):
    def __init__(self,
                 options: list[str]) -> None:
        self._options = options

    def validate(self, value: str) -> None:
        if value not in self._options:
            raise ValueError(f"Expected {value} to be one of {self._options}")

        return


class BurgerRecipe:
    buns = Number(int, 2, 3)
    cheese = Number(int, 0, 2)
    tomatoes = Number(int, 0, 3)
    cutlets = Number(int, 1, 3)
    eggs = Number(int, 0, 2)
    sauce = OneOf(["ketchup", "mayo", "burger"])

    def __init__(self,
                 buns: int,
                 cheese: int,
                 tomatoes: int,
                 cutlets: int,
                 eggs: int,
                 sauce: str) -> None:
        self.buns = buns
        self.cheese = cheese
        self.tomatoes = tomatoes
        self.cutlets = cutlets
        self.eggs = eggs
        self.sauce = sauce

    print("burger will be created")

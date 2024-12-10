from abc import ABC, abstractmethod
from typing import Optional, Dict, List
from math import log2


class Computer(ABC):

    def __init__(self, manufacturer: str, model: str) -> None:
        self.manufacturer = manufacturer
        self.model = model
        self.processor: Optional[str] = None
        self.ram: Optional[int] = None
        self.price: int = 0

    @property
    @abstractmethod
    def available_processors(self) -> Dict[str, int]:
        pass

    @property
    @abstractmethod
    def max_ram(self) -> int:
        pass

    @property  # it is calculating only here, base on the given value of the max_ram
    def valid_ram(self) -> List[int]:
        return [2 ** i for i in range(1, int(log2(self.max_ram))+1)]

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '':
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == '':
            raise ValueError("Manufacturer name cannot be empty.")
        self.__model = value

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.available_processors:
            raise ValueError(f"{processor} is not compatible with {self.__str__()}"
                             f" {self.manufacturer} {self.model}!")
        if ram not in self.valid_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with {self.__str__()}"
                             f" {self.manufacturer} {self.model}!")
        self.processor = processor
        self.ram = ram
        self.price += self.available_processors[processor] + int(log2(ram)) * 100
        return f"Created {self.__repr__()} for {self.price}$."

    @abstractmethod
    def __str__(self):
        pass

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and " \
               f"{self.ram}GB RAM"

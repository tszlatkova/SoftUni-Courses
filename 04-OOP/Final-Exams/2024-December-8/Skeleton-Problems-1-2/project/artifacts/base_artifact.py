from abc import ABC, abstractmethod


class BaseArtifact(ABC):

    def __init__(self, name: str, price: float, space_required: int) -> None:
        self.name = name
        self.price = price
        self.space_required = space_required

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Artifact name cannot be null or empty!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value) -> None:
        if value <= 0.0:
            raise ValueError("Artifact price should be more than 0.0!")
        self.__price = value

    @property
    def space_required(self):
        return self.__space_required

    @space_required.setter
    def space_required(self, value) -> None:
        if value < 1 or value > 1000:
            raise ValueError("Space required for the artifact exhibition must be between "
                             "1 and 1000!")
        self.__space_required = value

    @property
    @abstractmethod
    def kind_of_artefact(self):
        pass

    def artifact_information(self) -> str:
        return f"{self.kind_of_artefact()} Artifact: {self.name}; " \
               f"Price: {self.price:.2f}; " \
               f"Required space: {self.space_required}"

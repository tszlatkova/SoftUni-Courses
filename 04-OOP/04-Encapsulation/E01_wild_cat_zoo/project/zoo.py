from project.animal import Animal
from project.worker import Worker
from typing import List


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int,
                 workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        worker = next((w for w in self.workers if w.name == worker_name), None)
        if worker:
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        total_salaries = sum(w.salary for w in self.workers)
        if total_salaries < self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        total_care = sum(a.money_for_care for a in self.animals)
        if total_care < self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= total_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int) -> None:
        self.__budget += amount

    # def animals_status(self):
    #     lions = []
    #     tigers = []
    #     cheetah = []
    #     for animal in self.animals:
    #         if animal.__class__.__name__ == 'Lion':
    #             lions.append(repr(animal))
    #         if animal.__class__.__name__ == 'Tiger':
    #             tigers.append(repr(animal))
    #         if animal.__class__.__name__ == 'Cheetah':
    #             cheetah.append(repr(animal))
    #
    #     result = [f"You have {len(self.animals)} animals", f"----- {len(lions)} Lions:"]
    #     result.extend(lions)
    #     result.append(f"----- {len(tigers)} Tigers:")
    #     result.extend(tigers)
    #     result.append(f"----- {len(cheetah)} Cheetahs:")
    #     result.extend(cheetah)
    #     return '\n'.join(result)
    def animals_status(self):
        return self.__print_status(self.animals, 'Lion', 'Tiger', 'Cheetah')

    def workers_status(self):
        return self.__print_status(self.workers, 'Keeper', 'Caretaker', 'Vet')

    @staticmethod
    def __print_status(category: List[Animal|Worker], *args) -> str:
        elements = {arg: [] for arg in args}
        for el in category:
            elements[el.__class__.__name__].append(repr(el))

        result = [f"You have {len(category)} "
                  f"{str(category[0].__class__.__bases__[0].__name__).lower()}s"]
        for key in args:
            value = elements[key]
            result.append(f"----- {len(value)} {key}s:")
            result.extend(value)

        return '\n'.join(result)

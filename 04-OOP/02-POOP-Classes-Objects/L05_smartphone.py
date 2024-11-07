# Create a class called Smartphone. Upon initialization, it should receive a memory
# (number). It should also have 2 other instance attributes: apps (empty list by default)
# and is_on (False by default).


class Smartphone:

    def __init__(self, memory: float) -> None:
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self) -> None:
        """"
        Sets is_on to True if the phone is off, otherwise sets it to False
        """
        self.is_on = not self.is_on
        # if not self.is_on:
        #     self.is_on = True
        # else:
        #     self.is_on = False

    def install(self, app: str, app_memory: float) -> str:
        """"
        o	If there is enough memory on the phone and it is on, install the app (add it
        to apps and decrease the memory of the phone) and return "Installing {app}"
        o	If there is enough memory, but the phone is off, returns "Turn on your phone
        to install {app}"
        o	Otherwise, returns "Not enough memory to install {app}"
        """
        if self.memory - app_memory >= 0:
            if self.is_on:
                self.apps.append(app)
                self.memory -= app_memory
                return f"Installing {app}"
            return f"Turn on your phone to install {app}"
        return f"Not enough memory to install {app}"

    def status(self) -> str:
        """"
        Returns "Total apps: {total_apps_count}. Memory left: {memory_left}"
        """
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())

print(Smartphone.status.__doc__)
print(smartphone.__dict__)

# Create a function called start_playing which will receive an instance and will return
# its play() method.
# Submit only the start_playing function in the judge system

def start_playing(obj):
    return obj.play()


# Test code 1
class Guitar:
    def play(self):
        return "Playing the guitar"


guitar = Guitar()
print(start_playing(guitar))


# Test code 2
class Children:
    def play(self):
        return "Children are playing"


children = Children()
print(start_playing(children))

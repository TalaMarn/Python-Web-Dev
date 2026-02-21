class car:
    color = "red"
    model = 'Toyota'
    hose_power = 200
    def drive(self):
        print("The car is driving")

class animal:
    def speak(self):
        print("The animal is speaking")

class dog(animal):
    def bark(self):
        print("The dog is barking")

dog = dog()
dog.speak()
class Animal:
    def speak(self):
        print("lion is always a lion")

class Bird(Animal):
    def speak(self):
        print("Tweet!")


my_bird = Bird()
my_bird.speak()

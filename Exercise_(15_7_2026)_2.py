class Animal:
    def eat(self):
        print("Animal eats food")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


class Cat(Animal):
    def meow(self):
        print("Cat meows")


class Elephant(Animal):
    def trumpet(self):
        print("Elephant trumpets")


dog1 = Dog()
cat1 = Cat()
elephant1 = Elephant()

dog1.eat()
dog1.bark()

cat1.eat()
cat1.meow()

elephant1.eat()
elephant1.trumpet()
import random

class Person:

    def __init__(self, firstname, lastname, health, status):
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        print("Hello, my name is {} {}".format(self.firstname, self.lastname))

    def emote(self):
        emotion = random.randrange(1,3)
        if emotion == 1:
            print("{} is happy today".format(self.firstname))
        elif emotion == 2:
            print("{} is sad right now".format(self.firstname))

    def status_change(self):
        if self.health >= 90:
            print("{} is totally healhy".format(self.firstname))
        elif self.health >= 76:
            print("{} is little bit tired".format(self.firstname))
        elif self.health >= 51:
            print("{} is unwell".format(self.firstname))
        elif self.health >= 40:
            print("{} must go to the doctor".format(self.firstname))
        else:
            print("{} is uncnscious".format(self.firstname))



Toretto = Person("Dominic" ,"Toretto", 100, status=True)
Heisenber = Person("Walter", "White", 77, status=False)
Lee = Person("Lee", "Williams", 72, status=True)

print("{} is my friend? {}".format(Toretto.firstname, Toretto.status))
print("{} is my friend? {}".format(Heisenber.firstname, Heisenber.status))

Toretto.introduce()
Heisenber.introduce()
Lee.introduce()
print("")
Toretto.status_change()
Heisenber.status_change()
Lee.status_change()


class Enemy(Person):

    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon = weapon

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'strick':
            other.health -= 5
        print(other.health)

    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak".format(other.firstname))

    def steal(self, other):
        print("{} ha ha ha, i have your stuf".format(other.firstname))
        if other.status == True:
            other.status = False

Chan = Enemy("rock", "Chan", "Li", 75, status=False)
Chan.hurt(Toretto)
Chan.insult(Heisenber)
Chan.steal(Heisenber)





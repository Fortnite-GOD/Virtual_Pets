class Pet:

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.direction = 0
        self.is_alive = True
        self.happiness = 5

    def eat(self):
        if self.is_alive:
            print(self.name + " says 'Mmmmmm, so good and tasty!'")
        else:
            print(self.name + " is too dead to eat.")
            
    def sleep(self):
        if self.is_alive:
            print(self.name + " is schleeep")
        else:
            print(self.name + " is already aschleeep... FOREVER!")

    def play(self):
        if self.is_alive:
            print(self.name + " says, 'Yeet!'")
        else:
            print(self.name + " currently has no arms, so they can't play.")

    def rotate_right(self):
        if self.is_alive:
            self.direction += 1

            if self.direction == 4:
                self.direction = 0
        else:
            print(self.name + " has no legs, so HE AIN'T MOVIN")

    def rotate_left(self):
        if self.is_alive:
            self.direction -= 1

            if self.direction == -1:
                self.direction = 3
        else:
            print(self.name + " has no legs, so HE AIN'T MOVIN")

    def move(self):
        if self.is_alive:
            if self.direction == 0:
                self.y += 1
            elif self.direction == 1:
                self.x += 1
            elif self.direction == 2:
                self.y -= 1
            elif self.direction == 3:
                self.x -= 1
        else:
            print(self.name + " has no legs, so HE AIN'T MOVIN")

    def kill(self, other):
        if self.is_alive:
            print(self.name + " attacks " + other.name +"!")
            print(other.name + " goes 'oof' and dies.")
            other.is_alive = False
        else:
            print(self.name + " is too dead too kill people to make them dead.")

    def hug(self, other):
        print(self.name + " hugs " + other.name +"!")
        other.happiness += 1
        print(other.name + " says, 'I'm like " + str(other.happiness) + " happy now.")

    def __repr__(self):
        return "Name: " + self.name + \
               " [x=" + str(self.x) + \
               ", y=" + str(self.y) + \
               ", d=" + str(self.direction) + "]"
    
pet1 = Pet("Mr.Forehead the God")
pet2 = Pet("Juan Carlos Pablo Romero")
pet3 = Pet("Oofmaster")
pet4 = Pet("Herobrine the Scary Man")

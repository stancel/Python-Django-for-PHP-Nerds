class Cake(object):

    def __init__(self, flavour, icing):
        self.flavour = flavour
        self.icing = icing
        self._temperature = 22

    def __str__(self):
        """
        Python lets you do CRAZY stuff, like override the method used to
        represent an object as a string and have it do something else entirely.
        In this example here, we're telling the Cake object to run the
        make_toast() method whenever someone tries to print this object.
        """
        self.make_toast()
        return "This is a cake"

    def bake(self):
        while self._temperature < 180:
            self._temperature += 1
        return "Baked at {}C".format(self._temperature)

    def make_toast(self):
        print("Making toast!")
        # Some crazy logic should be here, something that telnets into a toaster


chocolate_cake = Cake("Chocolate", "Cream Cheese")

print(chocolate_cake.icing)    # Cream Cheese
print(chocolate_cake.flavour)  # Chocolate

# This will print "Making toast!" as well as "This is a cake"
print(chocolate_cake)

print(chocolate_cake.bake())  # Baked at 180C

#!/usr/bin/env python3

# We need random for our get_random_skill() methods
import random


# You'll notice that I'm using the triple-quote """ here for comments on
# classes.  Typically, this is called the "docstring" and it's used to
# autogenerate documentation for your classes and functions in much the same way
# as PHPDoc does.


class Person(object):
    """
    This is the base class, containing only two simple properties (name and
    city) and defining how to render a person if printed.
    """

    def __init__(self, name=None, city=None):
        """
        Note that we're using keyword arguments here.  This is common in Python
        objects because you're typically going to subclass things a few times
        and remembering the order of things at multiple inheritance levels can
        get ugly.

        Note that keyword arguments can also be positional.  That is, you could
        instantiate Person like this if you wanted to:

            Person("Kim", "Seoul")

        ...but doing this negates the usefulness of keyword arguments.  If we
        later want to modify the Person class, we need to make sure that all
        code calling this constructor won't be upset by our changes.

        You could add some validation here if you wanted to.  You could add a
        check that the city is defined, that the name is capitalised etc.  For
        our purposes though, this is all we needed.
        """
        self.name = name
        self.city = city

    def __str__(self):
        """
        Making use of the .format() minilanguage again.
        """
        return "{} lives in {}".format(self.name, self.city)


class SkilledPerson(Person):
    """
    SkilledPerson inherits from Person.
    """

    def __init__(self, skill_level=0, *args, **kwargs):
        """
        This may be your first experience with *args and **kwargs, but it won't
        be the last.  They're a way to dump variable declarations that you
        aren't immediately interested in into a container that can be passed
        around.  In this case, SkilledPerson is only interested in the attribute
        skill_level, but its parent class, Person probably wants other stuff.
        We use this variables to pass "all the things" passed to the constructor
        up to the parent class without having to know what they are.

        In other words, this method could have just as easily been written as:

        def __init__(self, name=None, city=None, skill_level=0):
            Person.__init__(self, name=name, city=city)
            self.skill_level = skill_level

        ...but that would be ugly and repetitive.
        """
        Person.__init__(self, *args, **kwargs)
        self.skill_level = skill_level

    def increase_skill_level(self, increment):
        self.skill_level += increment

    def get_random_skill(self):
        """
        This is a tidy way of specifying an interface without having to worry
        about default behaviour.  Now, all subclasses of SkilledPerson will have
        a get_random_skill() method, but only subclasses that override this
        method will be able to make use of it.
        """
        raise NotImplementedError()


class Hacker(SkilledPerson):
    """
    We're now a subclass of a subclass.
    """
    
    def __init__(self, kungfoo=None, *args, **kwargs):
        """
        Same as above, only we're going to sort the list of kungfoo skills since
        that's just nicer.
        """
        SkilledPerson.__init__(self, *args, **kwargs)
        self.kungfoo = sorted(kungfoo)

    def add_kungfoo(self, kungfoo):
        """
        This is a slick way to make sure that any additions to a list are kept
        unique:
        
        1. Add the object to the list by concatenating the lists together (you
           can also use .append() but this works on one line nicely
        2. Turn that new list into a set with set().  Sets don't allow for
           duplicate values, so this will automatically remove duplicates.
        3. Re-cast your set as a list to make sure that it's mutable.
        4. Sort the list with sorted() because that's nicer.
        """
        self.kungfoo = sorted(list(set(self.kungfoo + [kungfoo])))
    
    def get_random_skill(self):
        """
        Since self.kungfoo is just a list, random.choice() works nicely.
        """
        return random.choice(self.kungfoo)


class Chef(SkilledPerson):
    """
    Chef is a sibling to Hacker, a child to SkilledPerson, and a grandchild to
    Person.
    """
    
    def __init__(self, specialties, *args, **kwargs):
        SkilledPerson.__init__(self, *args, **kwargs)
        self.specialties = specialties
    
    def get_random_skill(self):
        return random.choice(self.specialties)


# And now, all of these "tests" should pass!

sarah = Hacker(
    name="Sarah",
    city="Vancouver",
    kungfoo=["Python", "PHP"],
    skill_level=10
)
stephen = Chef(
    name="Stephen",
    city="Toronto",
    specialties=["cakes", "pies"],
    skill_level=7
)
kim = Person(name="Kim", city="Seoul")

assert sarah.city == "Vancouver"
assert stephen.specialties == ["cakes", "pies"]
assert stephen.specialties[0] == "cakes"

assert kim.name == "Kim"
assert str(kim) == "Kim lives in Seoul"
kim.city = "Montréal"
assert str(kim) == "Kim lives in Montréal"

assert type(kim) == Person
assert type(sarah) == Hacker
assert type(stephen) == Chef

assert sarah.get_random_skill() in ["Python", "PHP"]

assert stephen.skill_level == 7
stephen.increase_skill_level(2)
assert stephen.skill_level == 9

assert sarah.kungfoo == ["PHP", "Python"]
sarah.add_kungfoo("Perl")
sarah.add_kungfoo("Java")
sarah.add_kungfoo("Java")
assert sarah.kungfoo == ["Java", "PHP", "Perl", "Python"]

print("All tests passed!")
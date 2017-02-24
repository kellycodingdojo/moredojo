

class Animal(object):
    def __init__(self, name):
    	self.name = name
    	self.health = 100

    def walk(self):
    	self.health -= 1
    	return self

    def run(self):
    	self.health -= 5
        return self

    def display(self):
    	print 'Your Animal has: ' + str(self.health) + ' health'


# cat = Animal('meow')
# cat.display()
#
# animal = Animal('grr')
# animal.walk().walk().walk().run().run().display()

class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.health = 150

	def pet(self):
		self.health += 5
        return self


snoop = Dog('roof')
snoop.run().run().pet().run().display()

class Human(object):
    def __init__(self, clan=None):
      print "New Human!!!"     # when we create a new human, we'll get self as an output
                               # initialize the clan instance variable by passing in a value
      self.clan = clan
      # initialize more attributes that will be the same for all humans
      self.health = 100
      self.strength = 3
      self.intelligence = 3
      self.stealth = 3
    def taunt(self):
      print "You want a piece of me?"
# create an instance of a human, pass in a clan name
michael = Human('CodingDojo')
jimmy = Human('CodingNinjas')



class Bike(object):
    def__init__(self)

    self.price = 200
    self.max_speed = 30
    self.miles = 0

    def displayInfo(self)
    print "The cost is:" + self.price
    print "The max speed is:" + self.max_speed
    print 'The milages is' + self.miles

fx_stlye = Bike('2000','25','0')

fx_stlye(display)
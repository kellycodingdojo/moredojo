


class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
            

    def display(self):
        print "The cost is: " + str(self.price)
        print "The max speed is: " + str(self.max_speed)
        print 'The milages is ' + str(self.miles)
        return self

    def ride(self):
        print  "you are riding 10 miles"
        self.miles += 10
        return self

    def backwards(self):
        print "wow you are going backwards"
        self.miles -= 5
        return self

fx_stlye = Bike(2000, 25, 0)

fx_stlye.ride().ride().ride().backwards().backwards().ride()

fx_stlye.display()
#fx_stlye.backwards()
fx_stlye.ride().ride()
fx_stlye.ride()
print fx_stlye.miles


   

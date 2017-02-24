



class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = 35
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12

    def display(self):
        print 'Price: ' + str(self.price)
        print 'Speed: ' + str(self.speed)
        print 'Fuel: '  + str(self.fuel)
        print 'Mileage: ' + str(self.mileage)
        print 'Tax: '   + str(self.tax)
        return self
# print \n "\nPrice"+ str(self.price) + "\nSpeed"+ str(self.speed)  <-- printing all on one line.



malibu = Car(12000, "35mph", 'Full', '15mpg')
camery = Car(9000, '45mph', 'Half', "20mpg")

malibu.display()
camery.display()


   

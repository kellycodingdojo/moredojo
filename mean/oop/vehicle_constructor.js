// function Transport(name,noise){
//     var car = {};
//     car.name = name;
//     car.noise = noise;
//     car.passengers = 0
//     car.sound=function(){
//     console.log(car.noise);
//     } 
//     car.pickup =function(num){
//          car.passengers = num;
//     }
//   return car;
//   }


// var Bike = Transport('bicycle','ring ring');
// Bike.sound();

// var Sedan = Transport('Convertable','Honk Honk!');
// Sedan.sound();

// var Bus = Transport('Big Blue', 'Beep Beep')
// Bus.sound();
// var busCount = Bus.pickup(3)
// console.log(Bus.passengers)

// function Bus(name,sound){
//   this.name=name;
//   this.sound=sound;
//   this.passengers = 0;
//   this.pickup= function(num){
//     this.passengers += num;
//     console.log(this.passengers);
//   }
// }

// var BigBlue = new Bus('bblue','beep beep');
// BigBlue.pickup(4)

// //<--------------------------------------------------Dojo code
// function VehicleConstructor(name, wheels, passengerNumber){
//   var vehicle = {};
// /*
//   Properties
// */
//   vehicle.name = name || "unicycle";
//   vehicle.wheels = wheels || 1;
//   vehicle.passengerNumber = passengerNumber || 0;
//   /*
//     methods
//   */
//   vehicle.makeNoise = function(noise){
//     var noise = noise || "Honk Honk";
//     console.log(noise)
//   }
//   /*
//   return
//   */
//   return vehicle;
// }

// var unicycle = VehicleConstructor();

// var bike = VehicleConstructor("bicycle", 2, 0);
// bike.makeNoise = function(){
//   console.log('ring, ring');
// }
// // or simply: bike.makenoise("ring, ring");
// var sedan = VehicleConstructor("sedan", 4, 4);
// sedan.makeNoise = function(){
//   console.log('Honk Honk');
// }

// var bus = VehicleConstructor('bus',6, 0);
// bus.pickupPassengers = function(newPassengers){
//   bus.passengerNumber += newPassengers;
// }

// console.log(bus.passengerNumber);
// bus.pickupPassengers(6);
// console.log(bus.passengerNumber);


//<---------------------------------------------------------------------
// part two! 

// function Transport(name,noise, wheels, speed){
//     var car = {};
//     car.name = name;
//     car.noise = noise;
//     car.wheels = wheels;
//     car.speed = 0;
//     car.traveled = 0; 
//     car.passengers = 0
//     car.sound=function(){
//     console.log(car.noise);
//     } 
//     car.pickup =function(num){
//          car.passengers = num;
//     }
//     car.travel = function(num){
//       car.speed += 2;
//       car.traveled += num;
//       console.log(car.traveled);
//       console.log(car.noise);
//     }
//   return car;
//   }


// var Bike = Transport('bicycle','ring ring', 2);
// Bike.sound();
// Bike.travel(5);

// // var Sedan = Transport('Convertable','Honk Honk!', 4);
// // Sedan.sound();

// // var Bus = Transport('Big Blue', 'Beep Beep', 6)
// // Bus.sound();
// // var busCount = Bus.pickup(3)
// // console.log(Bus.passengers)
// //<--------------------------------------------------------Dojo Code
// function VehicleConstructor(name, wheels, passengerNumber,speed){
//   if (!(this instanceof VehicleConstructor)){
//     return new VehicleConstructor(name,wheels,passengerNumber, speed);
//   }
//   /* Privates */
//   var distanceTraveled = 0;
//   var self = this;
//   function updateDistanceTraveled(){
//     distanceTraveled += self.speed;
//     console.log(distanceTraveled);
//   }
//   /* public */
//   this.speed = speed;
//   this.name = name || "unicycle";
//   this.wheels = wheels || 1;
//   this.passengerNumber = passengerNumber || 0;

//   this.makeNoise = function(noise){
//     var noise = noise || "Honk Honk";
//     console.log(noise)
//   };
//   this.move = function(){
//     this.makeNoise();
//     updateDistanceTraveled();
//   };
//   this.checkMiles = function(){
//     console.log(distanceTraveled);
//   };

// }

// var car = new VehicleConstructor('car', 4, 2, 40);
// car.move();
// car.checkMiles();
// console.log(car.speed);

//<---------------------------------------------------------------
// Part three!


var rnum = Math.floor((Math.random() * 10000000000000000) + 1);

function Transport(name,noise, wheels, speed, vin){
    var vin = vin;
    this.name = name;
    this.noise = noise;
    this.wheels = wheels;
    this.speed = speed;
    this.traveled = 0; 
    this.passengers = 0
    this.getSSN = function(){
      return vin;
    }
    };
    Transport.prototype.sound=function(){
    console.log(this.noise);
    return this;
    };
    Transport.prototype.pickup =function(num){
         this.passengers = num;
         return this;
    };
    Transport.prototype.travel = function(num){
      this.speed += 2;
      this.traveled += num;
      console.log(this.traveled);
      console.log(this.noise);
      return this;

    }

var convertable = new Transport('the whip', 'honk', 4, 99, rnum);
console.log(convertable.travel())
console.log(convertable.getSSN())
  
  
//<----------------------------------------------------------------dojo code
function VehicleConstructor(name, wheels, passengerNumber,speed){
  if (!(this instanceof VehicleConstructor)){
    return new VehicleConstructor(name,wheels,passengerNumber, speed);
  }
  // String used to generate vin number
  var chars = "0123456789ABCEDGHIJKLMNOPQRSTUVWXYZ";

  this.distanceTraveled = 0;
  this.speed = speed;
  this.name = name || "unicycle";
  this.wheels = wheels || 1;
  this.passengerNumber = passengerNumber || 0;
  // Invoke createVin to generate random vin number
  this.vin = createVin();

  function createVin(){
    var vin = '';
    for (var i = 0; i < 17; i+=1 ){
      // Use Math.floor and Math.random to generate random index to access character from char string
      vin += chars[Math.floor(Math.random()*35)];
    }
    return vin;
  }

}

VehicleConstructor.prototype.makeNoise = function(noise){
  var noise = noise || "Honk Honk";
  console.log(noise);
  return this;
};

VehicleConstructor.prototype.move = function(){
  this.makeNoise();
  this.updateDistanceTraveled();
  return this;
};

VehicleConstructor.prototype.checkMiles = function(){
  console.log(this.distanceTraveled);
  return this;
};

VehicleConstructor.prototype.updateDistanceTraveled = function(){
  this.distanceTraveled += this.speed;
  console.log(this.distanceTraveled);
  return this;
}

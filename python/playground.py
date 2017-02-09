'''
def od_even(a,b):
    for num in range(a,b):
        if num % 2 == 0:
            print("Num is", num, "This is an even num" )
        else:
            print ("Num is", num, "This is an odd num" )


a = [2,4,10,16]

def multiply(arr,num):
  a = [2,4,10,16]
  b = multiply(a,5)
  print b

def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)

print b


import random
random_num = random.randint(0,100)

def grades():
    if random_num < 60:
        print "fail"
    elif random_num > 60 and random_num < 70:
        print("Score: ", random_num, "; Your grade is D")
    elif random_num > 70 and random_num < 80:
        print("Score: ", random_num, "; Your grade is C")
    elif random_num > 80 and random_num < 90:
        print("Score: ", random_num, "; Your grade is B")
    elif random_num > 90 and random_num <= 100:
        print("Score: ", random_num, "; Your grade is A")
    print("End")
print grades()


import random


heads = 0
tails = 0

for count in range(0,5000):
    random_num = round(random.random())
    x = random_num
    if x == 0:
        heads += 1
        print "Attempt # {} Throw coin....It's heads!....Got  {} heads so far and {} tails so far!".format(count,heads,tails)
    else:
        tails += 1
        print "Attempt # {} Throw coin....It's Tails!....Got {} heads so far and {} tails so far!".format(count,heads,tails)

print x


x = [4, "ehllo", 1, 3, 5, 7, 25]

def star(arr):
    for index in range(len(arr)):
        if type(x[index]) == str:
            first = x[index]
            first = first[0].lower()
            for index in range(len(x[index])):
                print first,
        else:
                for index in range(x[index]):
                    print '*',
        print ''
star(x)



students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for counter in range(len(students)):
     print students[counter]["first_name"]," " + students[counter]["last_name"]

'''

users = {
 'students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for key, data in users.items():
     print key
     count = 1
     for value in data:
         print count,value["first_name"], ": ", value["last_name"], len(value["first_name"]) + len(value["last_name"])
         count += 1

                                #en(users["Students"][i]["first_name"])

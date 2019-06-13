while True:
  # Setting up vairables
  myNumber = input("What number would you like to use? ")
  myNumber1 = input("What is the second number you'd like to use? ")

  # Checks that the user entered a correct value 
  if myNumber.isdigit() == False or myNumber1.isdigit() == False:
    print("Not a number ")

    # Turns the users value into an integer so it can be manipulated 

  else:
    myNumber = int(myNumber)
    myNumber1 = int(myNumber1)
    break
  
# count to enable multiplication
count = 1

# Arrays to check hold multiples
myNumList1 = []
myNumList2 = []

# Checks if the lists contain similar elements and will print them if they are the same

def commonMultiple(myNumList1, myNumList2):
  result = False

  for x in myNumList1:
    for y in myNumList2:
      if x == y:
        result = True
        print(x, "is a multiple" )
        
   
# Number 1
print(myNumber, "x", count, "=")
multi = int((myNumber * count))
print(multi)
myNumList1.append(multi)


# Number 2
print(myNumber1, "x", count, "=")
multi1 = int((myNumber1 * count))
print(multi1)
myNumList2.append(multi1)
count = count + 1


while True:

    # Allows to exit, repeat or show 
  myExit = input("If you'd like to exit, enter 1; to repeat, enter 0; to print arrays, enter 2; to check for common multiples, enter 3. ")

  if myExit == "0":

    # Number 1
    print(myNumber, "x", count, "=")
    multi = int((myNumber * count))
    print(multi)
    myNumList1.append(multi)

    # Number 2
    print(myNumber1, "x", count, "=")
    multi1 = int((myNumber1 * count))
    print(multi1)
    myNumList2.append(multi1)

    # if the numebr is the same it will add it to a seperate list
    if multi == multi1:
      commonMultiples.append(multi) 
    else:
      pass

    count = count + 1
    pass


  elif myExit == "1":
    print("Thank you")
    break
  elif myExit == "2":
    print(myNumList1)
    print(myNumList2)
  elif myExit == "3":
    commonMultiple(myNumList1,myNumList2)
  else:
    print("Logic error")
    pass

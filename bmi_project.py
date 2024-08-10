# BMI - Body Mass Index

name = input("Enter you name: ")
Height = float(input("Enter your Height in Centimeters: "))
Weight = float(input("Enter your Weight in Kg: "))

Height = Height/100
BMI = Weight/(Height*Height)

print("Your Body Mass Index is: ",BMI)

if(BMI>0):
    if(BMI<18.5):
        print(name +", you are underweight.")
    elif(BMI<=24.9):
        print(name +", you are normal weight.")
    elif(BMI<=29.9):
        print(name +", you are overweight. You need to exercise.")
    elif(BMI<=34.9):
        print(name +", you are obese.")
    elif(BMI<=39.9):
        print(name +", you are severely obese.")
    else:
        print(name +", you are morbidly obese.")
else:
    print("Enter valid details...")
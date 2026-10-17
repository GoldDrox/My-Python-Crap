#Simple Password Detector
code = ""
truecode0 = "668800"
truecode1 = "885552"
truecode2 = "333771"
truecode3 = "111119"
maxchar = 6
chances = 3

while code != truecode0 and chances > 0:
    code = (input("Input A Password: "))
    codechar = len(code)
    if codechar > maxchar:
        print("Password Is Too Long, Maximum Of 6 Characters")
    else:
        print("Password Is Too Short, Minimum Of 6 Characters")

    #convert the string into an integer
    etc = int(code)

    if etc == truecode0 or etc == truecode1 or etc == truecode2 or etc == truecode3:
        print("Welcome User")
        break
    else:
        print("Your Password Is Incorect")
        chances = chances - 1
        print(chances)




#Clock And Week Counter
import datetime
present = datetime.datetime.now().weekday()
time = datetime.datetime.now().time()

#Clock
print(f"{time.hour} : {time.minute} : {time.second}")
#f strings can also use "and" or "or" functions i think

#Weekday
if present == 0:
    print("Monday")
elif present == 1:
    print("Tuesday")
elif present == 2:
    print("Wendsday")
elif present == 3:
    print("Thursday")
elif present == 4:
    print("Friday")
elif present == 4:
    print("Saturday")
else:
    print("Sunday")




# More Examples

# istrue = 1 == 1
# will print true

# flalse = 1 != 2
# will print false
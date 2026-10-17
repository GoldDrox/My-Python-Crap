# for var in range(10):
#     print(var)

# star = "*"
# for i in range(5):
#     print(star * i)

# for l in range(5, 0, -1):
#     print(star * l)


var = ["Pies", "Cakes", "Cheese"]
# for stuff in var:
#     print(stuff)


# this grabs index 1 from var array and replaces it
var[1] = "Strawberry"

# this adds a string to the var array can only be 1
# var.append("Blueberries")

# same thing with append but supports multiple strings needs to use its own array too
# var.extend(["Pizza", "French Toast", "Vanilla Ice-Cream"])

# select where to add a string in an array
var.insert(1, "Pepper")

# removes a string inside an array
var.pop(1)

# exports the indexes from the var array
# print(var[0:2])



numray = [0, 1, 2, 3, 4, 5]
numray.reverse()

print(numray)

# prints indexes from 2 > end of array
# print(numray[2:])

# prints indexes from start of array > index number 4
# print(numray[:4])

# grabs even indexes
# print(numray[::2])

# grabs odd indexes
# print(numray[1::2])



# altroots = []
# for i in range(1, 11):
#     altroots.append(i ** 2)

# prints root powers with the range of i
# print("Root Powers: ", altroots)

# altroots2 = [l ** 2 for l in range(1,11)]
# print("Root Powers: ", altroots2)



# randomarray = [4, 2, 5, 6, 9, 8,]

# sorts from largest to smallest
# randomarray.sort(reverse=True)

# counts & prints ammount of indexes 
# print(randomarray.__len__())



# todo = []
# action = ""

# while action != "0":
#     action = (input("What Do You Want To Do? "))
#     if action == "1":
#         add = input("Add A Task: ")
#         todo.append(add)

#     elif action == "2":
#         delete = int(input("Delete A Task With Index: "))
#         todo.pop(delete)

#     elif action == "3":
#         editdex = int(input("Select An Index "))
#         edittex = input("Write Task: ")
#         todo[editdex] = edittex
        
#     else:
#         break

#     print(todo)



def addtsk(addtask, aptodo):
    aptodo.append(addtask)

def remtsk(remtask, aptodo):
    aptodo.pop(remtask)

def edit(eddex, edtex, aptodo):
    aptodo[eddex] = edtex

todo = []
action = ""

while action != "0":
    action = (input("What Do You Want To Do? "))
    if action == "1":
        add = input("Add A Task: ")
        addtsk(add, todo)

    elif action == "2":
        delete = int(input("Delete A Task With Index: "))
        remtsk(delete, todo)

    elif action == "3":
        editdex = int(input("Select An Index "))
        edittex = input("Write Task: ")
        edit(editdex, edittex, todo)
    else:
        break

    print(todo)
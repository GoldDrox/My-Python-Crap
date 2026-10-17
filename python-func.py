# def greeting():
#     print("Hello, World!")

# def name(stock):
#     print("User", stock)

# def age(octane, hecate):
#     print(16, octane, hecate)

# greeting()
# name("Rici")
# age("Years Old", "Im Old!")



# def multi(num1, num2):
#     result = num1 * num2
#     print(result)

# def add(num1, num2):
#     result = num1 + num2
#     print(result)

# def neg(num1, num2):
#     result = num1 - num2
#     print(result)

# def multi2 (num1, num2):
#     result = num1 * num2
#     return result

# multi(25, 20)
# add(12, 8)
# neg(90, 80)
# newvar = multi2(25, 20)
# print(newvar)



def instpkg(name, ver="Latest", verbose=False):
    if verbose:
        status = f"installing {name} v{ver}"
    else:
        status = f"{name} installed"
    temp = len(name) * 10
    success = True

    return status, temp, success

msg, size, ok = instpkg(verbose=True, name="firefox")

print(f"status: {msg}")
print(f"Package Size: {size} MB")
print(f"Success: {ok}")



def hecate(ary, tex):
    ary.append(tex)

arrays = []
tex = "Fish Oil"
hecate(arrays, tex)
print(arrays)
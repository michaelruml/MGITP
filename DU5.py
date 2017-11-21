#TODO:
#add, substract, multiply, divide, pythagorian, factorial


# Adds two numbers
def add(x, y):
    return x+y


# Returns a result of a Pythagorian equation
def pyth(x, y, z): 
    return 0
    #TODO


#Get and process input
def parse_input():
    inp = input('Your input: ')
    par = inp.split(' ')
    return par

#Get a result from an appropriate function
def get_result(par_list):
    result = -1
    if op == "+":
        result = add(par[0], par[1])
    elif op == "pyth":
        if len(par) != 3:
            print("Not enough parameters, returning -1 instead")
        else: 
            result = pyth(par[0], par[1], par[2])
    return result

print("Welcome to Stupid Calculator!")
print("The supported operations are:")
print("- Add. To add, provide an input in this format: \"+ 1 2\"")
par = parse_input()
op = par.pop(0)
par = [int(x) for x in par];
result = get_result(par)
print("And the result is: ", result)
#############################################################################
#                                                                           #
#   Copyright 2020 Daniel Bryce Beetham                                     #
#                                                                           #
# Licensed under the Apache License, Version 2.0 (the "License");           #
# you may not use this file except in compliance with the License.          #
# You may obtain a copy of the License at                                   #
#                                                                           #
#    http://www.apache.org/licenses/LICENSE-2.0                             #
#                                                                           #
# Unless required by applicable law or agreed to in writing, software       #
# distributed under the License is distributed on an "AS IS" BASIS,         #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  #
# See the License for the specific language governing permissions and       #
# limitations under the License.                                            #
#                                                                           #
#############################################################################



# SymPy is a symbolic manipulation library (ie. a CAS) written in Python!
import sympy as sp

#Pretty Table will allow us to show our data in a nice way
import prettytable as pt

# Define SymPy variables for use with our program
x = sp.symbols('x') # generic x for our calculations (

# f, f_prime = symbols('f f_prime', cls=Function)
f = None
f_prime = None

xold = None #This is our first guess at a root
xnew = None #This is our first calculated value
tolerance = 6 # How many places to round to
max_tries = 50 # Maximum number of times to iterate

#Initalise pretty printing from SymPy. Will Use LATEX if available!
sp.init_printing()

print("Newton Raphson Solver")
print("---------------------")
print("\n")


#Try and get an expression for the f(x) to solve roots for
goodexpression = False
while goodexpression == False:
    
    print("Please enter a function to find roots: (Use Phython Synxtax like the following\na*x**2 + b*x + c -sqrt(x) -cos(x):")
    f_text = input("")
    
    try:
        # This is quite likely to fail, so we need to catch an exception for sure!
        f = sp.sympify(f_text)
    except:
        print("\n")
        print("Error! This function is ill defined - remember that you need to use phython syntax (with an x for the function variable)")
        print("\n")
    else:
        #differentiate f
        f_prime = sp.diff(f, x)

        print("\n")
        print("---------------------")
        print("\n")

        print("This is f(x) as it's been interpreted:\n")
        sp.pprint(f)

        print("\n")
        print("Here is f'(x):\n")
        sp.pprint(f_prime)

        print("\n")
        
        print("Are the functions correct? y/n")
        proceed = input("")
        
        if proceed == 'n':
            goodexpression = False
        else:
            goodexpression = True

#Enter a guess, and check the value
goodexpression = False
while goodexpression == False:
    print("\n")
    print("Enter a guess for the root:\n")
    guess = input()
    
    try:
        xold = sp.sympify(guess)
    except:
        print("This can't be processed by SymPy (it probably isn't even an expression)\nTry again...")
    else:
        if xold.is_real == True:
            goodexpression = True
        else:
           print("This isn't a real value, try again...")
    
n = 0
t = pt.PrettyTable(["X_n","F(n)","F'(n)","X_n+1"])


while n <= max_tries:
    
    #This is the actual Newton/Raphson Method (one line of code!)
    xnew = xold - (f.subs(x, xold)/f_prime.subs(x, xold))
    
    #print loading dots (only useful for big complicated functions)
    print(".", end="")
    
    t.add_row([xold, f.evalf(subs={x: xold}), f_prime.evalf(subs={x: xold}), xnew.evalf()])
    
    if xold.round(tolerance) == xnew.round(tolerance):
        break
    
    xold = xnew.evalf()
    
    n = n + 1

print("\n")
print(t)

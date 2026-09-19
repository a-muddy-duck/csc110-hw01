# ------------------------------------------------------
#        Name: Ash Rulifson
#       Peers: (add any collaborators)
#  References: Textbook (How to Think Like a Computer Scientist)
# ------------------------------------------------------


def main():
    """
    This is a Docstring for the main function. This is the short description.

    Here, after a blank line, you can add a longer paragraph description.
    Docstrings are like long comments that we put right under the function definition.
    The Docstring goes from one set of "opening" three double-quotes to
    another set of "closing" three double-quotes. We also try to keep the lines short.
    The Docstring has 4 sections:
      - the short one-line description
      - the paragraph description
      - the Params section that indicates input parameters and return values
      - the "how to run" section called "Example Use".

    PARAMS:
        - None. If the function took an input int of "apples" called num, we would
                indicate it like this: - num: int with number of apples
    RETURNS:
        - None. If the function returned something (like the integer half of num),
                we would indicate it like this: int : integer half of num
        to test code: run in command prompt (within wd hw01): python -m pytest -v -s
    """

    # ========== Setup for HW. DO NOT MODIFY ======
    x=0
    y=0
    a=0
    b=0
    c=0
    result1 = 0
    result2 = 0
    result3 = 0
    result4 = 0
    result5 = 0
    # End of Setup code ---------------------------



    # Part 1: Basic Operations
    # =============================================
    # Your code for part 1 under this line and before the print statements
# reassign variables
x = 27
y = 1
a=1.5
b=7
c=-1

# write math for result1
result1 = ((3*x) - (9*y))/((2*a)*(b-c))

# print results
for loopvariable in[f"x = {x}", f"y = {y}", f"a = {a}", f"b = {b}", f"c = {c}", f"result = {result1}"]:
    print("Part 1:", loopvariable)
    
    # End of Part 1 ---------------------- 


    # Part 2: Power
    # =============================================
    # Your code for part 2 under this line and before the print statements
# overwrite variables
x =5
y= -3

# do math
result2 = x**2*y**4

#print results
print("Part 2: x =", x)
print("Part 2: y =", y)
print("Part 2: result =", result2)
    # End of Part 2 ---------------------- don't forget to add and commit after part 2



    # Part 3: Integer divide
    # =============================================
    # Your code for part 3 under this line and before the print statements
# overwrite variables
a = 100 #treats
b=13 #dogs

#math & print
result3 = a//b
print("Part 3: a =",a)
print("Part 3: b =",b)
print("Part 3: result =",result3)
    # End of Part 3 ----------------------


    # Part 4: Modulo
    # =============================================
    # Your code for part 4 under this line and before the print statements
#math & print
result4 = a%b

print("Part 4: result =", result4)
    # End of Part 4 ----------------------

if __name__ == "__main__":
    main()

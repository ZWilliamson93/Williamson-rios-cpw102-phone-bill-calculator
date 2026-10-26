extra_Gb_cost = 2
base_Gb = 10

"""We cannot have regular numbers in our code without context. Without global variables to attach
our numbers to, our other coders will lack context to what the numbers mean, especially for
base costs and dollars per Gb.
"""

def data_usage(Gb, base_Gb, base_cost, extra_Gb_cost):
    Gb = Gb - base_Gb
    total_bill = base_cost
    if Gb > 0:
        if 5 > Gb:
            print(f"You are {Gb} over your limit.")
            print("Moderate extra usage.")
            total_bill = (Gb * extra_Gb_cost) + base_cost

        else:
            print(f"You are {Gb} GB over your limit.")
            print("High extra usage.")
            total_bill = (Gb * extra_Gb_cost) + base_cost
    
    else:
        print("You are within your data limit.")
    return total_bill


"""
(1) calculate total bill only if we exceed maximum of base Gb usage. Multiply surplus with
$ per Gb. We need to nestle if-else statements, but we also need boolean functions as well.
We need to make true/false statement that will determine how the code manifests. In our base
code, we have the proper output, but what we need is the specific code to follow the 
instructions.

We need a thing that will fill in the "True" and a thing that fills in the "False".
"""


def main():
    Gb = float(input("Enter data used in GB: "))
    base_cost = float(input("Enter base plan cost: "))
    total_bill = data_usage(Gb, base_Gb, base_cost, extra_Gb_cost)
    print(f"Your total bill is: ${total_bill:.2f}")

"""
For our main code, we need to produce numbers for our variables, which vary between our
phone clients. Also, we'll need to perform if-else and boolean functions to calculate (1) total
costs, (2) determine how many Gb over the limit, and (3) how high over the limit our client is over
their base plan. After the calculations, it will print out all three.
"""


main()


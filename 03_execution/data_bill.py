extra_Gb_cost = 2
base_Gb = 10

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


def main():
    Gb = float(input("Enter data used in GB: "))
    base_cost = float(input("Enter base plan cost: "))
    total_bill = data_usage(Gb, base_Gb, base_cost, extra_Gb_cost)
    print(f"Your total bill is: ${total_bill:.2f}")
    


main()

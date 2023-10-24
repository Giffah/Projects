def main():
    print("This program converts Ghana Cedis to USD")
    print()

    cedi = eval(input("Enter amount in Ghana Cedis: "))
    USD = convert_to_USD(cedi)
    print("This is",USD,"USD")

convert_to_USD= lambda cedi: cedi*0.085

main()
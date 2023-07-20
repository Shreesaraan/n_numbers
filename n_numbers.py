def n_numbers(range):
    if range==1:
        print(1,end=" ")
        return
    n_numbers(range-1)
    print(range,end=" ")

range=int(input("Enter the Range : "))
n_numbers(range)
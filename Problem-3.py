#Problem-3.py
#input: a --> as integer
#Output : odd number series from 1 to n with thw given length : 

#Rules as mentioned on the problem statement
# if a is odd --> a terms needs to print
# if a is even --> a+1 terms needs to print

#Examples: 
# a = 1 --> 1
# a = 2 --> 1
# a = 3 --> 1,3,5
# a = 4 --> 1,3,5
# a = 5 --> 1,3,5,7,9
# a = 6 --> 1,3,5,7,9


#Here for the output I'm using the same logic as in Problem-2.py to generate odd numbers also that the same join method to print the list in desired format


if __name__ == "__main__":
    a = int(input("a = "))

    if a % 2 == 0:
        n = a - 1
    else:
        n = a

    result = []

    for i in range(1, n+1 ):
        odd = 2 * i - 1
        result.append(str(odd))

    print("Output : ", " , ".join(result))




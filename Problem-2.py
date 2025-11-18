#Problem-2.py

# Second problem - With a single integer as the input --> generate the following until a = x [1,3,5,...,x]

# Output : a list of odd numbers from 1 to x 

#Example : 
# a = 1 -> 1
# a = 3 -> 1,3,5

#here i am taking input and generating the list of odd numbers
#I am using the formula for generating odd numbers : 2 * n - 1 where n
#Here i am using string join to print the list in the desired format


if __name__ == "__main__":
    a = int(input("a = "))

    result = []

    for i in range(1, a+1 ):
        od = 2*i -1
        result.append(str(od))

    print("Output : ", " , ".join(result))
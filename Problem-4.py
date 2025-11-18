#Problem-4.py
# Fourth problem - Get the total count of number listed in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]
# Input : A list of integers [1,2,8,9,12,46,76,82,15,20,30]
# Output : {1:11,2:8,3:4,4:4,5:3,6:2,7:0,8:1,9:1}

if __name__ == "__main__":

    input_lst = input("Enter a list of integers separated by commas: ")
    numbers = list(map(int, input_lst.split(",")))

    # sir! here the input format must be in the form of comma separated values without spaces
    # example : 1,2,3,4,5,6


    mul_count = {i : 0 for i in range(1, 10)}

    for num in numbers: 
        for i in range(1, 10):
            if num % i == 0:
                mul_count[i] += 1



    print("Output :", mul_count)



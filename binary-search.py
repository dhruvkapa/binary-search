print("Binary search algorithm")
print("-----------------------")


list_of_nums = []
inputLenOfList = int(input("Enter the length of list: "))

getNumFromUser = int(input("Enter a number between 0 and the inputted length of the list: "))
print("\n")




def fill_list_with_num(input):
    i = 0
    while i < input:
        list_of_nums.append(i)
        i += 1

fill_list_with_num(inputLenOfList)




lowIndex = 0
highIndex = len(list_of_nums)
midIndex = (lowIndex + highIndex)//2
num_of_splits = 0



isTrue = True

if midIndex == getNumFromUser:
    print("Found it: {}".format(list_of_nums[midIndex]))
    print("Total number of splits: {}".format(num_of_splits))
    isTrue = False


while isTrue:
    num_of_splits += 1
    if midIndex < getNumFromUser: # 50, 62

        print("First half of list (List 1): {}".format(list_of_nums[lowIndex:midIndex]))
        print("Second half of list (List 2): {}\n".format(list_of_nums[midIndex:highIndex]))
        print("Proceeding to search second half of list (List 2)...")
        print("Split # {}".format(num_of_splits))
        print(list_of_nums[midIndex:highIndex])
        print("\n")

        lowIndex = midIndex
        highIndex = highIndex
        midIndex = (lowIndex + highIndex) //2

        if midIndex == getNumFromUser:
            print("Found it: {}".format(list_of_nums[midIndex]))
            print("Total number of splits: {}".format(num_of_splits))
            isTrue = False

    elif midIndex > getNumFromUser:  #   32 ,50

        print("First half of list (List 1): {}".format(list_of_nums[lowIndex:midIndex]))
        print("Second half of list (List 2): {}\n".format(list_of_nums[midIndex:highIndex]))
        print("Proceeding to search first half of list (List 1)...")
        print("Split # {}".format(num_of_splits))
        print(list_of_nums[lowIndex:midIndex])
        print("\n")


        lowIndex = lowIndex
        highIndex = midIndex
        midIndex = (lowIndex+highIndex)//2

        if midIndex == getNumFromUser:
            print("Found it: {}".format(list_of_nums[midIndex]))
            print("Total number of splits: {}".format(num_of_splits))
            isTrue = False

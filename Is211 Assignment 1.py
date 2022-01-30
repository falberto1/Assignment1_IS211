'''
1.Create a function named listDivide that takes in two parameters.
One parameter is a list called numbers. The second parameter is
an integer called divide. The divide parameter should have a default value of 2
'''


def listDivide(numbers, divide=2):
    # varibale that count the number divisible by divide in the list
    count = 0

    # condition check for empty list
    if (len(numbers) == 0):
        return 0

    # loop around the element of list
    for i in numbers:
        try:
            # check for divisibility
            if (i % divide == 0):
                # increment the counter
                count += 1

                # 3. Create acustom exception class called 'ListDivideException'. This should be two lines of Python code.
        except:
            return 'Error: ListDivideException'

    # 2. The function returns the number of elements in the numbers list that are divisible by divide.
    return count


# 4. create another function called testListDivide that performs the following tests on listDivide:
def testListDivide():
    # listDivide([1,2,3,4,5]) should return 2
    print(listDivide([1, 2, 3, 4, 5]))

    # listDivide([2,4,6,8,10]) should return 5
    print(listDivide([2, 4, 6, 8, 10]))

    # listDivide([30, 54, 63,98, 100], divide=10) should return 2
    print(listDivide([30, 54, 63, 98, 100], divide=10))

    # listDivide([]) should return 0
    print(listDivide([]))

    # listDivide([1,2,3,4,5], 1) should return 5
    print(listDivide([1, 2, 3, 4, 5], 1))


testListDivide()
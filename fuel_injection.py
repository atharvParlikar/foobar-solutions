# basic plan:
# make a function to get the numbers

def getNumbers(n):
    if n % 2 == 0:
        return [n / 2]
    else:
        return [(n + 1), (n - 1)]


def inList(list1, list2):
    for i in list1:
        if i not in list2:
            return False
    return True


def solution(n):
    n = int(n)
    isodd = True if n % 2 == 0 else False
    list_ = [n]
    counter = 0

    while 1 not in list_:
        test = []
        for n in list_:
            if not inList(getNumbers(n), list_):
                test = getNumbers(n)
        list_ += test
        counter += 1
    return counter if isodd else counter - 1


def test():
    if solution('4') == 2:
        print("TEST 1 PASSED!!!")
    else:
        print("TEST 1 FAILED!!!")

    if solution('15') == 5:
        print("TEST 2 PASSED!!!")
    else:
        print("TEST 2 FAILED!!!")


test()

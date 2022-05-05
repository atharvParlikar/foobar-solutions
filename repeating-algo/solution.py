# 1. convert it to string and find k, then do the base substraction shit also strings are better for sorting the numbers and later joining them

def dec_to_base(num, base):
    base_num = ""
    while num > 0:
        dig = int(num % base)
        base_num += str(dig)
        num //= base

    base_num = base_num[::-1]
    return base_num


def solution(n, b):
    minions = []
    while n not in minions:
        minions.append(n)
        k = len(n)
        assending = int(''.join(sorted([x for x in n], reverse=True)), b)
        desending = int(''.join(sorted([x for x in n])), b)
        nextid = str(dec_to_base(assending - desending, b))
        n = nextid if len(nextid) == k else ('0' * (k - len(nextid))) + nextid
    return len(minions) - minions.index(n)


print(solution('210022', 3))


# 5C5 = 1
# 5C1 = 5

# nCn = 1
# nC1 = n
# nCk = n! / k!(n-k)!
# nCk = nC(n-k)

def choose(n:int, k:int) -> int:
    if n < k:
        raise Exception('k must be less than or equal to n')
        return
    if n == k: return 1
    if k == 1: return n

    # either just take k or take both n and k
    return choose(n, k-1) + choose(n-1, k-1)

if __name__ == '__main__':
    i = choose(2,2) * choose(2,1)
    print(i)


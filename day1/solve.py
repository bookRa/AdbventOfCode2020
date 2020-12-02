from typing import DefaultDict, Dict, Iterable, List, Set, Tuple

def input_to_list(path: str):
    with open(path, 'r') as f:
        result: List[int] = list(map(lambda x: int(x), f.read().splitlines()))
    print(f"found {len(result)} entries")
    return result

def twoSum(l: List[int], sum: int) -> Tuple[int, int]:
    store: Set[int] = set()
    for i in l:
        if i in store:
            return (i, sum-i)
        else:
            store.add(sum-i)
    raise Exception("not all were ints")

assert(twoSum([-2, 8, 3, 4, 5], 6) == (8,-2))

x1, x2 = twoSum(input_to_list('./input.txt'), 2020)
answer = x1 * x2
print("first answer")
print(answer)

def threeSum(l: List[int], sum: int = 2020) -> Tuple[int, int, int]:
    d: Dict[int, List[int]] = DefaultDict(lambda: [])
    for idx,val in enumerate(l):
        d[sum-val].append(idx)
    
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            x, y = l[i], l[j]
            z = x+y
            if z in d:
                if any([k not in [i,j] for k in d[z]]):
                    return (x, y, sum-z)
    raise Exception("no three sum found")

assert(sum(threeSum([3, 4, 5, 8, -9, 4, 5], 4))==4)

a1, a2, a3 = threeSum(input_to_list('./input.txt'), 2020)
print("second answer")
print(a1*a2*a3)
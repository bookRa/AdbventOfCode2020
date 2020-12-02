from typing import List, Set, Tuple

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

x1, x2 = twoSum(input_to_list('input.txt'), 2020)
answer = x1 * x2
print(answer)
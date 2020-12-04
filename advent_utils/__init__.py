from typing import List


def input_to_int_list(path: str):
    with open(path, 'r') as f:
        result: List[int] = list(map(lambda x: int(x), f.read().splitlines()))
    print(f"found {len(result)} entries")
    return result

def input_to_str_list(path: str):
    with open(path, 'r') as f:
        result: List[str] = f.read().splitlines()
    print(f"found {len(result)} entries")
    return result

# def split_by_double_lines(path:str):
#     with open(path, 'r') as f:
#         result: List[str] = f.read().spli
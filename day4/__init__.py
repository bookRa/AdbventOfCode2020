


from typing import Dict, List
import re

def get_kv_pairs(path:str) -> List[Dict[str,str]]:
    """
    splits based on provided input
    """
    result = []
    with open(path, 'r') as f:
       passport_blocks = f.read().split("\n\n") 
    
    for block in passport_blocks:
        # split on both newlines and spaces
        def colon_to_tuple(raw_string):
            pair = raw_string.split(':')
            return (pair[0], pair[1])
        myd = dict([colon_to_tuple(p) for p in block.split()])
        result.append(myd)
    return result


def valid_passports(path:str) -> int:
    valid_count = 0
    required_keys = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    
    all_dicts = get_kv_pairs(path)
    for doc in all_dicts:
        keys = set(doc.keys())
        if not required_keys - keys:
            valid_count +=1
    return valid_count

def extra_valid(path:str) -> int:
    valid_count = 0
    def validate_hgt(s):
        m = re.match(r"^(\d{2,3})((cm)|(in))$", s)
        if m:
            val = m.group(1)
            unit = m.group(2)
            if unit == 'cm':
                return 150 <= int(val) <= 193
            if unit == 'in':
                return 59 <= int(val) <= 76
        else:
            return False
    def validate_hcl(s):
        m = re.match(r"^\#([0-9]|[a-f]){6}$", s)
        if m: return True
        else: return False
    def validate_ecl(s):
        return bool(re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$", s))
    rules = {
        'byr': lambda x: 1920 <= int(x) <= 2002,
        'iyr': lambda x: 2010 <= int(x) <= 2020,
        'eyr': lambda x: 2020 <= int(x) <= 2030,
        'hgt': validate_hgt,
        'hcl': validate_hcl,
        'ecl': validate_ecl,
        'pid': lambda s: bool(re.match(r"^\d{9}$", s))
    }
    all_dicts = get_kv_pairs(path)
    for doc in all_dicts:
        print(f"looking at {doc}")
        is_valid = True
        for k,f in rules.items():
            if k not in doc:
                print(f"{k} not in curr_dict, breaking")
                is_valid = False
                break
            elif not f(doc[k]):
                print(f"validation {k} returned {f(doc[k])}, breaking")
                is_valid = False
                break
        if is_valid:
            # print(f"{doc} was valid!!!!")
            valid_count +=1
    print(f"found {valid_count} valid")
    return valid_count
               


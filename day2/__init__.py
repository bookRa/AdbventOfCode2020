from typing import List

def valid_passwords(strings: List[str]) -> List[str]:
    answer = []
    for p in strings:
        counts, letter, password = p.split()
        min_occ, max_occ = map(lambda x: int(x), counts.split('-'))
        letter = letter[0]
        occ = 0
        for l in password:
            if l == letter:
                occ +=1
            if occ > max_occ:
                break
        if min_occ <= occ <= max_occ:
            answer.append(p)
    return answer


def passwords_redux(strings: List[str]) -> List[str]:
    answer = []
    for p in strings:
        pos, letter, password = p.split()
        pos1, pos2 = map(lambda x: int(x)-1, pos.split('-'))
        letter = letter[0]
        occ = 0
        if password[pos1] == letter: occ +=1 
        if password[pos2] == letter: occ +=1
        if occ == 1: answer.append(p)
    return answer
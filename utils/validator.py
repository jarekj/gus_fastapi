import re

def is_regon_valid(check: str) -> bool:
    if not re.match('^([\d]{9}|[\d]{14})$', check):
        return False
    
    chars = list(map(int, check))

    if len(check) == 9:
        checksum = sum(
            map(
                lambda weight, digit: weight * digit, 
                (8, 9, 2, 3, 4, 5, 6, 7), 
                chars[slice(0, 8)]
            )   
        ) % 11
        return checksum % 10 == chars[8]
    else:
        checksum = sum(
            map(
                lambda weight, digit: weight * digit, 
                (2, 4, 8, 5, 0, 9, 7, 3, 6, 1, 2, 4, 8), 
                chars[slice(0, 13)]
            )   
        ) % 11
        return checksum % 10 == chars[13]

def is_nip_valid(nip: str) -> bool:
    nip = nip.replace('-', '')
    if len(nip) != 10 or not nip.isdigit(): 
        return False
    digits = [int(i) for i in nip]
    weights = (6, 5, 7, 2, 3, 4, 5, 6, 7)
    check_sum = sum(d * w for d, w in zip(digits, weights)) % 11
    return check_sum == digits[9]

def is_krs_valid_length(krs: str) -> bool:
    if len(krs) != 10:
        return False
    if not krs.isdigit():
        return False
    return True

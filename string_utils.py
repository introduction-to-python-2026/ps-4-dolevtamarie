def split_before_each_uppercase(formula):
    if not formula:
        return []
    parts = []
    start = 0
    for i, char in enumerate(formula[1:], start=1):
        if char.isupper():
            parts.append(formula[start:i])
            start = i
    parts.append(formula[start:])
    return parts

def split_at_digit(formula):
    for i, char in enumerate(formula):
        if char.isdigit():
            return (formula[:i], int(formula[i:]))
    return (formula, 1)

def split_formula(formula):
    return [split_at_digit(part) for part in split_before_each_uppercase(formula) if part]
    

def split_before_each_uppercase(formula):
    if not formula:
        return []
    parts = []
    start = 0
    for i in range(1, len(formula)):
        if formula[i].isupper():
            parts.append(formula[start:i])
            start = i
    parts.append(formula[start:])
    return parts

def split_at_digit(formula):
    for i in range(len(formula)):
        if formula[i].isdigit():
            prefix = formula[:i]
            number = int(formula[i:])
            return (prefix, number)
    return (formula, 1)

def split_formula(formula):
    result = []
    for part in split_before_each_uppercase(formula):
        if part:
            result.append(split_at_digit(part))
    return result

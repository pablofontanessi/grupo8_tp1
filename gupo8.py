from collections import defaultdict
import re

def sort_terms(input_operation, ops = ''):
    d = defaultdict(list)
    depth = 0
    pattern = r'[()]|[^( )' + ops + ']+'
    for item in re.findall(pattern, input_operation):
        if item == '(':
            depth += 1
        elif item == ')':
            depth -= 1
        else:
            d[depth].append(item)
    terms = []
    for depth in sorted(d.keys(),reverse = True):
        terms.extend(d[depth])
    return terms
    

def calculator(input_operation):
    count = 0
    result = ''
    for i in sort_terms(input_operation):
        count += 1
        if count < 4:
            result = str(result + ' ' + i)
    return int(eval(input_operation)), result[1:len(result)]
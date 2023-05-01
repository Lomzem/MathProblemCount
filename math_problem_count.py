import sys

def math_problem_count(text: str) -> int:
    groups = text.split(', ')
    for i, group in enumerate(groups):
        try:
            p_range, mult = group.split(' ')
            p_range = [int(x) for x in p_range.split('-')]
            p_range = list(x for x in range(p_range[0], p_range[1] + 1))
            mult_table = {'odds': [x for x in p_range if x % 2 != 0], 'evens': [x for x in p_range if x % 2 == 0], 'all': p_range}
            p_range = mult_table[mult]
            groups[i] = len(p_range)
        except ValueError:
            groups[i] = 1
    return sum(groups)

if __name__ == '__main__':
    try:
        result = math_problem_count(sys.argv[1])
    except IndexError:
        result = math_problem_count(input('Input string: '))
    input(f'{result}\n')
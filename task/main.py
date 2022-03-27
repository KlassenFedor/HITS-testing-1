from math import factorial as f


def formula(n):
    if type(n) != int:
        raise ValueError
    if -200 > n or n > 200:
        raise ValueError
    if n == 0:
        return '1'
    if n < 0:
        return '1/(' + do_all_steps(n) + ')'
    else:
        return do_all_steps(n)


def get_new_string_by_degree_a_b_and_ratio(a_degree, b_degree, ratio):
    if type(a_degree) != int or type(b_degree) != int or type(ratio) != int:
        raise ValueError
    if a_degree < 0 or b_degree < 0 or ratio < 0:
        raise ValueError
    if ratio == 0:
        return ''
    a_str = 'a^' + str(int(a_degree)) if a_degree > 1 else 'a'
    a_str = '' if a_degree == 0 else a_str
    b_str = 'b^' + str(int(b_degree)) if b_degree > 1 else 'b'
    b_str = '' if b_degree == 0 else b_str
    ratio_str = str(int(ratio)) if ratio > 1 else ''
    return ratio_str + a_str + b_str


def do_all_steps(input_number):
    if type(input_number) != int:
        raise ValueError
    if -200 > input_number or input_number > 200 or input_number == 0:
        raise ValueError
    input_number = abs(input_number)
    answer = ''
    for i in range(abs(input_number) + 1):
        ab_list = [input_number - i, i]
        ratio = int(f(input_number) // f(i) // f(input_number - i))
        string = get_new_string_by_degree_a_b_and_ratio(ab_list[0], ab_list[1], ratio)
        answer += '+' + str(string)
    return answer[1:]

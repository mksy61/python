def to_upper_case(s):
    return str(s).upper()


map_iterator = map(to_upper_case, 'abc')
print(type(map_iterator))
print(list(map_iterator))

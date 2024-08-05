
def calculate_structure_sum(*args):
    sum_args = 0
    for i in args:
        if isinstance(i, int) or isinstance(i,float):
            sum_args += i
        elif isinstance(i, str):
            sum_args += len(i)
        elif isinstance(i, list) or isinstance(i, tuple) or isinstance(i,set):
            for j in i:
                sum_args += calculate_structure_sum(j)
        elif isinstance(i, dict):
            for key, value in i.items():
                sum_args += calculate_structure_sum(key)
                sum_args += calculate_structure_sum(value)

    return sum_args



data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)

print(result)

def binary_sum(number_a, number_b):
  """
  The function takes two binary numbers as input (as strings) and returns their sum. The result (calculated sum) is also a binary number as a string.
  """
  print(format(int(number_a, base=2) + int(number_b, base=2), 'b'))

binary_sum('101', '111')
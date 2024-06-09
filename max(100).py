def maximum100():
  a = input()
  a = int(a)
  max = a
  for i in range(99):
    a = int(input())
    if a>max:
      max = a
  return max

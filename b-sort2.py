def b_sort(k=[],s=10):
  if k is not None:
    for i in range(s-1):
      for j in range(s-1-i):
        if k[j] > k[j+1]:
          temp = k[j]
          k[j] = k[j+1]
          k[j+1] = temp
    return 1
  else:
    return 0

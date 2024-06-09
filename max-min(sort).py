def max_min(tr):
  tr.sort()
  return tr[-1],tr[0]
  A=inputlist()
  M,m=max_min(A)
  print(M,m)

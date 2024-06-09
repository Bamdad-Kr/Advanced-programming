def mxamin_count(L):
  L.sort()
  count_min = L.count(L[0])
  count_max = L.count(L[-1])
  return L[-1],count_max,L[0],count_min

def b_sort(k,s):
  if k is not None:
    for i in range(s-1):
      for j in range(s-1-i):
        if k[j]>k[j+1]:
          temp = k[j]
          k[j]=k[j+1]
          k[j+1]=temp
    return k

def mean_new():
  k =[]
  i = 0
  counter =0
  while i!=1000:
    i=int(input())
    if i==1000:
      break
    k.append(i)
    counter+=1
  return k,counter

L,s=mean_new()
if b_sort(L,s):
  print(L)
else:
  print('is empty')

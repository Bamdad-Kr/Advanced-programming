class student ():
  def __init__(self,Reyazi,Faesi,Eghtesad,physies):
    self.r=Reyazi
    self.f=Faesi
    self.e=Eghtesad
    self.p=physies

  def Moadel(self):
    return(self.r + self.f + self.e + self.p)/4


  def Mashrot(self):
    if self.r<10 and self.f<10 and self.e<10 and self.p<10:
      print("the student is faild")
    else:
      print("the student is succefu11....")

  def subject(self):
    count=0
    s=[self.r,self.f,self.e,self.p]
    for item in s:
      count+=1
    print(f"The student passed {count}")

  def choose_Ryazi2(self):
    if self.r<10:
      print("the student you cant't choose math 2")
    else:
      print("the student you can choose math2 .....")

  def __del__(self):
    print("the student point is  deleted")

st=student(19,20,8,17)
print(st.Moadel())
print(st.Mashrot())
print(st.subject())
print(st.choose_Ryazi2())
del st

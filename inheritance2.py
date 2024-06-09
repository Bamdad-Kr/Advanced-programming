class Money:
  money=200000000

class Doctor(Money):
  docor="this doctor is famous...."

class Medical(Money):
  medical="this hospial is equipped"

class Hospital(Doctor,Medical):
  hospital="this hospital has a  doctor"

obj=Hospital()

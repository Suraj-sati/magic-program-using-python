import time
import os
from os import system
import random as r



def ss():
 os.system('cls')
 for i in range(0,9):
  
  print(r.randint(1,1),end="")
  print(r.randint(3,5),end="")
  print(r.randint(5,7),end="")
  print(r.randint(0,2))
 
 print() 
 x1=input("choose a number in your mind from above given number but dont tell me ...now press enter : ")
 print() 
 os.system('cls')
 x2=input("enter ur name : ")
 try:
  x3=int(input("enter ur age : "))
 except ValueError : 
  print("please enter valid age")
  time.sleep(2)
  ss()
 print()
 print("connecting ur brain......")
 print()
 time.sleep(3)


 system('cls')    

 for i in range(0,9):
  print(r.randint(1,1),end="")
  print(r.randint(3,5),end="")
  print(r.randint(0,2),end="")
  print(r.randint(5,7))
 
 print() 
 print("ur number is disappeared")
 
ss()
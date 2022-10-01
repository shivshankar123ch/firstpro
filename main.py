import datetime
import os

print(datetime.datetime.now())

print(" path where i'm working is :",os.getcwd())

for i in range(10):
  print("Hi:",i)
path = os.getcwd()
print(os.listdir(path))

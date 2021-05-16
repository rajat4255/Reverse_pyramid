# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

oddstar=1
# Pyramid Pattern programming
# Every pyramid have some number of rows and columns
print("please Enter number of Rows")
Row =int(input())
col = 2*Row-1

for i in range(0,Row):
      for j in range(0,col):
         print(end=" ")
      col=col-1
      for k in range(0,i+1):
            print("*",end=" ")
      print("\r")










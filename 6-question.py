#6.	Input marks, calculate percentage (arithmetic), and assign grade using logical conditions.
marks=int(input("marks"))
totalmarks=int(input("total marks"))
percentage=(marks/totalmarks)*100
if(percentage>90):
    print(percentage,"A")
elif(percentage>80):
    print(percentage,"B")
elif(percentage>70):
    print(percentage,"C")
else:
    print(percentage,"D")
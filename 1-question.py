#1.	Input age and nationality; check if the person is eligible to vote 
# (age >= 18 and nationality == 'Indian').
#2.	Use logical operators to check if a year is a leap year.
#3.	Use logical operators to verify if a password contains letters, digits, and has proper length.

# .5.	Even/Odd and Positive/Negative Checker
#6.	Input marks, calculate percentage (arithmetic), and assign grade using logical conditions.
# 7.	Apply discounts based on purchase amount using arithmetic and logical operators
# .8.	Compute roots using arithmetic; 

year=int(input("year"))
if(year%4==0 or year%100==0):
    print("it is a leep year")
else:
    print("not a leep year")
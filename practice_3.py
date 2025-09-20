#f string
word = input("enter your name")

print(f"good afternoon {word}")

#programme to add name and date in letter

name=input("enter name")
date=input("enter date")
print(f"dear<|{name}|>,\n You are selected!\n<|{date}|>")


#replace
string="dear<|name|>,\n You are selected!\n<|date|>"
print(string.replace("name","sadaf").replace("date","11-7-35"))

#detect double space in string

hello = "i am  sadaf"
print(hello.find("  "))
s=input("enter a string")

rev=""

for i in range(len(s)):

    rev=s[i]+rev

print(rev)
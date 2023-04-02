#Տարբերակ 1
text = str(input())
z_count=0
o_count=0
for x in text:
    if x == "z":
        z_count +=1
    elif x == "o":
        o_count +=1
if 2*z_count == o_count:
    print("Yes")
else:
    print("No")

#Տարբերակ 2
text = list(input())
z=text.count("z")
o=text.count("o")
if 2*z==o:
    print("Yes")
else:
    print("No")

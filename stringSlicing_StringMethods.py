a="Hello World"
print(a[8:])
print(a[-1])
print(a[::-1])

b=" Hello World  "
print(b)
print(b.strip())#strip() remove whitespaces from beginning and ending
print(b.replace("H","Y"))#replace("initial","towhichyouwant_toreplace") 

c="101"
print(c.isdigit()) #Python_String_Methods

d=a+b #String Concatination
print(d)
#Escape_Characters...
print("Alishan\nAbhiRam\nNikhil") #\n for new line.

#Print First,last,middle character of String...
strr="NAWAZ"
length=len(strr)
print(strr[0])
print(strr[int(length/2)])
print(strr[length-1])


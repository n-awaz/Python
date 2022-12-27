a,b,c,d=10,15,5,20
str="a={0},b={3},c={1},d={2}" #by default values are index:0,1,2,... but you can assign yourself too.
print(str.format(d,b,a,c))
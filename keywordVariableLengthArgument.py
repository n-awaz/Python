def details(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)

details("Adhiraj",place="Chandigarh",age="26",number=99999999)
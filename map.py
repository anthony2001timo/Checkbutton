#def doblar(numero):
#    return numero*2

#numeros=[2,5,10,23,50,33]

#i=map(doblar,numeros)
#print(list(i))

#Otra forma de hacer el codigo

#def doblar(numero):
#    return numero*2

#numeros=[2,5,10,23,50,33]

#i=map(lambda x:x*2,numeros)
#print(list(i))

#otro ejemplo:
a=[1,2,3,4,5]
b=[6,7,8,9,10]

i=map(lambda x,y: x*y,a,b)
print(list(i))


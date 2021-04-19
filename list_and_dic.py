def diezcuad():
    # list=[]
    # for i in range(100):
    #     if(i%3!=0):
    #         list.append(i**2)
    # print(list)
    #Usando list comprehension
    lista=[i**2 for i in range(1,100) if(i%3!=0)]
    print(lista)
def reto():
    lista=[i for i in range(1,100000) if i%4==0 and i%6==0 and i%9==0]
    print(lista)
def diction():
    # dic={}
    # for i in range(100):
    #     dic[i]=i**3
    # print(dic)
    #dict comprehension
    dic={i: i**3 for i in range(100) if i%3!=0}
    print(dic)
def reto2():
    dic={i: i**1/2 for i in range(1000)}
    print(dic)
if __name__ == "__main__":
    diezcuad()
    reto()
    diction()
    reto2()
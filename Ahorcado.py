import random
import numpy as np
import copy
import os
def run():
    band=1
    with open('./Palabras.txt','r', encoding='utf-8') as archivo:
        palabras=[palabra[:-1] for palabra in archivo]
    max=len(palabras)
    num_al=random.randint(0,max-1)
    escogida=palabras[num_al]
    referencia=copy.copy(escogida)
    escogida=list(escogida)
    correcta= "_" * len(escogida)
    ahor=list(map(lambda x:" ",np.zeros(len(escogida))))
    while band==1:
        letra=input("Digite una letra \n")
        for i,j in enumerate(escogida):
            if(letra==j and letra in referencia):
                correcta= correcta[:i] + letra + correcta[i+1:]
        if(referencia==correcta):
            band=0
        os.system("clear")
        print(correcta)
    print("Ganaste el juego")


if __name__=='__main__':
    run()
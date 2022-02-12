import random
import threading
import time


class Carrera ():
    def __init__(self, corredor_1=0, corredor_2=0, corredor_3=0, corredor_4=0):
        self.locked = threading.Lock()
        self.corredor_1 = corredor_1
        self.corredor_2 = corredor_2
        self.corredor_3 = corredor_3
        self.corredor_4 = corredor_4

    def correr_1(self):
        self.locked.acquire()
        try:
            self.corredor_1 += 1
            if(self.corredor_1 < 20):
                print("CORREDOR 1 distancia: ", self.corredor_1)
            else:

                print("CORREDOR 1 ha terminado")

        finally:
            self.locked.release()

    def correr_2(self):
        self.locked.acquire()
        try:
            self.corredor_2 += 1
            if(self.corredor_2 < 20):
                print("CORREDOR 2 distancia: ", self.corredor_2)

            else:
                print("CORREDOR 2 ha terminado")
        finally:
            self.locked.release()

    def correr_3(self):
        self.locked.acquire()
        try:
            self.corredor_3 += 1
            if(self.corredor_3 < 20):
                print("CORREDOR 3 distancia: ", self.corredor_3)
            else:

                print("CORREDOR 3 ha terminado")
        finally:
            self.locked.release()

    def correr_4(self):
        self.locked.acquire()
        try:
            self.corredor_4 += 1
            if(self.corredor_4 < 20):
                print("CORREDOR 4 distancia: ", self.corredor_4)
            else:
                print("CORREDOR 4 ha terminado")

        finally:
            self.locked.release()


def func_carrera_corredores(x):
    for y in range(5):
        time.sleep(random.random())
        x.correr_1()
        time.sleep(random.random())
        x.correr_2()
        time.sleep(random.random())
        x.correr_3()
        time.sleep(random.random())
        x.correr_4()


if __name__ == "__main__":
    carrera = Carrera()
    for y in range(4):
        print("Corredor: ", y+1)
        tsart = threading.Thread(
            target=func_carrera_corredores, args=(carrera,))
        tsart.start()

import random
import threading
import time


class Carrera ():
    def __init__(self, corredor_1=0, corredor_2=0, corredor_3=0, corredor_4=0):
        self.locked1 = threading.Lock()
        self.locked2 = threading.Lock()
        self.locked3 = threading.Lock()
        self.locked4 = threading.Lock()
        self.corredor_1 = corredor_1
        self.corredor_2 = corredor_2
        self.corredor_3 = corredor_3
        self.corredor_4 = corredor_4

    def correr_1(self):
        self.locked1.acquire()
        try:
            self.corredor_1 += 1
            if(self.corredor_1 < 20):
                time.sleep(random.random())
                print("CORREDOR 1 distancia: ", self.corredor_1)
            else:

                print("CORREDOR 1 ha terminado")

        finally:
            self.locked1.release()

    def correr_2(self):
        self.locked2.acquire()
        try:
            self.corredor_2 += 1
            if(self.corredor_2 < 20):
                time.sleep(random.random())
                print("CORREDOR 2 distancia: ", self.corredor_2)

            else:
                print("CORREDOR 2 ha terminado")
        finally:
            self.locked2.release()

    def correr_3(self):
        self.locked3.acquire()
        try:
            self.corredor_3 += 1
            if(self.corredor_3 < 20):
                time.sleep(random.random())
                print("CORREDOR 3 distancia: ", self.corredor_3)
            else:
                print("CORREDOR 3 ha terminado")
        finally:
            self.locked3.release()

    def correr_4(self):
        self.locked4.acquire()
        try:
            self.corredor_4 += 1
            if(self.corredor_4 < 20):
                time.sleep(random.random())
                print("CORREDOR 4 distancia: ", self.corredor_4)
            else:
                print("CORREDOR 4 ha terminado")
        finally:
            self.locked4.release()


def func_carrera_1(x):
    for y in range(20):
        x.correr_1()


def func_carrera_2(x):
    for y in range(20):
        x.correr_2()


def func_carrera_3(x):
    for y in range(20):
        x.correr_3()


def func_carrera_4(x):
    for y in range(20):
        x.correr_4()


if __name__ == "__main__":
    carrera = Carrera()
    print("Corredor: 1")
    print("Corredor: 2")
    print("Corredor: 3")
    print("Corredor: 4")
    
    tsart_1 = threading.Thread(
        target=func_carrera_1, args=(carrera,))
    tsart_2 = threading.Thread(
        target=func_carrera_2, args=(carrera,))
    tsart_3 = threading.Thread(
        target=func_carrera_3, args=(carrera,))
    tsart_4 = threading.Thread(
        target=func_carrera_4, args=(carrera,))
    tsart_1.start()
    tsart_2.start()
    tsart_3.start()
    tsart_4.start()

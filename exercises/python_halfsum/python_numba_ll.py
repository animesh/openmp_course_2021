#pip install numba
from numba import njit,prange

@njit(parallel=True)
def func1():
    j=0
    print('func1: starting')
    for i in range(1,3000000000000000000):
        j=j+i/2
    print('func1: finishing',j)

if __name__ == '__main__':
    func1()

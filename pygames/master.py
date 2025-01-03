import numpy as np
from numba import jit

@jit
def init():
    initW1 = np.random.uniform(-1, 1, (6, 6))
    initW2 = np.random.uniform(-1, 1, (6, 5))
    initW3 = np.random.uniform(-1, 1, (5, 4))
    initW4 = np.random.uniform(-1, 1, (4, 3))
    initB1 = np.random.uniform(-0.2, 0.2, 6)
    initB2 = np.random.uniform(-0.2, 0.2, 5)
    initB3 = np.random.uniform(-0.2, 0.2, 4)
    initB4 = np.random.uniform(-0.2, 0.2, 3)
    return (initW1, initW2, initW3, initW4, initB1, initB2, initB3, initB4)


def elimination(parameters, allFitness):
    for e in range(50):
        poppy = allFitness.index(min(allFitness))
        allFitness.pop(poppy)
        parameters.pop(poppy)
    return parameters


def mutate(survivors, learningRate):
    nsurv = survivors
    for survivornum in range(50):
        rands = init()
        l = []
        ns = []
        for j in rands:
            l.append(j*learningRate)
        for f in range(8):
            ns.append(survivors[survivornum][f]+l[f])
        nsurv.append(ns)
    return nsurv


if __name__ == "__main__":
    print(init())


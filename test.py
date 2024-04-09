import numpy as np
import gameplay

A = np.array([[0,0,0,2], [0,0,2,4], [4,2,4,2], [4,8,2,32]])

moved = gameplay.playsucessfulmove(A, 4, 4, 'd')
print(repr(moved))

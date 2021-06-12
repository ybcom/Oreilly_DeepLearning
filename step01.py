'''
Dezero 구현을 위한 변수 클래스 구현
'''
class Variable:
    def __init__(self, data):
        self.data = data

import numpy as np
data = np.array(2.0)
x = Variable(data)
print(x.data)

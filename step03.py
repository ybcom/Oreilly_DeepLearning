'''
Function class 이용
'''
import numpy as np

class Variable:
    def __init__(self, data):
        self.data = data

# Function 클래스는 기반 클래스로, 모든 함수에 공통되는 기능을 구현함
# 구체적인 함수는 Function 클래스를 상속한 클래스에서 구현함
class Function:
    # __call__ 매서드는 f = Function() 형태로 인스턴스를 변수 f에 대입하고 f(...)로 사용 가능함
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        return output

    def forward(self, x):
        # Function 클래스의 forward 메서드는 예외를 발생시킴
        # 이 메서드는 상속하여 구현해야 한다는 의미
        raise NotImplementedError()

class Square(Function):
    def forward(self, x):
        return x**2

'''
자연로그의 밑을 구함
'''
class Exp(Function):
    def forward(self,x):
        return np.exp(x)

# y = (e^x^2)^2 계산
A = Square()
B = Exp()
C = Square()

x = Variable(np.array(0.5))
a = A(x)
b = B(a)
y = C(b)
print(y.data)

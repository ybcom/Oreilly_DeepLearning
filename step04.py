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

class Exp(Function):
    def forward(self,x):
        return np.exp(x)

# 중앙차분 구하기
# f(x+h) - f(x-h) / 2h
def numerical_diff(f, x, eps=1e-4):
    x0 = Variable(x.data - eps)
    x1 = Variable(x.data + eps)
    y0 = f(x0)
    y1 = f(x1)
    return (y1.data - y0.data) / (2 * eps)

# Square 클래스를 대상으로 미분 수행
f = Square()
x = Variable(np.array(2.0))
dy = numerical_diff(f,x)
print(dy)

'''
합성 함수의 미분
y = (e^x^2)^2
'''
def f(x):
    A = Square()
    B = Exp()
    C = Square()
    return C(B(A(x)))

x = Variable(np.array(0.5))
dy = numerical_diff(f,x)
print(dy)


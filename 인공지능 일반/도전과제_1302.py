import numpy as np
import matplotlib.pyplot as plt

x = np.array([174, 152, 138, 128, 186])
y = np.array([71, 55, 46, 38, 88])

lrate = [0.00001, 0.000001, 0.0000001]
epochs = 1000

n = float(len(x))

for rate in lrate:
    w = 0
    b = 0
    for i in range(epochs):
        y_pred = w * x + b
        dw = (2 / n) * sum(x * (y_pred - y))
        db = (2 / n) * sum(y_pred - y)
        w = w - rate * dw 
        b = b - rate * db 
    print(f"학습률 {rate} 일 때 -> w: {w:.4f}, b: {b:.4f}")

print(w, b)
#nan, nan이 출력 결과로 뜨게 되는데 입력값의 크기가 커서, 기울기의 계산값이 튀어올라서 범위를 초과하게 되어서 nan이 출력된다
#학습률을 크게 줄여서 계산값이 튀어오르지는 않지만 학습률이 너무 작아지고 반복 횟수가 너무 작아서 정답에 도달하기 전에 끝나버렸다
#입력 데이터 x의 값이 크기 때문에 발생한다. 그렇기에 데이터의 크기를 줄여주면 적당한 학습률에서도 정답에 도달할수있을것이다.
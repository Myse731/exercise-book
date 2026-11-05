import matplotlib.pyplot as plt
from sklearn import linear_model

reg = linear_model.LinearRegression()

x = [[174], [152], [138], [128], [186]]
y = [71, 55, 46, 38, 88]

reg.fit(x, y)

print(reg.predict([[165]]))
print(reg.coef_)         
print(reg.intercept_)    
print(reg.score(x, y))

heights = [[150], [160], [172], [180]]
predicted_weights = reg.predict(heights)
print(predicted_weights)

plt.scatter(x, y, color='black')
y_pred = reg.predict(x)
plt.plot(x, y_pred, color = 'blue', linewidth = 3)
plt.show()

# 직선의 식 : y = 0.82x -68 (기울기는 2자리 까지 반올림, 절편은 소수점을 날렸음)
#키가 1CM 증가할때마다 몸무게가 약 0.82kg 증가한다
#score값은 0.981...로 1에 매우 가깝다. 이것은 매우 높은 확률로 정확하게 예측하고 반영하고 있음을 알 수 있다.
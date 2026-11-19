import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

X_train = np.array([
    [158, 62],
    [162, 66],
    [165, 64],
    [160, 70],
    [155, 60],
    [168, 68],
    [163, 72],
    [157, 65],
    [170, 71],
    [161, 63],
    [172, 78],
    [178, 82],
    [175, 80],
    [169, 74],
    [181, 86],
    [174, 77],
    [183, 90],
    [176, 84],
    [167, 79],
    [179, 88]
])
Y_train = np.array([0]*10 + [1]*10)

X_test = np.array([
    [164, 67],
    [159, 61],
    [167, 69],
    [162, 74],
    [156, 63],
    [171, 75],
    [173, 79],
    [177, 83],
    [168, 73],
    [182, 87]
])

Y_test = np.array([0] * 5 + [1] * 5)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, Y_train) 
y_pred = knn.predict(X_test)
wrong = np.where(y_pred != Y_test)[0]

print(X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)
plt.scatter(X_train[Y_train == 0, 0], X_train[Y_train == 0, 1], label = '여자')
plt.scatter(X_train[Y_train == 1, 0], X_train[Y_train == 1, 1], label = '남자')
plt.xlabel('키(cm)')
plt.ylabel('허리둘레(cm)')
plt.legend()
#plt.show()

print(knn.score(X_train, Y_train))
print(y_pred, Y_test)
print(knn.score(X_test, Y_test))
print(wrong, wrong+1, X_test[wrong])
print(metrics.confusion_matrix(Y_test, y_pred))
print(metrics.classification_report(Y_test, y_pred, target_names=['여자', '남자']))

for i in range(1, 10):
    kz = KNeighborsClassifier(n_neighbors=i)
    kz.fit(X_train, Y_train)
    print(kz.score(X_test, Y_test))
#가장 좋은 K는 7이다. 그 이유로 1은 정확도가 1이지만 과적합의 위험이 크기에 적당한 크기의 출력이 7을 고르는것이 안전하기 때문이다.

while True:
    height = input('키(종료하려면 "종료" 입력): ')
    if height == "종료":
        break
    h = int(height)
    waist = int(input('허리둘레: '))
    pred = knn.predict([[h, waist]])[0]
    proba = knn.predict_proba([[h, waist]])[0]
    if pred == 0:
        print(f"여자 (여자일 확률: {proba[pred]:.2f})")
    else:
        print(f"남자 (남자일 확률: {proba[pred]:.2f})")

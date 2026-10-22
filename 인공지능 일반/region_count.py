import pandas as pd
import matplotlib.pyplot as plt

# 한글이 깨지지 않도록 폰트 설정 (Mac 환경)
plt.rcParams['font.family'] = 'AppleGothic'  
plt.rcParams['axes.unicode_minus'] = False       

# 전처리에서 새로 저장한 'hollys_지역별_매장수.csv' 파일 불러오기
df = pd.read_csv('/Users/kwonminse/Desktop/exbk/인공지능 일반/hollys_지역별_매장수.csv', encoding='cp949')

# 선 그래프 그리기
plt.plot(df['region'], df['매장수'], color='orange', marker='o', label='매장 수')

plt.title('지역별 할리스 매장 수')
plt.xlabel('지역')
plt.ylabel('매장 수(개)')
plt.legend()

plt.show()
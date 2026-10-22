import pandas as pd

df = pd.read_csv('/Users/kwonminse/Desktop/exbk/인공지능 일반/sleep.csv', encoding='cp949')

df_selected = df[['사고연도', '사고시간', '노선명', '사망', '부상']]

df_selected.to_csv('졸음운전_사고통계_전처리.csv', index=False, encoding='utf-8-sig')
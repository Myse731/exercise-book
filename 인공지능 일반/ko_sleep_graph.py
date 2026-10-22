import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rc('font', family='AppleGothic')
plt.rc('axes', unicode_minus=False)

df = pd.read_csv('/Users/kwonminse/Desktop/exbk/인공지능 일반/졸음운전_사고통계_전처리.csv')

df['사고시'] = pd.to_datetime(df['사고시간'], format='%H:%M').dt.hour

year_df = df.groupby('사고연도')[['사망', '부상']].sum().reset_index()
hour_df = df.groupby('사고시')[['사망', '부상']].sum().reset_index()
route_df = df.groupby('노선명')[['사망', '부상']].sum().sort_values(by='부상', ascending=False).head(10).reset_index()

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

year_df.plot(x='사고연도', y=['사망', '부상'], kind='bar', ax=axes[0], color=['#e74c3c', '#3498db'])
axes[0].set_title('연도별 사망자 및 부상자 수')
axes[0].set_xlabel('사고연도')
axes[0].set_ylabel('인원 수 (명)')
axes[0].tick_params(axis='x', rotation=0)

axes[1].plot(hour_df['사고시'], hour_df['부상'], marker='o', label='부상', color='#3498db', linewidth=2)
axes[1].plot(hour_df['사고시'], hour_df['사망'], marker='s', label='사망', color='#e74c3c', linewidth=2)
axes[1].set_title('시간대별(0~23시) 사망자 및 부상자 수')
axes[1].set_xlabel('사고 시간(시)')
axes[1].set_ylabel('인원 수 (명)')
axes[1].set_xticks(range(0, 24, 2))
axes[1].legend()
axes[1].grid(True, linestyle='--', alpha=0.5)

route_df.plot(x='노선명', y=['사망', '부상'], kind='barh', ax=axes[2], color=['#e74c3c', '#3498db'])
axes[2].set_title('상위 10개 노선별 사망자 및 부상자 수')
axes[2].set_xlabel('인원 수 (명)')
axes[2].set_ylabel('노선명')
axes[2].invert_yaxis() 

plt.tight_layout()
plt.show()
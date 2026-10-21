import pandas as pd
import re

df = pd.read_csv('/Users/kwonminse/Desktop/exbk/인공지능 일반/hollys1.csv', encoding='cp949')

def check_second_floor(address):
    if pd.isna(address):
        return False, '주소 정보 없음'
    
    addr = str(address).strip()
    
    if re.search(r'2층|2F|2f', addr):
        return True, '2층 직접 명시'
        
    range_match = re.search(r'(\d+)\s*(?:층)?\s*[~-]\s*(\d+)\s*층?', addr)
    if range_match:
        start_floor = int(range_match.group(1))
        end_floor = int(range_match.group(2))
        if start_floor <= 2 <= end_floor:
            return True, f'층수 범위 포함 ({start_floor}~{end_floor}층)'

    comma_match = re.search(r'(\d+)\s*,\s*(\d+)\s*층', addr)
    if comma_match:
        f1 = int(comma_match.group(1))
        f2 = int(comma_match.group(2))
        if f1 == 2 or f2 == 2:
            return True, f'층수 쉼표 구분 포함 ({f1},{f2}층)'

    # 4) 2xx호 패턴 (200~299호)
    # 호수 패턴 예: 201호, 204호 등
    ho_matches = re.findall(r'(\d+)호', addr)
    for ho in ho_matches:
        num = int(ho)
        if 200 <= num <= 299:
            return True, f'200번대 호수 포함 ({num}호)'

    return False, '2층 해당 없음'


results = df['address'].apply(check_second_floor)
df['is_2F'] = [r[0] for r in results]
df['reason_2F'] = [r[1] for r in results]  


df_2f = df[df['is_2F'] == True].copy()


print(f"전체 매장 수: {len(df)}개")
print(f"2층 영업 매장 수: {len(df_2f)}개")
print("\n--- 판단 근거별 매장 수 ---")
print(df_2f['reason_2F'].value_counts())

df_2f.to_csv('/Users/kwonminse/Desktop/exbk/인공지능 일반/hollys_2층매장.csv', encoding='cp949', index=False)
print("\n'hollys_2층매장.csv' 파일 저장 완료!")
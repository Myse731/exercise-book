# ==========================================
# 「내가 조선시대에 태어났다면?」
# 조선시대 상극 / 연분 인물 진단기
# ==========================================

# 조선시대 인물 지식 베이스 (총 30명)
people = [
    # 기존 인물 10명
    {
        "name": "세종대왕",
        "type": "ENFJ",
        "job": "국왕/왕족",
        "status": "문반/무반",
        "description": "인재를 발굴하고 백성을 위한 정책을 추진한 포용형 리더"
    },
    {
        "name": "이순신",
        "type": "ISTJ",
        "job": "암행어사",
        "status": "문반/무반",
        "description": "위기에도 침착하게 전략을 세우고 책임을 다한 전략가"
    },
    {
        "name": "정약용",
        "type": "INTJ",
        "job": "외지부",
        "status": "유학자/선비",
        "description": "현실의 문제를 분석하고 새로운 해결책을 찾은 실용적 개혁가"
    },
    {
        "name": "장영실",
        "type": "INTP",
        "job": "산원/기술관",
        "status": "기술관",
        "description": "관찰과 실험을 통해 새로운 과학 기술을 만든 탐구형 발명가"
    },
    {
        "name": "이황",
        "type": "INFJ",
        "job": "외지부",
        "status": "유학자/선비",
        "description": "도덕적 원칙과 자기 성찰을 중요하게 생각한 사색가"
    },
    {
        "name": "황희",
        "type": "ENFJ",
        "job": "외지부",
        "status": "문반/무반",
        "description": "다양한 의견을 듣고 갈등을 조율한 소통형 중재자"
    },
    {
        "name": "허균",
        "type": "ENTP",
        "job": "전기수",
        "status": "문반/무반",
        "description": "기존 질서에 의문을 제기하고 새로운 관점을 제시한 도전자"
    },
    {
        "name": "김홍도",
        "type": "ESFP",
        "job": "화원",
        "status": "광대/백정",
        "description": "사람들의 일상을 관찰하고 유쾌하게 표현한 예술가"
    },
    {
        "name": "김만덕",
        "type": "ESTJ",
        "job": "역관",
        "status": "상인/보부상",
        "description": "뛰어난 실행력으로 사업을 성공시키고 나눔을 실천한 사업가"
    },
    {
        "name": "허난설헌",
        "type": "INFP",
        "job": "화원",
        "status": "광대/백정",
        "description": "섬세한 감정과 풍부한 상상력을 작품으로 표현한 창작가"
    },
    
    # 추가 인물 20명
    {
        "name": "장희빈",
        "type": "ESTP",
        "job": "국왕/왕족",
        "status": "상인/보부상",
        "description": "변화를 빠르게 포착하고 과감하게 기회를 잡는 현실적 수완가"
    },
    {
        "name": "인현왕후",
        "type": "ISFJ",
        "job": "국왕/왕족",
        "status": "문반/무반",
        "description": "온화함과 곧은 덕성으로 자신의 신념과 자리를 지킨 내조자"
    },
    {
        "name": "정도전",
        "type": "ENTJ",
        "job": "외지부",
        "status": "문반/무반",
        "description": "새로운 나라의 기틀과 제도를 설계한 대담한 전략가"
    },
    {
        "name": "박문수",
        "type": "ESTJ",
        "job": "암행어사",
        "status": "문반/무반",
        "description": "현장을 직접 발로 뛰며 정의를 구현한 암행어사"
    },
    {
        "name": "허준",
        "type": "ISFJ",
        "job": "의원",
        "status": "기술관",
        "description": "환자를 보살피고 묵묵히 의학을 집대성한 전문가"
    },
    {
        "name": "변승업",
        "type": "ESTP",
        "job": "역관",
        "status": "상인/보부상",
        "description": "뛰어난 정보력과 수완으로 거부를 쌓은 대표 역관"
    },
    {
        "name": "신윤복",
        "type": "ENFP",
        "job": "화원",
        "status": "광대/백정",
        "description": "조선의 풍속을 자유롭고 섬세한 감각으로 그려낸 천재 화가"
    },
    {
        "name": "이업복",
        "type": "ESFP",
        "job": "전기수",
        "status": "광대/백정",
        "description": "몰입감 넘치는 연기로 좌중을 사로잡은 최고의 이야기꾼"
    },
    {
        "name": "임경업",
        "type": "ISTP",
        "job": "착호갑사",
        "status": "문반/무반",
        "description": "뛰어난 무예와 용맹함으로 이름을 날린 무신"
    },
    {
        "name": "임상옥",
        "type": "ENTJ",
        "job": "역관",
        "status": "상인/보부상",
        "description": "상도를 지키며 큰 부를 일궈낸 조선 최고의 거상"
    },
    {
        "name": "조광조",
        "type": "ENTJ",
        "job": "외지부",
        "status": "유학자/선비",
        "description": "타협 없는 원칙과 철학으로 개혁을 추진한 사림파의 리더"
    },
    {
        "name": "율곡 이이",
        "type": "INFJ",
        "job": "외지부",
        "status": "유학자/선비",
        "description": "시대를 내다보고 철학적 혜안을 제시한 대표 학자"
    },
    {
        "name": "서경덕",
        "type": "INTP",
        "job": "외지부",
        "status": "유학자/선비",
        "description": "벼슬을 사양하고 독자적인 학문을 탐구한 사색가"
    },
    {
        "name": "홍대용",
        "type": "ENTP",
        "job": "산원/기술관",
        "status": "기술관",
        "description": "새로운 사상을 받아들이며 기존 관념을 깨뜨린 실학자"
    },
    {
        "name": "황진이",
        "type": "ENFP",
        "job": "전기수",
        "status": "광대/백정",
        "description": "틀에 갇히지 않고 자유로운 시와 예술을 즐긴 예인"
    },
    {
        "name": "김석주",
        "type": "ISTJ",
        "job": "외지부",
        "status": "향리/아전",
        "description": "냉철한 판단력으로 송사를 대리한 법률가"
    },
    {
        "name": "김정호",
        "type": "ISTJ",
        "job": "산원/기술관",
        "status": "기술관",
        "description": "집념과 꼼꼼함으로 대동여지도를 완성한 지리학자"
    },
    {
        "name": "신사임당",
        "type": "INFJ",
        "job": "화원",
        "status": "유학자/선비",
        "description": "고결한 인품과 뛰어난 예술적 재능을 갖춘 예술가"
    },
    {
        "name": "이항복",
        "type": "ENTP",
        "job": "전기수",
        "status": "문반/무반",
        "description": "재치와 유쾌한 재담으로 위기를 극복한 융통성파"
    },
    {
        "name": "전봉준",
        "type": "ENFJ",
        "job": "암행어사",
        "status": "자유 농민",
        "description": "불의에 맞서 백성을 이끌고 변화를 촉구한 리더"
    }
]


# ------------------------------------------
# 사용자 성향을 결정하는 함수
# ------------------------------------------

def get_mbti():
    mbti = ""

    # E / I
    print("\n[1] 사람들과 함께 활동하는 것이 좋나요?")
    print("1. 사람들과 함께하는 것이 좋다.")
    print("2. 혼자 있는 것이 좋다.")
    answer = input("선택: ")
    mbti += "E" if answer == "1" else "I"

    # S / N
    print("\n[2] 문제를 해결할 때 무엇을 중요하게 생각하나요?")
    print("1. 실제 경험과 구체적인 정보를 중요하게 생각한다.")
    print("2. 새로운 아이디어와 가능성을 중요하게 생각한다.")
    answer = input("선택: ")
    mbti += "S" if answer == "1" else "N"

    # T / F
    print("\n[3] 중요한 결정을 내릴 때 무엇을 중요하게 생각하나요?")
    print("1. 논리와 원칙을 중요하게 생각한다.")
    print("2. 사람의 감정과 관계를 중요하게 생각한다.")
    answer = input("선택: ")
    mbti += "T" if answer == "1" else "F"

    # J / P
    print("\n[4] 평소 생활 방식은 어떤가요?")
    print("1. 계획을 세우고 계획대로 행동하는 편이다.")
    print("2. 상황에 따라 유연하게 행동하는 편이다.")
    answer = input("선택: ")
    mbti += "J" if answer == "1" else "P"

    return mbti


# ------------------------------------------
# 직업 선택 (당대 명칭 기준 정리)
# ------------------------------------------

def get_job():
    # 데이터 매칭용 실제 직업 명칭
    jobs = [
        "국왕/왕족", "의원", "역관", "외지부", "화원", 
        "산원/기술관", "암행어사", "전기수", "착호갑사", "매분구", "수모"
    ]

    # 화면 출력용 간결 명칭
    job_descriptions = [
        "국왕/왕족 (통치자 및 왕실 인물)",
        "의원 (의사/한의사)",
        "역관 (통역사/외교관)",
        "외지부 (변호사)",
        "화원 (화가/디자이너)",
        "산원/기술관 (과학자/수학자/지리학자)",
        "암행어사 (시크릿 감찰관)",
        "전기수 (이야기꾼/아나운서)",
        "착호갑사 (특수부대/경찰)",
        "매분구 (뷰티 컨설턴트)",
        "수모 (웨딩플래너)"
    ]

    print("\n[5] 조선시대에 어떤 직업을 가지고 싶나요?")
    for i in range(len(job_descriptions)):
        print(f"{i + 1}. {job_descriptions[i]}")

    while True:
        try:
            answer = int(input("선택: "))
            if 1 <= answer <= len(jobs):
                return jobs[answer - 1]
            print("올바른 번호를 선택해주세요.")
        except ValueError:
            print("숫자로 입력해주세요.")


# ------------------------------------------
# 신분 선택
# ------------------------------------------

def get_status():
    statuses = [
        "문반/무반", "유학자/선비", "향리/아전", "기술관",
        "상인/보부상", "자유 농민", "외거노비", "광대/백정"
    ]

    print("\n[6] 어떤 신분으로 살아가고 싶나요?")
    for i in range(len(statuses)):
        print(f"{i + 1}. {statuses[i]}")

    while True:
        try:
            answer = int(input("선택: "))
            if 1 <= answer <= len(statuses):
                return statuses[answer - 1]
            print("올바른 번호를 선택해주세요.")
        except ValueError:
            print("숫자로 입력해주세요.")


# ------------------------------------------
# 매칭 점수 계산
# ------------------------------------------

def calculate_score(user_type, user_job, user_status, person):
    score = 0

    # MBTI의 각 요소가 일치하면 +1 (최대 4점)
    for i in range(4):
        if user_type[i] == person["type"][i]:
            score += 1

    # 직업이 비슷하면 +2
    if user_job == person["job"]:
        score += 2

    # 신분이 같으면 +2
    if user_status == person["status"]:
        score += 2

    return score


# ------------------------------------------
# 진단
# ------------------------------------------

def diagnose(user_type, user_job, user_status):
    scores = []

    for person in people:
        score = calculate_score(
            user_type,
            user_job,
            user_status,
            person
        )

        scores.append({
            "name": person["name"],
            "score": score,
            "description": person["description"]
        })

    # 점수가 높은 순서대로 정렬
    scores.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return scores


# ------------------------------------------
# 프로그램 시작
# ------------------------------------------

print("=" * 45)
print("     「내가 조선시대에 태어났다면?」")
print("       조선시대 상극 / 연분 진단기")
print("=" * 45)

print("\n질문에 답하면 당신과 잘 맞는")
print("조선시대 인물을 찾아드립니다!")

# 사용자 정보 입력
user_type = get_mbti()
user_job = get_job()
user_status = get_status()

# 진단
results = diagnose(
    user_type,
    user_job,
    user_status
)


# ------------------------------------------
# 결과 출력
# ------------------------------------------

best = results[0]
worst = results[-1]

print("\n")
print("=" * 45)
print("               진단 결과")
print("=" * 45)

print(f"\n당신의 성향 : {user_type}")
print(f"희망 직업   : {user_job}")
print(f"희망 신분   : {user_status}")

print("\n💕 당신의 연분")
print("-" * 30)
print(f"인물 이름 : {best['name']}")
print(f"특징 설명 : {best['description']}")
print(f"매칭 점수 : {best['score']} / 8")

print("\n💥 당신의 상극")
print("-" * 30)
print(f"인물 이름 : {worst['name']}")
print(f"특징 설명 : {worst['description']}")
print(f"매칭 점수 : {worst['score']} / 8")

print("\n" + "=" * 45)
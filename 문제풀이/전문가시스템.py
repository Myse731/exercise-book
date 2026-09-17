# ==========================================
# 「내가 조선시대에 태어났다면?」
# 조선시대 상극 / 연분 인물 진단기
# ==========================================


# 조선시대 인물 지식 베이스
people = [
    {
        "name": "세종대왕",
        "type": "ENFJ",
        "job": "왕",
        "status": "문반/무반",
        "description": "인재를 발굴하고 백성을 위한 정책을 추진한 포용형 리더"
    },
    {
        "name": "이순신",
        "type": "ISTJ",
        "job": "무신",
        "status": "문반/무반",
        "description": "위기에도 침착하게 전략을 세우고 책임을 다한 전략가"
    },
    {
        "name": "정약용",
        "type": "INTJ",
        "job": "문신",
        "status": "유학자/선비",
        "description": "현실의 문제를 분석하고 새로운 해결책을 찾은 실용적 개혁가"
    },
    {
        "name": "장영실",
        "type": "INTP",
        "job": "과학 기술자",
        "status": "기술관",
        "description": "관찰과 실험을 통해 새로운 과학 기술을 만든 탐구형 발명가"
    },
    {
        "name": "이황",
        "type": "INFJ",
        "job": "성리학자",
        "status": "유학자/선비",
        "description": "도덕적 원칙과 자기 성찰을 중요하게 생각한 사색가"
    },
    {
        "name": "황희",
        "type": "ENFJ",
        "job": "문신",
        "status": "문반/무반",
        "description": "다양한 의견을 듣고 갈등을 조율한 소통형 중재자"
    },
    {
        "name": "허균",
        "type": "ENTP",
        "job": "문신",
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
        "job": "상인",
        "status": "상인/보부상",
        "description": "뛰어난 실행력으로 사업을 성공시키고 나눔을 실천한 사업가"
    },
    {
        "name": "허난설헌",
        "type": "INFP",
        "job": "시인",
        "status": "광대/백정",
        "description": "섬세한 감정과 풍부한 상상력을 작품으로 표현한 창작가"
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

    if answer == "1":
        mbti += "E"
    else:
        mbti += "I"


    # S / N
    print("\n[2] 문제를 해결할 때 무엇을 중요하게 생각하나요?")
    print("1. 실제 경험과 구체적인 정보를 중요하게 생각한다.")
    print("2. 새로운 아이디어와 가능성을 중요하게 생각한다.")

    answer = input("선택: ")

    if answer == "1":
        mbti += "S"
    else:
        mbti += "N"


    # T / F
    print("\n[3] 중요한 결정을 내릴 때 무엇을 중요하게 생각하나요?")
    print("1. 논리와 원칙을 중요하게 생각한다.")
    print("2. 사람의 감정과 관계를 중요하게 생각한다.")

    answer = input("선택: ")

    if answer == "1":
        mbti += "T"
    else:
        mbti += "F"


    # J / P
    print("\n[4] 평소 생활 방식은 어떤가요?")
    print("1. 계획을 세우고 계획대로 행동하는 편이다.")
    print("2. 상황에 따라 유연하게 행동하는 편이다.")

    answer = input("선택: ")

    if answer == "1":
        mbti += "J"
    else:
        mbti += "P"

    return mbti


# ------------------------------------------
# 직업 선택
# ------------------------------------------

def get_job():
    jobs = [
        "의원",
        "역관",
        "외지부",
        "화원",
        "암행어사",
        "전기수",
        "착호갑사",
        "매분구",
        "수모"
    ]

    print("\n[5] 조선시대에 어떤 직업을 가지고 싶나요?")

    for i in range(len(jobs)):
        print(f"{i + 1}. {jobs[i]}")

    answer = int(input("선택: "))

    return jobs[answer - 1]


# ------------------------------------------
# 신분 선택
# ------------------------------------------

def get_status():
    statuses = [
        "문반/무반",
        "유학자/선비",
        "향리/아전",
        "기술관",
        "상인/보부상",
        "자유 농민",
        "외거노비",
        "광대/백정"
    ]

    print("\n[6] 어떤 신분으로 살아가고 싶나요?")

    for i in range(len(statuses)):
        print(f"{i + 1}. {statuses[i]}")

    answer = int(input("선택: "))

    return statuses[answer - 1]


# ------------------------------------------
# 매칭 점수 계산
# ------------------------------------------

def calculate_score(user_type, user_job, user_status, person):

    score = 0

    # MBTI의 각 요소가 일치하면 +1
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
print("              진단 결과")
print("=" * 45)

print(f"\n당신의 성향 : {user_type}")
print(f"희망 직업   : {user_job}")
print(f"희망 신분   : {user_status}")

print("\n💕 당신의 연분")
print("-" * 30)
print(best["name"])
print(best["description"])
print(f"매칭 점수 : {best['score']} / 8")

print("\n💥 당신의 상극")
print("-" * 30)
print(worst["name"])
print(worst["description"])
print(f"매칭 점수 : {worst['score']} / 8")

print("\n" + "=" * 45)
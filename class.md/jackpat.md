## 주제 : 확률 게임 사이트

- 화면구현(HTML/CSS)
    - 메인 화면
        
        ```css
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
        }
        
        html, body{
            width:100%;
            overflow-x:hidden;
            background:#000;
            font-family:'Segoe UI', sans-serif;
        }
        
        /* 헤더 */
        
        header{
            display:flex;
            justify-content:space-between;
            align-items:center;
            padding:18px 40px;
            background:#000;
            border-bottom:2px solid gold;
            position:sticky;
            top:0;
            z-index:100;
        }
        
        .logo{
            color:gold;
            font-size:48px;
            font-weight:900;
        
            text-shadow:
            0 0 3px rgba(255,215,0,.8),
            0 0 8px rgba(255,215,0,.5);
        }
        
        .menu{
            display:flex;
            gap:15px;
        }
        
        .c-btn,
        .s-btn{
            padding:12px 22px;
            background:gold;
            color:black;
            border:none;
            border-radius:10px;
            font-size:15px;
            font-weight:bold;
            cursor:pointer;
            transition:.3s;
        }
        
        .c-btn:hover,
        .s-btn:hover{
            transform:scale(1.05);
            box-shadow:0 0 20px gold;
        }
        
        /* 메인 배너 */
        
        .mainchang{
            width:100%;
            height:440px; /* 기존 520px -> 380px */
            overflow:hidden;
            background:black;
            border-bottom:2px solid gold;
        }
        
        .mainchang img{
            width:100%;
            height:100%;
            object-position:center;
            display:block;
        }
        
        /* 메인 컨텐츠 */
        
        .content-wrap{
            width:95%;
            margin:25px auto;
            display:grid;
            grid-template-columns:3fr 1fr;
            gap:30px;
        }
        
        /* 게임 영역 */
        
        .game-area{
            display:grid;
            grid-template-columns:1fr 1fr;
            gap:25px;
        }
        
        .game-card{
            background:#111;
            border:2px solid gold;
            border-radius:18px;
            overflow:hidden;
            transition:.3s;
        }
        
        .game-card:hover{
            transform:translateY(-8px);
        
            box-shadow:
            0 0 15px gold,
            0 0 30px gold;
        }
        
        .game-card img{
            width:100%;
            height:280px;
            object-fit:cover;
        }
        
        .game-info{
            padding:25px;
            text-align:center;
            color:white;
        }
        
        .game-info h2{
            color:gold;
            font-size:32px;
            margin-bottom:15px;
        }
        
        .game-info p{
            color:#ddd;
            margin-bottom:20px;
        }
        
        .game-info button{
            padding:12px 35px;
            background:gold;
            color:black;
            border:none;
            border-radius:10px;
            font-size:17px;
            font-weight:bold;
            cursor:pointer;
            transition:.3s;
        }
        
        .game-info button:hover{
            transform:scale(1.08);
            box-shadow:0 0 15px gold;
        }
        
        /* 유저 정보 */
        
        .userinfo{
            background:#111;
            border:2px solid gold;
            border-radius:18px;
            padding:25px;
            color:white;
            height:fit-content;
        
            box-shadow:
            0 0 10px rgba(255,215,0,.3);
        }
        
        .userinfo h2{
            text-align:center;
            color:gold;
            margin-bottom:25px;
        }
        
        .info-box{
            margin-bottom:25px;
            padding-bottom:15px;
            border-bottom:1px solid #444;
        }
        
        .info-box p{
            color:#999;
            margin-bottom:10px;
        }
        
        .info-box span{
            font-size:20px;
            font-weight:bold;
        }
        
        .mypage{
            width:100%;
            padding:14px;
            background:gold;
            color:black;
            border:none;
            border-radius:10px;
            font-weight:bold;
            font-size:16px;
            cursor:pointer;
            transition:.3s;
        }
        
        .mypage:hover{
            transform:scale(1.03);
            box-shadow:0 0 15px gold;
        }
        
        /* 푸터 */
        
        .barr{
            margin-top:50px;
            padding:18px;
            background:#000;
            color:gold;
            text-align:center;
            border-top:2px solid gold;
        }
        
        /* 반응형 */
        
        @media(max-width:1200px){
        
            .content-wrap{
                grid-template-columns:1fr;
            }
        
            .game-area{
                grid-template-columns:1fr;
            }
        
            .userinfo{
                width:100%;
            }
        
            .mainchang{
                height:250px;
            }
        }
        ```
        
        ```html
        <!DOCTYPE html>
        <html lang="ko">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>낙동랜드</title>
            <link rel="stylesheet" href="../css/mmain.css">
        </head>
        <body>
        
        <header>
            <div class="logo">🎰 낙동랜드</div>
        
            <div class="menu">
                <!-- 이거 충전소 charge.html을 연결했는데 저기 아니면 바꿔야하는 -->
                <button class="c-btn"><a href="http://127.0.0.1:5501/html/charge.html">충전소</a></button>
                <button class="s-btn"><a href="http://127.0.0.1:5500/html/login.html">로그인 / 회원가입</a></button>
            </div>
        </header>
        
        <div class="mainchang">
            <img src="../zz.png" alt="이벤트 배너">
        </div>
        
        <div class="content-wrap">
        
            <div class="game-area">
        
                <div class="game-card">
                    <img src="../zzz (1).png" alt="슬롯">
                    <div class="game-info">
                        <h2>🎰 슬롯 게임</h2>
                        <p>다양한 슬롯 게임을 즐기고 코인을 획득하세요!</p>
                        <button><a href="http://127.0.0.1:5500/html/doback.html">입장하기</a></button>
                        <!-- 글자색 바뀜 주의 -->
                    </div>
                </div>
        
                <div class="game-card">
                    <img src="../zzz (2).png" alt="룰렛">
                    <div class="game-info">
                        <h2>🎡 룰렛 게임</h2>
                        <p>행운의 룰렛을 돌려 추가 코인을 획득하세요!</p>
                        <button><a href="http://127.0.0.1:5500/html/doback2.html">입장하기</a></button>
                    </div>
                </div>
        
            </div>
        
            <div class="userinfo">
        
                <h2>👤 내 정보</h2>
        
                <div class="info-box">
                    <p>닉네임</p>
                    <span>낙동유저</span>
                </div>
        
                <div class="info-box">
                    <p>보유 코인</p>
                    <span>12,500 코인</span>
                </div>
        
                <div class="info-box">
                    <p>출석 상태</p>
                    <span>오늘 출석 완료 ✅</span>
                </div>
        
                <button class="mypage">마이페이지</button>
        
            </div>
        
        </div>
        
        <footer class="barr">
            협찬 / 문의 : myse_731
        </footer>
        
        </body>
        </html>
        ```
        
    - 로그인 화면
        
        
        ```jsx
        #CSS
        
        body{
            margin: 0;
            min-height: 100vh;
        
            background: linear-gradient(
                180deg,
                #12001f 0%,
                #250040 50%,
                #100018 100%
            );
        
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        .container{
            background-color: transparent;
        }
        
        .logbox{
            width: 650px;
            height: 800px;
        
            background: rgba(15,15,15,0.95);
        
            border: 4px solid gold;
        
            border-radius: 20px;
        
            box-shadow:
                0 0 15px gold,
                0 0 40px rgba(255,215,0,0.4);
        
            color: white;
        }
        
        .logo{
            text-align: center;
        
            font-size: 72px;
        
            color: gold;
        
            margin-top: 30px;
        
            letter-spacing: 5px;
        
            text-shadow:
                0 0 10px gold,
                0 0 20px orange,
                0 0 40px orange;
        }
        
        .log1,
        .log2{
            width: 70%;
            height: 60px;
        
            margin-top: 25px;
        
            display: block;
        
            margin-left: auto;
            margin-right: auto;
        
            background-color: #1d1d1d;
        
            border: 2px solid gold;
        
            border-radius: 10px;
        
            color: white;
        
            font-size: 16px;
        }
        
        input::placeholder{
            color: #cfcfcf;
            padding-left: 10px;
        }
        
        .keep-login{
            display: block;
            width: 70%;
            margin: 15px auto 0;
            font-size: 15px;
            color: white;
            cursor: pointer;
        }
        
        .keep-login input[type="checkbox"]{
            width: 18px;
            height: 18px;
            vertical-align: middle;
        }
        
        .login{
            width: 70%;
            height: 60px;
        
            margin-top: 30px;
        
            margin-left: auto;
            margin-right: auto;
        
            background: linear-gradient(
                180deg,
                #ffd700,
                #ff9d00
            );
        
            border: 2px solid gold;
        
            border-radius: 10px;
        
            cursor: pointer;
        
            display: flex;
            justify-content: center;
            align-items: center;
        
            box-shadow:
                0 0 10px gold,
                0 0 20px orange;
        }
        
        .logms{
            color: black;
            font-size: 24px;
            font-weight: 700;
            margin: 0;
        }
        
        .links{
            display: flex;
            justify-content: space-between;
        
            width: 70%;
        
            margin: 20px auto 0;
        
            color: #e0e0e0;
        }
        
        .links span{
            cursor: pointer;
        }
        
        .links span:hover{
            color: gold;
        }
        
        .ml{
            display: flex;
            align-items: center;
        
            width: 70%;
        
            margin: 20px auto 0;
        
            color: #cfcfcf;
        }
        
        .ml::before,
        .ml::after{
            content: '';
            flex: 1;
            height: 1px;
            background-color: gold;
        }
        
        .ml::before{
            margin-right: 10px;
        }
        
        .ml::after{
            margin-left: 10px;
        }
        
        .naver,
        .google{
            width: 70%;
            height: 60px;
        
            margin: 20px auto 0;
        
            cursor: pointer;
        
            display: flex;
            align-items: center;
            justify-content: center;
        
            position: relative;
        
            border-radius: 10px;
        }
        
        .naver{
            background-color: rgb(24,200,74);
        }
        
        .google{
            background-color: white;
            border: 1px solid #ddd;
        }
        
        .naver img,
        .google img{
            width: 40px;
            height: 40px;
        
            position: absolute;
            left: 15px;
        }
        
        .naver p,
        .google p{
            margin: 0;
            font-weight: 600;
            font-size: 16px;
        }
        
        .slot-icons{
            text-align: center;
            font-size: 40px;
            margin-top: 20px;
        }
        ```
        
        ```jsx
        #HTML 
        
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link href ="../css/login.css" rel = "stylesheet">
        </head>
        <body>
            <div class="container">
                <div class="logbox">
                    <div class="slot-icons">🎰 🎰 🎰</div>
                    <h1 class="logo">LOGIN</h1>
                    <input type="text" class = "log1" placeholder="아이디">
                    <input type="password" class = "log2" placeholder="비밀번호">
                    <label class="keep-login">
                        <input type="checkbox"> 로그인 상태 유지
                    </label>
                    <div class="login">
                        <p class="logms">로그인</p>
                    </div>
                    <div class="links">
                        <span>회원 가입</span>
                        <span>아이디 찾기</span>
                        <span>비밀번호 재설정</span>
                    </div>
                    <p class="ml">또는</p>
                    <div class="naver">
                        <img src="../unnamed.png">
                        <p style="color: black;">Naver로 로그인</p>
                    </div>
                    <div class="google">
                        <img src="../images-4.png"> 
                        <p style="color: black;">Google로 로그인</p>
                    </div>
                </div>
            </div>
            
        </body>
        </html>
        ```
        
    - 충전 화면
        
        
    - 슬롯 화면
        
        
    - 룰렛 화면
        
        
- DB 테이블
    - users 테이블 : user의 정보를 저장하는 테이블
    
    | 컬럼명 | 설명 |
    | --- | --- |
    | user_id | 회원 번호 |
    | user_name | 회원 아이디 |
    | password | 비밀번호 |
    | coin | 보유 코인 |
    - charge_history 테이블 : 충전 기록 저장
    
    | 컬럼명 | 설명 |
    | --- | --- |
    | charge_id | 충전 번호 |
    | user_id | 회원 번호 |
    | amount | 충전 코인 |
    | charge_data | 날짜 |
    - gamg_history 테이블 : 게임 결과 저장
    
    | 컬럼명 | 설명 |
    | --- | --- |
    | game_id | 게임 번호 |
    | user_id | 회원 번호 |
    | game_type | 게임 종류 |
    | bet_coin | 베팅 코인 |
    | result | 승/패 |
    | created_at | 날짜 |

#### 팀원

- 권민세(팀장)
    - 홈, 로그인, 충전 화면 제작 담당
    - DB 설계
- 방윤선(팀원)
    - 게임 화면 제작 담당
    - DB 설계
// 서버 대신 쓸 가짜 데이터
const fakeNow = { id: 3, temperature: 24, humidity: 55, created_at: "2026-10-26 10:10:00" };
const fakeRecords = [
    { id: 2, temperature: 25, humidity: 50, created_at: "2026-10-26 10:05:00" },
    { id: 1, temperature: 24, humidity: 55, created_at: "2026-10-26 10:00:00" }
];

// 기록 목록으로 표를 다시 그림
function showRecords(records) {
    let html = "";
    // ✏️ 직접 작성하기 : records 를 하나씩 꺼내 html 에 <tr> 한 줄씩 이어 붙일 것
    records.forEach(r => {
        html += `<tr><td>${r.id}</td><td>${r.created_at}</td><td>${r.temperature}°C</td><td>${r.humidity}%</td></tr>`;
    });
    document.getElementById("table").innerHTML = html;
}


document.getElementById("now").addEventListener("click", function () {
    showRecords([fakeNow]);     // 기록 하나를 [ ] 로 감싸 목록으로 넘김
});

document.getElementById("record").addEventListener("click", function () {
    // ✏️ 직접 작성하기 : 가짜 기록으로 표를 그림
    showRecords(fakeRecords);
});
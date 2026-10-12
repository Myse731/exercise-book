const fakePhotos = [
    { title: "사진 1", img: "https://picsum.photos/seed/1/600" },
    { title: "사진 2", img: "https://picsum.photos/seed/2/600" },
    { title: "사진 3", img: "https://picsum.photos/seed/3/600" }
];

const gallery = document.getElementById("gallery");
const moreBtn = document.getElementById("more");

// 사진 목록을 받아 화면에 붙임
function showPhotos(photos) {
    let html = "";
    photos.forEach(photo => {
        html += `
            <div class="col-4 mb-3">
                <img src="${photo.img}" class="img-fluid">
                <p>${photo.title}</p>
            </div>
        `;
    });
    gallery.insertAdjacentHTML("beforeend", html);
}

// 더 보기 버튼 (예시로 완성해둠)
moreBtn.addEventListener("click", function () {
    showPhotos(fakePhotos);
});
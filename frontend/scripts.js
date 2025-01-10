// frontend/scripts.js
document.addEventListener("DOMContentLoaded", function() {
    fetch('/videos/1')
        .then(response => response.json())
        .then(data => {
            document.getElementById('video-title').innerText = data.title;
            document.getElementById('video-author').innerText = `Author: ${data.author.name} (${data.author.subscribers} subscribers)`;
            document.getElementById('video-views').innerText = `Views: ${data.views}`;
            document.getElementById('video-likes').innerText = `Likes: ${data.likes}`;

            const commentsList = document.getElementById('comments-list');
            data.comments.forEach(comment => {
                const li = document.createElement('li');
                li.innerText = comment;
                commentsList.appendChild(li);
            });
        });

    fetch('/recommended/')
        .then(response => response.json())
        .then(data => {
            const recommendedList = document.getElementById('recommended-list');
            data.forEach(video => {
                const li = document.createElement('li');
                li.innerHTML = `
                    <img src="${video.preview_url}" alt="${video.title}" width="100">
                    <div>
                        <h4>${video.title}</h4>
                        <p>Author: ${video.author.name}</p>
                        <p>Views: ${video.views}</p>
                    </div>
                `;
                recommendedList.appendChild(li);
            });
        });
});
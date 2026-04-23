// Simulate loading more content as the user scrolls
window.addEventListener('scroll', () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        loadMorePosts();
    }
});

function loadMorePosts() {
    const container = document.querySelector('.infinite-scroll');
    for (let i = 0; i < 3; i++) {
        const post = document.createElement('div');
        post.className = 'post';
        post.textContent = `Post ${container.children.length + 1}`;
        container.appendChild(post);
    }
}
const container = document.querySelector('.infinite-scroll');
const loadingIndicator = document.querySelector('.loading-indicator');
const backToTopBtn = document.getElementById('back-to-top');

window.addEventListener('scroll', () => {
  if (window.scrollY > 400) {
    backToTopBtn.style.display = 'block';
  } else {
    backToTopBtn.style.display = 'none';
  }

  if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
    loadMorePosts();
  }
});

backToTopBtn.addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});

function loadMorePosts() {
  loadingIndicator.style.display = 'block';
  setTimeout(() => {
    for (let i = 0; i < 3; i++) {
      const post = document.createElement('div');
      post.className = 'post';
      post.textContent = `Post ${container.children.length + 1}`;
      container.appendChild(post);
    }
    loadingIndicator.style.display = 'none';
  }, 1000);
}
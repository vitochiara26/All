let currentPage = 1;
const postsPerPage = 3;
const totalPosts = 9; 
const totalPages = Math.ceil(totalPosts / postsPerPage);
const container = document.querySelector('.pagination');
const prevButton = document.querySelector('.prev');
const nextButton = document.querySelector('.next'); 

function renderPosts() {
  container.innerHTML = '';
  const start = (currentPage - 1) * postsPerPage;
  const end = start + postsPerPage;
  for (let i = start; i < end && i < totalPosts; i++) {
    const post = document.createElement('div');
    post.className = 'post';
    post.textContent = `Post ${i + 1}`;
    container.appendChild(post);
  }
  prevButton.disabled = currentPage === 1;
  nextButton.disabled = currentPage === totalPages;
}

prevButton.addEventListener('click', () => {
  if (currentPage > 1) {
    currentPage--;
    renderPosts();
  }
});

nextButton.addEventListener('click', () => {
  if (currentPage < totalPages) {
    currentPage++;
    renderPosts();
  }
});

renderPosts();
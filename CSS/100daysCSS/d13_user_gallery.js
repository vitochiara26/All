document.querySelectorAll('.profile').forEach(profile => {
    profile.addEventListener('click', () => {
        document.querySelectorAll('.detail').forEach(detail => {
            detail.classList.add('active');
        });
    });
});

document.querySelectorAll('.close').forEach(closeBtn => {
    closeBtn.addEventListener('click', () => {
        document.querySelectorAll('.detail').forEach(detail => {
            detail.classList.remove('active');
        });
    });
});
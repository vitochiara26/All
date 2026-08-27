let droppedFiles = false;
let fileName = '';
let uploading = false

const dropzone = document.querySelector('.dropzone');
const button = document.querySelector('.upload-btn');
const syncing = document.querySelector('.syncing');
const done = document.querySelector('.done');
const bar = document.querySelector('.bar');
const fileInput = document.querySelector('.input');
const fileNameSpan = document.querySelector('.filename');
const uploadImg = document.querySelector('.dropzone .upload');

const dragEvents = ['drag', 'dragstart','dragend', 'dragover', 'dragenter', 'dragleave', 'drop'];
dragEvents.forEach(eventName => {
    dropzone.addEventListener(eventName, (e) => {
        e.preventDefault();
        e.stopPropagation();
    });
});

['dragover', 'dragenter'].forEach(eventName => {
    dropzone.addEventListener(eventName, () => {
        dropzone.classList.add('is-dragover');
    });
});

['dragleave', 'dragend', 'drop'].forEach(eventName => {
    dropzone.addEventListener(eventName, () => {
        dropzone.classList.remove('is-dragover');
    });
});


dropzone.addEventListener('drop', (e) => {
    droppedFiles = e.dataTransfer.files;
    if (droppedFiles.length > 0) {
        fileName = droppedFiles[0].name;
        fileNameSpan.textContent = fileName;
        uploadImg.style.display = none;
    }
});

fileInput.addEventListener('change', (e) => {
    if (e.target.files.length > 0) {
        fileName = e.target.files[0].name;
        fileNameSpan.textContent = fileName;
        uploadImg.style.display = none;
    }
});

button.addEventListener('click', startUpload);

function startUpload() {
    if (!uploading && fileName !== '') {
        uploading = true;
        button.textContent = 'Uploading...';

        dropzone.style.transition = 'opacity 0.4s ease';
        dropzone.style.opacity = '0'
        setTimeout(() => {
            dropzone.style.display = 'none';
        }, 400);

        syncing.classList.add('active');
        done.classList.add('active');
        bar.classList.add('active');
        
        setTimeout(showDone, 3200)
    }
}

function showDone() {
    button.textContent = 'Done';
}
const markdownInput = document.getElementById("markdown-input");
const htmlOutput = document.getElementById("html-output");
const preview = document.getElementById("preview");

JavaScript
function convertMarkdown() {
    return markdownInput.value
        .replace(/^\s*### (.*)$/gm, '<h3>$1</h3>')
        .replace(/^\s*## (.*)$/gm, '<h2>$1</h2>')
        .replace(/^\s*# (.*)$/gm, '<h1>$1</h1>')
        .replace(/^\s*> (.*)$/gm, '<blockquote>$1</blockquote>')
        .replace(/!\[(.*?)\]\((.*?)\)/g, '<img alt="$1" src="$2">')
        .replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2">$1</a>')
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/__(.*?)__/g, '<strong>$1</strong>')
        .replace(/\*(.*?)\*/g, '<em>$1</em>')
        .replace(/_(.*?)_/g, '<em>$1</em>')
        .replace(/\n/g, '');
}

// Escuchador de eventos en tiempo real
markdownInput.addEventListener("input", () => {
    const convertedHtml = convertMarkdown();
    htmlOutput.textContent = convertedHtml;
    preview.innerHTML = convertedHtml;
});
const themes = [
    {
        name: "light",
        message: "Hello sunshine — Light theme is on!"
    },
    {
        name: "dark",
        message: "The night is yours — Dark theme is on!"
    },
    {
        name: "ocean",
        message: "Blue skies and high tides — Ocean theme is on!"
    },
    {
        name: "frost",
        message: "The frost has settled - Frost theme is on!"
    }
];

const themeButton = document.getElementById("theme-switcher-button");
const themeDropdown = document.getElementById("theme-dropdown");
const statusContainer = document.querySelector("[aria-live='polite']");
const themeOptions = document.querySelectorAll("#theme-dropdown [role='menuitem']");

themeButton.addEventListener('click', () => {
    const isExpanded = themeButton.getAttribute("aria-expanded") === "true";

    if (isExpanded) {
        themeDropdown.hidden = true;
        themeButton.setAttribute("aria-expanded", "false");
    } else {
        themeDropdown.hidden = false;
        themeButton.setAttribute("aria-expanded", "true");
    }
});

themeOptions.forEach((option) => {
    option.addEventListener('click', () => {
        const selectedText = option.textContent.trim();
        const matchedTheme = themes.find((t) => t.name === selectedText.toLowerCase());

        if (matchedTheme) {
            const activeThemeClasses = Array
            .from(document.body.classList).filter((cls) => cls.startsWith("theme")
            );
            activeThemeClasses.forEach((cls) => document.body.classList.remove(cls));

            document.body.classList.add(`theme-${matchedTheme.name}`);

            statusContainer.textContent = matchedTheme.message;
        }

        themeDropdown.hidden = true;
        themeButton.setAttribute("aria-expanded", "false");
    });
});
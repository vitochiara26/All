const books = [
    {
        title: 'The Embedded Entrepreneur',
        authorName: 'Arvid Kahl',
        releaseYear: 2021,
    },
    {
        title: 'Rich Dad Poor Dad',
        authorName: 'Robert Kiyosaki and Sharon Lechter',
        releaseYear: 1997,
    },
    {
        title: 'Atomic Habits',
        authorName: 'James Clear',
        releaseYear: 2018,
    }
]

function sortByYear(book1, book2) {
    if (book1.releaseYear < book2.releaseYear) {
        return -1;
    }
    else if (book1.releaseYear > book2.releaseYear) {
        return 1;
    } else {
        return 0;
    }
}

const targetYear = 2020;
const filteredBooks = books.filter((book) => book.releaseYear < targetYear);

filteredBooks.sort(sortByYear);

console.log(filteredBooks);
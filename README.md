# Library Management System

This is a simple Library Management System built using Python and Tkinter. The system allows users to manage books and members, checkout and return books, and save/load library data to/from a file.

## Features

- Add new books to the library.
- Add new members to the library.
- Checkout and return books.
- Save library data to a file.
- Load library data from a file.
- Search for books by title, author, or ISBN.
- Sort books by title, author, or publication date.

## Requirements

- Python 3.12
- Tkinter (usually included with Python installations)

## Usage

1. Clone the repository or download the code.
2. Run the `main.py` file to start the application.
3. Use the GUI to manage books and members.

## Running the Application


## GUI Elements

- **Book List:** Displays the list of books in the library.
- **Member ID:** Field to enter the member ID for checking out and returning books.
- **ISBN:** Field to enter the ISBN of the book for checking out and returning books.
- **Checkout Book Button:** Checks out the book with the entered ISBN for the member with the entered ID.
- **Return Book Button:** Returns the book with the entered ISBN for the member with the entered ID.
- **Add New Book Section:**
- **Title:** Field to enter the title of the new book.
- **Author:** Field to enter the author of the new book.
- **ISBN:** Field to enter the ISBN of the new book.
- **Publication Date:** Field to enter the publication date of the new book.
- **Add Book Button:** Adds the new book to the library.
- **Add New Member Section:**
- **Name:** Field to enter the name of the new member.
- **Member ID:** Field to enter the member ID of the new member.
- **Add Member Button:** Adds the new member to the library.
- **Save Data Button:** Saves the current library data to `library_data.json`.
- **Load Data Button:** Loads the library data from `library_data.json`.

## Example Data

The application comes with some sample data:

### Books
- "The Great Gatsby" by F. Scott Fitzgerald (ISBN: 1234567890, Published: 1925)
- "1984" by George Orwell (ISBN: 2345678901, Published: 1949)

### Members
- Alice (Member ID: 1)
- Bob (Member ID: 2)

## Code Structure

- **library.py:** The main application file containing the GUI and library management logic.
- **library_data.json:** The file where library data is saved and loaded.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the LICENSE.txt file for details.

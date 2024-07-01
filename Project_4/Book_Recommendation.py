import pandas as pd

# Load the dataset
books_df = pd.read_csv('Project_1/books.csv')

class Rec():
    def __init__(self,books_store):
        self.books = books_store
        self.first = True
        self.interface()

    def search_books(self,keyword):
        self.first = False
        keyword = keyword.lower()
        results = self.books[
            books_df['title'].str.lower().str.contains(keyword) |
            books_df['authors'].str.lower().str.contains(keyword) |
            books_df['publisher'].str.lower().str.contains(keyword)
        ]

        self.display_books(results)

    def display_books(self,books):
        if not len(books):
            print("No books found.")
        else:
            for index, book in books.iterrows():
                print(f" Title: {book['title']}")
                print(f" Author: {book['authors']}")
                print(f" Average Rating: {book['average_rating']}")
                print(f" ISBN: {book['isbn']}")
                print(f" ISBN13: {book['isbn13']}")
                print(f" Language: {book['language_code']}")
                if 'num_pages' in book: print(f" Number of Pages: {book['num_pages']}")
                print(f" Ratings Count: {book['ratings_count']}")
                print(f" Text Reviews Count: {book['text_reviews_count']}")
                print(f" Publication Date: {book['publication_date']}")
                print(f" Publisher: {book['publisher']}")
                print('\n')

        self.interface()

    def interface(self):
        if self.first:
            print( "Welcome to the Book Recommendation Program!")
        else:
            print(" Another Search?")

        keyword = input(" Enter a keyword to search for books: ")
        self.search_books(keyword)

book_search = Rec(books_store=books_df)



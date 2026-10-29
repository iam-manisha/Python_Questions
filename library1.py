
class Library:
    library_name = "QSP"
    books = {
        'python':10,
        'java':20,
        'sql':10,
        'html':20
    }
    no_of_books = 5


    def __init__(self,name,book={}):
        self.name = name
        self.book = book

    def available_books(self):
        print("1.Library Books\n2.User Books")
        choice = int(input("Enter Your Choice:"))
        if choice == 1:
            for i,j in self.books.items():
                print("Book Name:",i,"Quantity:",j)
        else:
            if self.book != {}:
                for i,j in self.book.items():
                    print("Book Name:",i,"Quantity:",j)
            else:
                print("No books Taken")

    def issue_book(self):
        bk = input("Enter the Book Name:").lower()
        if bk in self.books:
            print("Book Available")
            q = int(input("Enter the Quantity:"))
            if q<=self.books[bk]:
                print("Book issued Successfully")
                self.book[bk] = q
                self.books[bk]-=q
            else:
                print(f"Limited Quantity Availble {self.books[bk]}")
        else:
            print("Out of Stock")

user = Library("Chandan")
user.available_books()
user.issue_book()
user.available_books()
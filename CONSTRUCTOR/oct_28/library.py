#1.wap to create a class called Library create 3 generic property and 5 specific property and 3 object method called issue book,return book,available book and each object can take only 5 books(maximum)

class Library:
    lib_name="The Library"
    lib_loc="Marathahalli"

    books={
          "python":10,
          "java":20,
          "sql":10,
          "html":20
    }

    no_of_books=5
    
    def __init__(self,name,book={}):
        self.name=name
        self.book = book

    def available_book(self):
        print("1.Library Books \n2.User Books")
        choice = int (input("Enter your choice"))
        if choice==1:
            for i ,j in self.books.items():
                print("Book Name:",i,"Quantity".j)
        else:
            if self.book != {}:
                for i,j in self.books.items():
                    print("Book Name:",i,"Quantity:",j)
            else:
                print("No Book Taken")

    def issue_book(self):
        bk= input("enter the book name:").lower()
        if bk in self.books:
            print("Book Available")
            q=int(input("enter the quantity"))
            if q<=self.book:

        

    
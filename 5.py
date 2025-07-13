print("The Library Managment System:\n")
class Library:
    books=["Bhagwat Geeta","Bible","Shiv puran","Discovery of india","time travel","The Secret","A brief history of time","Parallel Universes"]
    Number_of_books=len(books)
    def aDD_Books(self,name):
        self.name=name
        self.books.append(self.name)
    def No_of_books(self):
        print("The number of books in the library are:", len(self.books))
    
    def Name_of_books(self):
           print("The books in the library are:")
           for book in self.books:
                print(book)
    

    
boki1=Library()
boki1.aDD_Books("Mahabharat")
boki1.Name_of_books()
boki1.No_of_books()

boki1.aDD_Books("Space and brief of the times")
boki1.Name_of_books()
boki1.No_of_books()

boki1.aDD_Books("C++ Programming")
boki1.Name_of_books()
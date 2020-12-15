class PreciousStone:
    numberOfPreciousStones = 0
    preciousStoneCollection = []
    def __init__(self, name):
        self.name = name
        # Increment the number of preciousStones
        PreciousStone.numberOfPreciousStones += 1
        # Append the precious stone to the list if total number of stones are less than 5
        if PreciousStone.numberOfPreciousStones <= 5:
            PreciousStone.preciousStoneCollection.append(self)
        else:
            # If more than 5 stones are present, delete the first one and store the new one
            del PreciousStone.preciousStoneCollection[0]
            PreciousStone.preciousStoneCollection.append(self)

    @staticmethod
    def displayPreciousStones():
        for preciousStone in PreciousStone.preciousStoneCollection:
            print(preciousStone.name, end = ' ')
        print()

preciousStoneOne  = PreciousStone("Ruby")
preciousStoneTwo  = PreciousStone("Emerald")
preciousStoneThree  = PreciousStone("Sapphire")
preciousStoneFour  = PreciousStone("Diamond")
preciousStoneFive  = PreciousStone("Amber")
preciousStoneFive.displayPreciousStones()
preciousStoneSix = PreciousStone("Onyx")
# Print all the stones after deleting the first stone
preciousStoneSix.displayPreciousStones()

class Library:
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
    def displayAvailableBooks(self):
        print()
        print("Available Books: ")
        for book in self.availableBooks:
            print(book)
    def lendBook(self,requestedBook):
        if requestedBook in self.availableBooks:
            print("you have now borrowed the book")
            self.availableBooks.remove(requestedbook)
        else:
            print("sorry the book is not availble in our list. ")
            
    def addBook(self,returnedBook):
        self.availableBooks.append(returnedBook)
        print("You have return the book. Thank You!")
class Customer:
    def requestBook(self) :
        print()
        print("Enter the name of a book you would like to borrow: ")
        self.book = input()
        return self.book
        print()
    def returnBook(self):
        print()
        print("Enter the name of book which you are returning: ")
        self.book = input()
        return self.book
        print()
        
library = Library(['Think & Grow Rich','Who will Cry When you die','For One More Day','Ignited minds'])
customer= Customer()
while True:
    print("Enter 1 to display to available the book ")
    print("Enter 2 to request for a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    userChoice = int(input())
    if userChoice is 1:
        library.displayAvailableBooks()
    elif userChoice is 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice is 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    elif userChoice is 4:
        quit()

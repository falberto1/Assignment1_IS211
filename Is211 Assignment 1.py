# Class declaration
class Book:
    # Variables declaration
    author = ''
    title = ''

    # Constructer method with variables
    def __init__(self, author, title):
        self.author = author
        self.title = title

    # Method to display book infomation
    def display(self):
        print(self.title + ", written by " + self.author)


# Creating two objects of Book class
obj1 = Book('Jay Shetty', 'Think Like a Monk')
obj2 = Book('Guy Raz', 'How I Built This')

# Calling method of Book class to display book details
obj1.display()
print()
obj2.display()
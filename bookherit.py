class book:

   def __init__(self,author,title):
      self.author=author
      self.title=title

   def display(self):
      print("The author of a book is",author)
      print("The title is",title)


author=input("Enter the author:")
title=input("Enter the title:")

b=book(author,title)
b.display()

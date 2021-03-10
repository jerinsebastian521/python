class publisher:
    def title(self):
        print("TITLE OF BOOK")

    def author(self):
        print("AUTHOR OF THE BOOK::*********")


class book(publisher):
    def title(self):
        print("BOOK NAME is python")

    def price(self):
        print("Price of the book:343")

    def no_of_page(self):
        print("NO_OF_PAGES:1000")


obj = book()
obj.title()
obj.author()
obj.price()
obj.no_of_page()

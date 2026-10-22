class Publication:
    def __init__(self, title, author):
        self.__title = __title
        self.__author = __author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print(f"Title: {self.__title]")
        print(f'Author: {self.__author")

class Book(Publication):
    def __init__(self, __title, __author, __number_of_pages):
        super().__init__(__title, __author)
        self.__number_of_pages = __number_of_pages

        

class Magazine(Publication):
    def __init__(self, __title, __author, __issue_number):
        super().__init__(__title, __author)
        self.issue_number = __issue_number

    def get_issue_number(self):
        return __issue_number

    def set_issue_number(self, issue_number):
        if issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("Issue number must be positive")
             



pub1 = Publication("Journal of Experimental Psycology", "Ratchiff. R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

print("Publication Information")
pub1.display_info

print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print(book1.get_number_of_pages())


print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())

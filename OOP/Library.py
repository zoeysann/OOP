# so it's the LIBRARY i guess
from datetime import timedelta, datetime

class Library():
    def __init__(self, username):
        self.username = username

    def due_time(self):
        borrow_date_str = self.borrow_date
        borrow_date_obj = datetime.strptime(borrow_date_str, "%d-%m-%Y")
        return borrow_date_obj + timedelta(days=21)
    
    def __str__(self):
        return f"\nStatus: {self.username} took '{self.book_name}' by {self.book_author} in {self.borrow_date}.\nAnd the Due Time is {due_date}"
    
    
    def user_info(self, user_id, age, borrow_date):
        self.user_id = user_id
        self.age = age
        self.borrow_date = borrow_date
        return f"\nHello {self.username}, Your ID is {self.user_id}"
    
    def book_info(self, book_id, book_name, book_author, year):
        self.book_id = book_id
        self.book_name = book_name
        self.book_author = book_author
        self.year = year
        return f"\nThe book is {self.book_name} by {self.book_author}. It's published in {self.year}\nIn our Library this book is with ID {self.book_id}\n"

me = Library('zoeysann')
info = me.user_info('054', 17, '01-03-2024')
book_info = me.book_info('3022', "A.S.S.A.S.I.N", 'A.Melik.Ibrahimov', 2017)
due_date = me.due_time()

print(info, me, book_info, sep="\n")
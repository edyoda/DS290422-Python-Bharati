class book:

    def __init__(self,book_id,book_name,book_author,book_publisher,book_price):
        self.book_id = book_id
        self.book_name = book_name
        self.book_author = book_author
        self.book_publisher = book_publisher
        self.book_price = book_price

    def __str__(self): #overridding
        return f"Book ID : {self.book_id} \nBook Name : {self.book_name} \nBook Author : {self.book_author} \nBook Publisher : {self.book_publisher} \nBook Price : {self.book_price}" 

    def set_book_id(self,book_id):
        self.book_id = book_id

    def get_book_id(self):
        return self.book_id

    def set_book_name(self,book_name):
        self.book_name = book_name

    def get_book_name(self):
        return self.book_name

    def set_book_author(self,book_author):
        self.book_author = book_author

    def get_book_author(self):
        return self.book_author

    def set_book_publisher(self,book_publisher):
        self.book_publisher = book_publisher

    def get_book_publisher(self):
        return self.book_publisher

    def set_book_price(self,book_price):
        self.book_price = book_price

    def get_book_price(self):
        return self.book_price


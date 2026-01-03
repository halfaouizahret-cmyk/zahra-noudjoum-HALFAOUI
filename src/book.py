def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        self.available = False

    def return_book(self):
        self.available = True

    def __str__(self):
        status = "Disponible" if self.available else "Emprunté"
        return f"[{self.book_id}] {self.title} - {self.author} ({status})"

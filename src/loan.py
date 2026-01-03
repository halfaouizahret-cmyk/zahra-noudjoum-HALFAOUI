  def __init__(self, book, user):
        self.book = book
        self.user = user

    def __str__(self):
        return f"Le livre '{self.book.title}' est emprunté par {self.user.name}"

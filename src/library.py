from book import Book
from user import User
from loan import Loan

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.loans = []

    # Ajouter un livre
    def add_book(self, book_id, title, author):
        self.books.append(Book(book_id, title, author))

    # Supprimer un livre
    def remove_book(self, book_id):
        self.books = [b for b in self.books if b.book_id != book_id]

    # Inscrire un utilisateur
    def add_user(self, user_id, name):
        self.users.append(User(user_id, name))

    # Emprunter un livre
    def borrow_book(self, book_id, user_id):
        book = next((b for b in self.books if b.book_id == book_id and b.available), None)
        user = next((u for u in self.users if u.user_id == user_id), None)

        if book and user:
            book.borrow()
            self.loans.append(Loan(book, user))
            print("Emprunt effectué avec succès ✅")
        else:
            print("Livre non disponible ou utilisateur inexistant ❌")

    # Retourner un livre
    def return_book(self, book_id):
        loan = next((l for l in self.loans if l.book.book_id == book_id), None)
        if loan:
            loan.book.return_book()
            self.loans.remove(loan)
            print("Livre retourné avec succès ✅")
        else:
            print("Ce livre n'est pas emprunté ❌")

    # Afficher l'état du système
    def display_status(self):
        print("\n📚 Livres :")
        for book in self.books:
            print(book)

        print("\n👤 Utilisateurs :")
        for user in self.users:
            print(user)

        print("\n🔗 Emprunts :")
        if not self.loans:
            print("Aucun emprunt en cours")
        for loan in self.loans:
            print(loan)

▶️ 5️⃣ Fichier main.py
from library import Library

library = Library()

while True:
    print("\n--- 📖 Bibliothèque Numérique ---")
    print("1. Ajouter un livre")
    print("2. Supprimer un livre")
    print("3. Inscrire un utilisateur")
    print("4. Emprunter un livre")
    print("5. Retourner un livre")
    print("6. Afficher l'état du système")
    print("7. Quitter")

    choice = input("Votre choix : ")

    if choice == "1":
        library.add_book(
            input("ID du livre : "),
            input("Titre : "),
            input("Auteur : ")
        )

    elif choice == "2":
        library.remove_book(input("ID du livre : "))

    elif choice == "3":
        library.add_user(
            input("ID de l'utilisateur : "),
            input("Nom de l'utilisateur : ")
        )

    elif choice == "4":
        library.borrow_book(
            input("ID du livre : "),
            input("ID de l'utilisateur : ")
        )

    elif choice == "5":
        library.return_book(input("ID du livre : "))

    elif choice == "6":
        library.display_status()

    elif choice == "7":
        print("👋 Au revoir")
        break

    else:
        print("Choix invalide ❌")

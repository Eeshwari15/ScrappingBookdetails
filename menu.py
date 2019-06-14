from app import books
USER_CHOICE='''
Enter your choice:
b:to look at 5 star books
c:to look at cheapest books
n:to look at next available book
q:to quit'''

def menu():
    USER_INPUT=input("Enter your choice")
    while USER_INPUT!='q':
        if USER_INPUT=='b':
            print_best_books()
        elif USER_INPUT=='c':
            cheapest_books()
        elif USER_INPUT=='n':
            print_next_books()
        else:
            print("Enter a valid choice")
        USER_INPUT=input("Enter your choice")

def print_best_books():
    best_books = sorted(books, key=lambda x:(x.rating*-1,x.price))
    for book in best_books:
        print(book)
def cheapest_books():
    cheapest=sorted(books,key=lambda x:x.price)[:10]
    for b in cheapest:
        print(b)

books_generator=(x for x in books)
def print_next_books():
    print(next(books_generator))
menu()
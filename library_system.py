books = [
  
  
]

print("CLI Based Library Management System \n")
def start_process():
    print(
        "What do you want to do? \n",
        "1. Add Book \n",
        "2. View Books \n",
        "3. Update A Book \n",
        "4. Delete A Book \n", 
        "5. Exit"
    )
    option = input("Choose one option: ")

    while True:
        if option == "1":
            add_book(books)
        elif option == "2":
            view_books(books)
        elif option == "3":
            update_books(books)
        elif option == "4":
            delete_books(books)
        elif option == "5":
            break
    



def add_book(books):
    global book_number
    
    while True:
        print("type'done' to stop")
        title = input("what's the title: ")
        title.lower()
        author = input("who's the author: ")
        author.lower()
        rstatus = input("what's the read status : " )
        rstatus.lower()
        if title == 'done'or author == 'done' or rstatus ==  'done':
            start_process(books)
        book_number += 1
        books.append({ {'book_number':str(book_number),'title': title, 'author': author, 'rstatus': rstatus}})
        return books


def view_books(books):
    print('These are the books')
    for items in books:
        books1=( items['title'] , items['author'])
        print(books1)
    start_process()


def update_books(books):
    print('Which Book do you want to update')
    book2 =[] 
    for items in books:
         book2.append((items['title'] , items['author']))
    print(book2)

    option = input('Your choice is ? Ex. Title ')
    option = option.lower()

    for items in books:
        if option in items['title']:
            items['title'] = input('what is the title? ')
            items['author'] = input("who's the author? ")
            items['rstatus'] = input('Read / Unread')
            return items['title'] , items['author'], items['rstatus']
        
    else: 
        print('invalid input')
        start_process()

        

def delete_books (books):
    print('this is a danger zone anything you delete is not undoable')
    for items in books:
        books3 = items['book_number'] , items['title']
        print(books3)


    option = input('What book do you want to delete ? Ex. "title"')
    option = option.lower()

    for book in books:
        if option in book['title']:
            books.remove(book)
            break
    
    else:
        print('book not found')
        start_process()


start_process()

      
            
    
        

        





        


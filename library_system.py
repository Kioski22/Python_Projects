books = [
  
  
]

print("--------------------------CLI Based Library Management System------------------------------------------------- \n")
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
            break
        elif option == "2":
            view_books(books)
            break
        elif option == "3":
            update_books(books)
            break
        elif option == "4":
            delete_books(books)
            break
        else:
            break
    



def add_book(books):
    
    global book_number
    
    
    
    while True:
        
        print("type'done' to stop")
        
        title = input("what's the title: ")
        title = title.lower()
        if title == 'done':
            return start_process()
            


        author = input("who's the author: ")
        author = author.lower()
        if author == 'done':
            return start_process()
           
  
        rstatus = input("what's the read status : " )
        rstatus = rstatus.lower()
        if rstatus == 'done':
            return start_process()
           
        

            
        book_number += 1
        books.append({'book_number':str(book_number),'title': title, 'author': author, 'rstatus': rstatus})
    
book_number = 0

def view_books(books):
    print('These are the books')
    for items in books:
        books1=[ items['title'] , items['author'], items ['rstatus']] 
        print(f"Title :{books1[0]},  Author : {books1[1]} ,  Read Status : {books1[2]}")
    return start_process()


def update_books(books):
    print('Which Book do you want to update')
    book2 =[] 
    for items in books:
         book2.append((items['title'] , items['author'] , items['rstatus']))
    print(book2)

    option = input('Your choice is ? Ex. Title ')
    if option == 'done':
        return start_process()
    option = option.lower()

    for items in books:
        if option in items['title']:
            items['title'] = input('what is the title? ')
            items['author'] = input("who's the author? ")
            items['rstatus'] = input('Read / Unread? ')
            return items['title'] , items['author'], items['rstatus']
    
    else: 
        print('invalid input')
        start_process()

        

def delete_books (books):
    print('this is a danger zone anything you delete is not undoable')
    for items in books:
        books3 = items['book_number'] , items['title']
        print(books3)


    option = input('What book do you want to delete ? Ex. "title" ')
    if option == 'done':
        return start_process()
    elif option == '5':
        return
    option = option.lower()

    for book in books:
        if option in book['title']:
            books.remove(book)
            break 
        return start_process()
    
    else:
        print('book not found')
        return start_process()


start_process()

      
            
    
        

        





        


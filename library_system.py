books = [
  
  
]

print("CLI Based Library Management System \n")
# def start_process(option):
# print(
#     "What do you want to do? \n",
#     "1. Add Book \n",
#     "2. View Books \n",
#     "3. Read Status"
# )

# option = input("Choose one option: ")

# if option == "1":
#     add_book(books)
# elif option == "2":
#     view_books(books)
# elif option == "3":
#     Read_status(books)
# else: 
#     print("wrong input")


def add_book(books):
    while True:
        print("type'done' to stop")
        title = input("what's the title: ")
        author = input("who's the author: ")
        rstatus = input("what's the read status : " )
        books.append({'title': title, 'author': author, 'rstatus': rstatus})
        if title and author and rstatus ==  'done':
            start_process()
        return books


def view_books(books):
    for items in books:
        print('These are the books')
        books1=( items['title'] , items['author'])
        print(books1)
    start_process()


def update_books(books):
   

        


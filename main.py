class Library:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, "a+")
        #Söylendiği gibi dosyamızı "a+" modunda açıyoruz.
    def __del__(self):
        if self.file:
            self.file.close()
            #Burada da nesne silindiğinde dosyayı kapatıyoruz.
    def list_books(self):
        self.file.seek(0) #"books.txt" dosyasının en başına gitmek için kullandığımız komut
        books = self.file.read().splitlines() #"splitlines()" metodu her satırı bir liste öğesi olarak alır.
        if books: #Data olup olmadığını kontrol ediyoruz. Eğer varsa if bloğu çalışır. Yoksa else bloğu.
            print("Books:")
            for book in books:
                book_information = book.split(",") #Virgülle ayırlan kısmı ayırıyoruz.
                book_name = book_information[0].strip() #Listenin ilk öğesini yani kitap adını alıyoruz.
                book_author = book_information[1].strip()#Listenin ikinci öğesi yani yazarı alıyoruz.
                book_release_date = book_information[2].strip()#Listenin üçüncü öğesi yani yayın yılını alıyoruz.
                book_number_of_pages= book_information[3].strip()#Listenin dördüncü öğesi olana sayfa sayısını alıyoruz.
                print(f"Book Name: {book_name}, Author: {book_author}\n")
        else:
            print("There are no books in library")
    def add_book(self):#Kullanıcı books.txt dosyasına kitap ekleyecek.
            book_title = input("Enter the book title: ")
            book_author = input("Enter the book author: ")
            book_release_date = input("Enter the release date: ")
            book_number_of_pages = input("Enter the number of pages: ")
            book_info=f"{book_title.strip()}, {book_author.strip()},{book_release_date.strip()},{book_number_of_pages.strip()}\n"
            #strip()'i kullanma sebebimiz kullanıcı datayı girerken eğer boşluk bırakıyorsa onları silmek.
            self.file.write(book_info)
            print("Book added succesfully.")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book you want to remove: ") #Kullanıcının silmek istediği kitabın adını alıyoruz.
        self.file.seek(0) #Dosyanın başına gidiyoruz
        books = self.file.read().splitlines()#Her bir satırı okuyoruz çünkü her bir satır, bir kitap datası içeriyor.
        updated_books = [] #Yeni bir kitap listesi oluşturduk, silinecek kitap harici kitapları ekleyeceğiz.
        removed = False  #Kitabın olup olmadığını izlemek için bir boole.
        for book in books:
            book_information = book.split(",")
            book_name = book_information[0].strip() #Kitap adını alıyoruz.
            if book_name != title_to_remove: #Aldığımız kitap adı harici kitapları yeni listemize ekliyoruz.
                updated_books.append(book)
            else:
                removed = True #İlk listede kaldırmak istediğimiz kitap başlığı bulunursa bu kitap başarıyla kaldırılmış demektir.
        self.file.seek(0)
        self.file.truncate() #Dosyanın başına gidiyoruz ve dosyayı tamamen siliyoruz.
        for book in updated_books:
            self.file.write(book + "\n")  #Kaldırılan kitap olmayacak şekilde yeniden satır satır yazıyoruz.
        if removed:
            print("Book removed successfully.")
        else:
            print("Book not found.")

lib =Library("books.txt") #lib objesini oluşturduk.

#Menü
print("***MENU*** \n")
print("1) List Books:")
print("2) Add Book:")
print("3) Remove Book:")
print("q) Quit: \n")


while True:
    menu_choice = input("Enter Your Choice: ") #Kullanıcıdan seçeneğini alıyoruz. Hangisini seçerse ona yönlendiriyoruz.
    if menu_choice == "1":
        lib.list_books()
    elif menu_choice == "2":
        lib.add_book()
    elif menu_choice == "3":
        lib.remove_book()
    elif menu_choice == "q":
        print("Exiting...")
        break
    else:
        print("Please select a valid option.")

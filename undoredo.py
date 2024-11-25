undo_stack = []
redo_stack = []

def tambah_aksi (aksi):
    undo_stack.append(aksi)
    redo_stack.clear()  
    print("Aksi ",aksi,"ditambahkan.")
    print("Data setelah di-Undo Stack:", undo_stack)
    print("Data setelah di-Redo Stack:", redo_stack)

def undo():
    if undo_stack:
        aksi = undo_stack.pop()
        redo_stack.append(aksi)
        print("Undo dilakukan: ",aksi,".")
    else:
        print("Tidak ada aksi untuk di-undo!")
        print("Data setelah di-Undo Stack:", undo_stack)
        print("Data setelah di-Redo Stack:", redo_stack)

def redo():
    if redo_stack:
        aksi = redo_stack.pop()
        undo_stack.append(aksi)
        print("Redo dilakukan: ",aksi,".")
    else:
        print("Tidak ada aksi untuk di-redo!")
        print("Data setelah di-Undo Stack:", undo_stack)
        print("Data setelah di-Redo Stack:", redo_stack)
        
def menu():
    print("\n MENU ")
    print("1. Tambah Data")
    print("2. Undo Data")
    print("3. Redo Data")
    print("4. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        aksi = input("Masukkan data yang ingin dimasukkan: ")
        tambah_aksi (aksi)
    elif pilihan == "2":
        undo()
    elif pilihan == "3":
        redo()
    elif pilihan == "4":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid! Silakan pilih menu yang tersedia.")

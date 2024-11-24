undo_stack = []
redo_stack = []

def add_action(action):
    undo_stack.append(action)
    redo_stack.clear()  # Kosongkan redo stack setiap kali ada aksi baru
    print(f"Aksi '{action}' ditambahkan.")
    print("Data setelah di-Undo Stack:", undo_stack)
    print("Data setelah di-Redo Stack:", redo_stack)

def undo():
    if undo_stack:
        action = undo_stack.pop()
        redo_stack.append(action)
        print(f"Undo dilakukan: '{action}'.")
    else:
        print("Tidak ada aksi untuk di-undo!")
    print("Data setelah di-Undo Stack:", undo_stack)
    print("Data setelah di-Redo Stack:", redo_stack)

def redo():
    if redo_stack:
        action = redo_stack.pop()
        undo_stack.append(action)
        print(f"Redo dilakukan: '{action}'.")
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
        add_action(aksi)
    elif pilihan == "2":
        undo()
    elif pilihan == "3":
        redo()
    elif pilihan == "4":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid! Silakan pilih menu yang tersedia.")

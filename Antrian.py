from collections import deque
def antrian():
   queue = deque()
   while True:
       print("\n Menu ")
       print("1. tambah pelanggan ke antrian: ")
       print("2. layani pelanggan ")
       print("3. tampilkan antrian ")
       print("4. keluar ")
       pilihan = input("masukkan menu pilihan")

       if pilihan == "1" :
           nama = input("masukkan nama pelanggan")
           queue.append(nama)
           print ("palanggan",nama,"telah ditambahkan ke antrian")
       elif pilihan == "2" :
           if queue :
               dilayani = queue.popleft()
               print ("pelanggan",dilayani,"sedang dilayani")
           else :
               print("antrian kosong")
       elif pilihan == "3" :
           print("antrian saat ini", list(queue))
       elif pilihan == "4" :
           print("anda keluar dari program")
           break
       else :
           print("inputan anda tidak valid")
antrian()

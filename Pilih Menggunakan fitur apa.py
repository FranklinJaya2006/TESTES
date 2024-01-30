import time
from pydub import AudioSegment
from pydub.playback import play
from datetime import datetime, timedelta
import threading
import pygame

while True :
    print("========== Pilih Fitur Yang Ingin Digunakan ==========")
    print("=========>>> 1. Untuk menggunakan fitur APP LOCK")
    print("=========>>> 2. Untuk menggunakan fitur PHONE LOCK")
    print("=========>>> 3. Untuk menggunakan fitur REMINDER")
    print("=========>>> 4. EXIT")
    print("======================================================")
    fitur = int(input("Pilih ingin menggunakan fitur apa = "))
    if fitur == 1 :
        def ehe(end_time):
            global is_locked
            while is_locked:
                current_time = datetime.now()
                if current_time >= end_time:
                    pygame.mixer.init()
                    pygame.mixer.music.load("Suara Kuntilanak Tertawa.mp3")
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():
                        pygame.time.Clock().tick(10)
                    print("-----------App lock telah terbuka-----------")
                    print("-----------Masukkan aktivitas yang ingin anda lakukan-----------")
                    print("----------->>> 1. Ingin mengedit waktu lock aplikasi <<<-----------")
                    print("----------->>> 2. Ingin mengedit aplikasi yang terlock <<<-----------")
                    print("----------->>> 3. Ingin mengedit aplikasi dan waktu lock <<<-----------")
                    print("----------->>> 4. Hapus Aplikasi dan waktu yang telah dimasukkan <<<-----------")
                    print("----------->>> 5. EXIT <<<-----------")
                    print("Masukkan angka untuk memilih aktivitas : ")
                    
                    is_locked = False  # Unlock the app
                    
        def lock_app(end_time):
            global is_locked
            is_locked = True  # Lock the app
            threading.Thread(target=ehe, args=(end_time,)).start()  
    
        print("==--Selamat datang pada fitur App Lock--==")
        print("==:)Masukkan aplikasi yang ingin dilock(:==")
        app = []
        mulai = []
        akhir = []
        p = []
        while True :
            print("============================================================================")
            print("-----------=== Silakan memilih kegiatan yang ingin anda lakukan ===-----------")
            print("----------->>> 1. Ingin menambah app yang ingin dilock <<<-----------")
            print("----------->>> 2. Mengatur lock aplikasi yang ingin di On <<<-----------")
            print("----------->>> 3. Edit waktu, aplikasi dan hapus lock App <<<-----------")
            print("----------->>> 4. status aplikasi <<<-----------")
            print("----------->>> 5. Exit <<<-----------")
            print("============================================================================")
            a = int(input("[----------Masukkan angka untuk memilih aktivitas----------]= "))
            if a == 1 :
                print("=========== Penambahan aplikasi dapat dilakukan 1 per 1 ===========")
                print("=========== Masukkan nama dan berapa jam aplikasi akan terlock ===========")
                nama = input(f"/========== Masukkan nama aplikasi yang ingin ditambahkan ==========\ = ")
                current_time = datetime.now()
                start_time_str = input("=========== Masukkan jam dan menit mulai (format: HH:MM): ")
                start_hours, start_minutes = map(int, start_time_str.split(':'))
                start_time = datetime.now().replace(hour=start_hours, minute=start_minutes, second=0, microsecond=0)
                end_time_str = input("=========== Masukkan jam dan menit berakhir (format: HH:MM): ")
                end_hours, end_minutes = map(int, end_time_str.split(':'))
                end_time = datetime.now().replace(hour=end_hours, minute=end_minutes, second=0, microsecond=0)
                mulai.append(start_time)
                app.append(nama)
                akhir.append(end_time)
                print(app)
                print(mulai)
                print(akhir)
                print("<Lock App masih off jika ingin meng-on dapat menggunakan fitur kedua>")
            elif a == 2:
                print("============================================================================")
                print("Pilih urutan aplikasi yang ingin di-on")
                urutan = int(input("Urutan App Lock yang ingin di-on = "))
                print("============================================================================")
                
                end_time = akhir[urutan - 1]

                # while True:
                #     current_time = datetime.now()
                #     print(current_time)
                #     time.sleep(5)
                #     print("App masih terlock")

                #     if current_time >= end_time:
                #         psong = AudioSegment.from_mp3("Suara Kuntilanak Tertawa.mp3")
                #         play(psong)
                #         print("App lock telah terbuka")
                #         break 
                tutu = akhir[urutan - 1]
                lock_app(tutu)
                    
            elif a == 3 :
                titik3 = input("Ingin lanjut atau tidak (y/n) : ")
                if titik3 == "y" :
                    print("--------------------------------------------------")
                    print("----Masukkan aktivitas yang ingin anda lakukan----")
                    print("1. Ingin mengedit waktu lock aplikasi")
                    print("2. Ingin mengedit aplikasi yang terlock")
                    print("3. Ingin mengedit aplikasi dan waktu lock")
                    print("4. Hapus Aplikasi dan waktu yang telah dimasukkan")
                    print("5. EXIT")
                    print("--------------------------------------------------")
                    while True :
                        print("---------------------------------------")
                        pilih = int(input("Pilih aktivitas anda = "))
                        if pilih == 1 :
                            print("-----------------------------------------------------------------")
                            print("Masukkan urutan aplikasi yang ingin diedit waktu lock aplikasinya")
                            print("Note :")
                            print("Jika urutan aplikasi tidak ada maka akan terjadi error")
                            urutan = int(input("Masukkan urutan aplikasi ke berapa yang ingin di edit = "))
                            print(f"aplikasi yang akan terlock {app[urutan-1]}")
                            print(f"akan dilock pada {mulai[urutan-1]}")
                            print(f"akan terunlock pada {akhir[urutan-1]}")
                            ganti1 = input("Masukkan jam dan menit mulai (format: HH:MM): ")
                            jamulai, memulai = map(int, ganti1.split(':'))
                            gantimulai = datetime.now().replace(hour=jamulai, minute=memulai, second=0, microsecond=0)
                            ganti2 = input("Masukkan jam dan menit berakhir (format: HH:MM): ")
                            jamakhir, meakhir = map(int, ganti2.split(':'))
                            gantiakhir = datetime.now().replace(hour=jamakhir, minute=meakhir, second=0, microsecond=0)
                            el = urutan-1
                            mulai[el]=gantimulai
                            akhir[el]=gantiakhir
                            print(app)
                            print(mulai)
                            print(akhir)
                            print("-----------------------------------------------------------------")
                            break
                        elif pilih == 2 :
                            print("===========================================")
                            print("Mengganti aplikasi yang terlock saat ini")
                            print("Tidak akan mengubah waktunya")
                            urutan = int(input("Masukkan urutan aplikasi ke berapa yang ingin di ganti = "))
                            print(f"{app[urutan-1]}")
                            print(f"{mulai[urutan-1]}")
                            print(f"{akhir[urutan-1]}")
                            ganti = (input("Ganti aplikasi yang terlock = "))
                            el = urutan-1
                            app[el]=ganti
                            print(app)
                            print(mulai)
                            print(akhir)
                            print("===========================================")
                            break
                        elif pilih == 3 :
                            print("=======================================================================")
                            print("      ===========================================================      ")
                            urutan = int(input("Masukkan urutan aplikasi ke berapa yang ingin di edit = "))
                            print(f"aplikasi yang akan terlock {app[urutan-1]}")
                            print(f"akan dilock pada {mulai[urutan-1]}")
                            print(f"akan terunlock pada {akhir[urutan-1]}")
                            ganti = (input("Ganti aplikasi yang terlock = "))
                            el = urutan-1
                            ganti1 = input("Masukkan jam dan menit mulai (format: HH:MM): ")
                            jamulai, memulai = map(int, ganti1.split(':'))
                            gantimulai = datetime.now().replace(hour=jamulai, minute=memulai, second=0, microsecond=0)
                            ganti2 = input("Masukkan jam dan menit berakhir (format: HH:MM): ")
                            jamakhir, meakhir = map(int, ganti2.split(':'))
                            gantiakhir = datetime.now().replace(hour=jamakhir, minute=meakhir, second=0, microsecond=0)
                            el = urutan-1
                            app[el]=ganti
                            mulai[el]=gantimulai
                            akhir[el]=gantiakhir
                            print(app)
                            print(mulai)
                            print(akhir)
                            print("      ===========================================================      ")
                            print("=======================================================================")
                            break
                        elif pilih == 4 :
                            print("=======================================================================")
                            print("      ===========================================================      ")
                            print("           =================================================           ")
                            print("Masukkan urutan aplikasi ke berapa yang ingin dihapus")
                            print(app)
                            print(mulai)
                            print(akhir)
                            print("Aplikasi yang dihapus juga akan dihapus untuk pengaturan waktunya")
                            urutan = int(input("Masukkan urutan aplikasi ke berapa yang ingin di hapus = "))
                            el = urutan-1
                            app.pop(el)
                            mulai.pop(el)
                            akhir.pop(el)
                            print(app)
                            print(mulai)
                            print(akhir)
                            print("           =================================================           ")
                            print("      ===========================================================      ")
                            print("=======================================================================")
                            break
                        elif pilih == 5 :
                            print("Keluar")
                            break
                elif titik3 == "n" :
                    print("Keluar")
            elif a == 4 :
                print("[][][][][][][][][][][][][][][][][][][][][][][]]")
                print("Aplikasi yang bisa di edit saat ini")
                print(app)
                print(mulai)
                print(akhir)
                print("[][][][][][][][][][][][][][][][][][][][][][][]]")
            elif a == 5 :
                print("Exit")
                print("Terima kasih telah menggunakkan aplikasi kami")
                break
            else :
                print("Tidak Valid")
    elif fitur == 2 :
        print("Selamat datang pada fitur PHONE LOCK")
        
        current_time = time.strftime("%H:%M")
        locks_array = []
        
        class Lock:
            def __init__(self, label, time):
                self.label = label
                self.time = time

        def display_locks(locks):
            if not locks:
                print("Tidak ada phone lock.")
            else:
                for lock in locks:
                    print("Label:", lock.label)
                    print("Time:", lock.time)
                    print("---------------")

        def add_lock(locks):
            label = input("Label phone lock: ")
            time = input("Masukkan waktu (HH:MM): ")
        
            new_lock = Lock(label, time)
            locks.append(new_lock)
            print("Phonelock berhasil ditambahkan")
            
        def nyala_lock(locks):
            pilih = input("Masukkkan judul phonelock yang ingin diaktifkan: ")
            for lock in locks:
                if pilih == lock.label:
                    while True:
                        current_time = time.strftime("%H:%M")
                        for lock in locks_array:
                            if current_time == lock.time:
                                for q in range (3):
                                    sua = AudioSegment.from_mp3("explosion_01-6225.mp3")
                                    play(sua)
                                print(f"!!!  PHONE UNLOCKED: {lock.label}  !!!")
                    
                        time.sleep(1)
                        if current_time > lock.time:
                            break
            else:
                print("Judul phonelock yang anda masukkan tidak terdeteksi dalam sistem")

        def delete_lock(locks):
            if not locks_array:
                print("Phone Ampun Fij")
            else:
                for lock in locks:
                    print("Daftar phonelock:")
                    for idx, lock in enumerate(locks_array, start=1):
                        print(f"{idx}. {lock.label} - {lock.time}")

                    hapus = int(input("Masukkan angka phone lock yang ingin dihapus: "))
                    if 1 <= hapus <= len(locks_array):
                        del locks_array[hapus - 1]
                        print("Phone lock berhasil dihapus")
                else:
                    print("Angka yang diinput tidak ada")
                    
        def edit_lock(locks):
            if not locks:
                print("Phone lock tidak ada dalam sistem")
            else:
                for idx, lock in enumerate(locks_array, start=1):
                    print(f"{idx}. {lock.label} - {lock.time}")
                edit_idx = int(input("Masukkan angka phone lock yang ingin diedit: "))
                if 1 <= edit_idx <= len(locks):
                    lock_to_edit = locks[edit_idx - 1]
                    new_label = input("Masukkan label baru: ")
                    new_time = input("Masukkan waktu baru (HH:MM): ")
                    lock_to_edit.label = new_label
                    lock_to_edit.time = new_time
                    print("Phonelock berhasil diedit")
                else:
                    print("Angka yang diinput tidak ada")

        while True:
            print("======PHONE LOCK======")
            print(f"     --- {current_time} ---")
            print("1. Tampilkan phone lock")
            print("2. Buat phone lock baru")
            print("3. Aktifkan phone lock")
            print("4. Hapus phone lock")
            print("5. Edit phone lock")
            print("6. Keluar")

            choice = input("Pilih opsi (1/2/3/4/5): ")

            if choice == "1":
                display_locks(locks_array)
            elif choice == "2":
                add_lock(locks_array)
            elif choice == "3":
                nyala_lock(locks_array)
            elif choice == "4":
                delete_lock(locks_array)
            elif choice == "5":
                edit_lock(locks_array)
            elif choice == "6":
                print("Berhasil keluar!")
                print("TERIMA KASIH")
                break
            else:
                print("Opsi tidak valid. Silakan pilih 1, 2, atau 3.")



    elif fitur == 3 :
        reminders_list = []
        reminders_active = False

        def check_reminders():
            while reminders_active:
                current_time = time.strftime('%H:%M', time.localtime())

                for reminder in reminders_list:
                    title, reminder_time = reminder
                    if current_time == reminder_time:
                        print(f"\nRemind! {title} at {reminder_time}")
                        # for i in range(1):
                        ra = AudioSegment.from_mp3("big-impact-7054.mp3")
                        play(ra)
                        if current_time > reminder_time:
                            break

                time.sleep(1)
            

        while True:
            print("\n====== Reminder ======")
            print("1. Add Reminder")
            print("2. Show Reminder List")
            print("3. Toggle Reminders (On/Off)")
            print("4. Edit Reminder Time")
            print("5. Delete Reminder")
            print("6. Exit")

            choice = input("Enter your choice (1/2/3/4/5/6): ")

            if choice == '1':
                title = input("Enter reminder title: ")
                reminder_time = input("Set the alarm time (format HH:MM): ")

                try:
                    time.strptime(reminder_time, '%H:%M')
                    reminders_list.append((title, reminder_time))
                except ValueError:
                    print("Invalid time format. Please use HH:MM.")

                print("\nReminder Set:")
                print("\nCurrent Reminders:")
                if not reminders_list:
                    print("No reminders.")
                else:
                    for idx, reminder in enumerate(reminders_list, start=1):
                        title, reminder_time = reminder
                        print(f"{idx}. {title} - {reminder_time}")

            elif choice == '2':
                print("\nCurrent Reminders:")
                if not reminders_list:
                    print("No reminders.")
                else:
                    for idx, reminder in enumerate(reminders_list, start=1):
                        title, reminder_time = reminder
                        print(f"{idx}. {title} - {reminder_time}")

            elif choice == '3':
                reminders_active = not reminders_active
                print(f"Reminders are {'On' if reminders_active else 'Off'}.")
                if reminders_active:
                    threading.Thread(target=check_reminders).start()

            elif choice == '4':
                print("\nCurrent Reminders:")
                if not reminders_list:
                    print("No reminders.")
                else:
                    for idx, reminder in enumerate(reminders_list, start=1):
                        title, reminder_time = reminder
                        print(f"{idx}. {title} - {reminder_time}")

                    edit_choice = int(input("Enter the number of the reminder to edit: "))
                    if 1 <= edit_choice <= len(reminders_list):
                        new_time = input("Enter the new reminder time (format HH:MM): ")
                        try:
                            time.strptime(new_time, '%H:%M')
                            reminders_list[edit_choice - 1] = (reminders_list[edit_choice - 1][0], new_time)
                            print("Reminder time edited successfully.")
                        except ValueError:
                            print("Invalid time format. Please use HH:MM.")
                    else:
                        print("Invalid choice. No reminder edited.")

            elif choice == '5':
                print("\nCurrent Reminders:")
                if not reminders_list:
                    print("No reminders.")
                else:
                    for idx, reminder in enumerate(reminders_list, start=1):
                        title, reminder_time = reminder
                        print(f"{idx}. {title} - {reminder_time}")

                    delete_choice = int(input("Enter the number of the reminder to delete: "))
                    if 1 <= delete_choice <= len(reminders_list):
                        del reminders_list[delete_choice - 1]
                        print("Reminder deleted successfully.")
                    else:
                        print("Invalid choice. No reminder deleted.")

            elif choice == '6':
                print("Exiting program. Goodbye!")
                reminders_active = False
                break

            else:
                print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")

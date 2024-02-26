# todo_app.py

class TodoItem:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def mark_item_as_completed(self, title):
        for item in self.items:
            if item.title == title:
                item.mark_as_completed()
                return True
        return False

    def get_completed_items(self):
        return [item for item in self.items if item.completed]

    def get_incomplete_items(self):
        return [item for item in self.items if not item.completed]

if __name__ == "__main__":
    todo_list = TodoList()

    while True:
        print("\nMenu:")
        print("1. Tambah Tugas")
        print("2. Tandai Tugas Selesai")
        print("3. Lihat Tugas Yang Belum Selesai")
        print("4. Lihat Tugas Yang Sudah Selesai")
        print("5. Keluar")

        choice = input("Pilih menu (1/2/3/4/5): ")

        if choice == "1":
            title = input("Masukkan judul tugas: ")
            description = input("Masukkan deskripsi tugas: ")
            todo_item = TodoItem(title, description)
            todo_list.add_item(todo_item)
            print("Tugas berhasil ditambahkan.")

        elif choice == "2":
            title = input("Masukkan judul tugas yang selesai: ")
            if todo_list.mark_item_as_completed(title):
                print("Tugas berhasil ditandai sebagai selesai.")
            else:
                print("Tugas tidak ditemukan.")

        elif choice == "3":
            print("Tugas yang belum selesai:")
            incomplete_items = todo_list.get_incomplete_items()
            for idx, item in enumerate(incomplete_items, start=1):
                print(f"{idx}. {item.title} - {item.description}")

        elif choice == "4":
            print("Tugas yang sudah selesai:")
            completed_items = todo_list.get_completed_items()
            for idx, item in enumerate(completed_items, start=1):
                print(f"{idx}. {item.title} - {item.description}")

        elif choice == "5":
            print("Terima kasih, sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")
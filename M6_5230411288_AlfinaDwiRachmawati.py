class Delivery:
    def __init__(self, id, name, information, date, address):
        self._id = id
        self.name = name
        self.information = information
        self.date = date
        self.address = address

    def process_delivery(self):
        print(f"Processing delivery ID {self._id} for {self.name} on {self.date} to {self.address}")


class Order:
    def __init__(self, ID, name, details):
        self._ID = ID
        self.name = name
        self.details = details
        self.deliveries = []

    def set_order(self, delivery):
        if isinstance(delivery, Delivery):
            self.deliveries.append(delivery)

    def get_order_details(self):
        print(f"Order ID: {self._ID}, Name:          {self.name}, Details: {self.details}")
        for delivery in self.deliveries:
            print(f" - Delivery ID: {delivery._id}, Date: {delivery.date}, Address: {delivery.address}")


def main_menu():
    orders = {}
    while True:
        print("\nMenu Utama:")
        print("1. Tambah Order")
        print("2. Tambah Delivery ke Order")
        print("3. Lihat Detail Order")
        print("4. Proses Semua Delivery dalam Order")
        print("5. Keluar")


        pilihan = input("Pilih Menu: ")

        if pilihan == "1":
            order_id = int(input("Masukkan ID Order: "))
            name = input("Masukkan Nama Order: ")
            details = input("Masukkan Detail Order: ")
            orders[order_id] = Order(order_id, name, details)
            print("Order berhasil ditambahkan.")

        elif pilihan == "2":
            order_id = int(input("Masukkan ID Order untuk menambah Delivery: "))
            if order_id in orders:
                delivery_id = int(input("Masukkan ID Delivery: "))
                name = input("Masukkan Nama Pengiriman: ")
                information = input("Masukkan Informasi Pengiriman: ")
                date = input("Masukkan Tanggal Pengiriman: ")
                address = input("Masukkan Alamat Pengiriman: ")
                delivery = Delivery(delivery_id, name, information, date, address)
                orders[order_id].set_order(delivery)
                print("Delivery berhasil ditambahkan ke Order.")
            else:
                print("Order dengan ID tersebut tidak ditemukan.")

        elif pilihan == "3":
            order_id = int(input("Masukkan ID Order untuk melihat detail: "))
            if order_id in orders:
                orders[order_id].get_order_details()
            else:
                print("Order dengan ID tersebut tidak ditemukan.")

        elif pilihan == "4":
            order_id = int(input("Masukkan ID Order untuk memproses semua Delivery: "))
            if order_id in orders:
                for delivery in orders[order_id].deliveries:
                    delivery.process_delivery()
            else:
                print("Order dengan ID tersebut tidak ditemukan.")

        elif pilihan == "5":
            print("Keluar dari program.")
            break
        else:
            print("Opsi tidak valid. Silakan pilih lagi.")

main_menu()

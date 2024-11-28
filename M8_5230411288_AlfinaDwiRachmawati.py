import tkinter as tk
from tkinter import ttk, messagebox

buku_data = {
    "Fiksi": [
        {"judul": "Pulang", "penulis": "Leila S. Chudori", "tahun": 2012, "rating": 4.5},
        {"judul": "Perahu Kertas", "penulis": "Dee Lestari", "tahun": 2009, "rating": 4.2},
        {"judul": "Laskar Pelangi", "penulis": "Andrea Hirata", "tahun": 2005, "rating": 4.8},
        {"judul": "Sang Pemimpi", "penulis": "Andrea Hirata", "tahun": 2006, "rating": 4.6},
        {"judul": "Bumi Manusia", "penulis": "Pramoedya Ananta Toer", "tahun": 1980, "rating": 4.7},
        {"judul": "Tetralogi Buru", "penulis": "Pramoedya Ananta Toer", "tahun": 1980, "rating": 4.8},
        {"judul": "Filosofi Kopi", "penulis": "Dee Lestari", "tahun": 1996, "rating": 4.4},
        {"judul": "Supernova", "penulis": "Dee Lestari", "tahun": 2001, "rating": 4.5},
        {"judul": "Hujan", "penulis": "Tere Liye", "tahun": 2016, "rating": 4.5},
        {"judul": "Bulan", "penulis": "Tere Liye", "tahun": 2017, "rating": 4.6}
    ],
    "Fantasi": [
        {"judul": "Harry Potter", "penulis": "J.K. Rowling", "tahun": 1997, "rating": 4.8},
        {"judul": "The Hobbit", "penulis": "J.R.R. Tolkien", "tahun": 1937, "rating": 4.7},
        {"judul": "The Lord of the Rings", "penulis": "J.R.R. Tolkien", "tahun": 1954, "rating": 4.9},
        {"judul": "Eragon", "penulis": "Christopher Paolini", "tahun": 2002, "rating": 4.6},
        {"judul": "Percy Jackson", "penulis": "Rick Riordan", "tahun": 2005, "rating": 4.7},
        {"judul": "Chronicles of Narnia", "penulis": "C.S. Lewis", "tahun": 1950, "rating": 4.8},
        {"judul": "Mistborn", "penulis": "Brandon Sanderson", "tahun": 2006, "rating": 4.7},
        {"judul": "The Name of the Wind", "penulis": "Patrick Rothfuss", "tahun": 2007, "rating": 4.8},
        {"judul": "His Dark Materials", "penulis": "Philip Pullman", "tahun": 1995, "rating": 4.5},
        {"judul": "The Wheel of Time", "penulis": "Robert Jordan", "tahun": 1990, "rating": 4.6}
    ],
    "Horor": [
        {"judul": "Goosebumps", "penulis": "R.L. Stine", "tahun": 1992, "rating": 4.3},
        {"judul": "It", "penulis": "Stephen King", "tahun": 1986, "rating": 4.6},
        {"judul": "Pet Sematary", "penulis": "Stephen King", "tahun": 1983, "rating": 4.4},
        {"judul": "The Shining", "penulis": "Stephen King", "tahun": 1977, "rating": 4.8},
        {"judul": "Dracula", "penulis": "Bram Stoker", "tahun": 1897, "rating": 4.7},
        {"judul": "Frankenstein", "penulis": "Mary Shelley", "tahun": 1818, "rating": 4.5},
        {"judul": "The Haunting of Hill House", "penulis": "Shirley Jackson", "tahun": 1959, "rating": 4.4},
        {"judul": "Bird Box", "penulis": "Josh Malerman", "tahun": 2014, "rating": 4.3},
        {"judul": "Coraline", "penulis": "Neil Gaiman", "tahun": 2002, "rating": 4.7},
        {"judul": "The Exorcist", "penulis": "William Peter Blatty", "tahun": 1971, "rating": 4.6}
    ],
    "Misteri": [
        {"judul": "Sherlock Holmes", "penulis": "Arthur Conan Doyle", "tahun": 1887, "rating": 4.9},
        {"judul": "The Girl with the Dragon Tattoo", "penulis": "Stieg Larsson", "tahun": 2005, "rating": 4.7},
        {"judul": "Gone Girl", "penulis": "Gillian Flynn", "tahun": 2012, "rating": 4.6},
        {"judul": "Big Little Lies", "penulis": "Liane Moriarty", "tahun": 2014, "rating": 4.5},
        {"judul": "The Silent Patient", "penulis": "Alex Michaelides", "tahun": 2019, "rating": 4.6}
    ],
    "Petualangan": [
        {"judul": "The Adventures of Tom Sawyer", "penulis": "Mark Twain", "tahun": 1876, "rating": 4.5},
        {"judul": "The Call of the Wild", "penulis": "Jack London", "tahun": 1903, "rating": 4.7},
        {"judul": "Into the Wild", "penulis": "Jon Krakauer", "tahun": 1996, "rating": 4.6},
        {"judul": "The Lost City of Z", "penulis": "David Grann", "tahun": 2009, "rating": 4.5},
        {"judul": "Life of Pi", "penulis": "Yann Martel", "tahun": 2001, "rating": 4.7}
    ],
    "Komedi": [
        {"judul": "The Hitchhiker's Guide to the Galaxy", "penulis": "Douglas Adams", "tahun": 1979, "rating": 4.8},
        {"judul": "Good Omens", "penulis": "Neil Gaiman & Terry Pratchett", "tahun": 1990, "rating": 4.7},
        {"judul": "Catch-22", "penulis": "Joseph Heller", "tahun": 1961, "rating": 4.6},
        {"judul": "A Confederacy of Dunces", "penulis": "John Kennedy Toole", "tahun": 1980, "rating": 4.5},
        {"judul": "The Importance of Being Earnest", "penulis": "Oscar Wilde", "tahun": 1895, "rating": 4.6}
    ]
}


def cari_buku():
    genre = genre_var.get()
    if not genre:
        messagebox.showerror("Error", "Pilih genre terlebih dahulu!")
        return
    
    listbox_buku.delete(0, tk.END) 
    
    buku_genre = buku_data.get(genre, [])
    if not buku_genre:
        listbox_buku.insert(tk.END, "Tidak ada buku untuk genre ini.")
    else:
        for buku in buku_genre:
            listbox_buku.insert(tk.END, buku["judul"])


def detail_buku(event):
    try:
        selected_index = listbox_buku.curselection()[0]
        selected_genre = genre_var.get()
        selected_buku = buku_data[selected_genre][selected_index]
        
        detail = (
            f"Judul: {selected_buku['judul']}\n"
            f"Penulis: {selected_buku['penulis']}\n"
            f"Tahun: {selected_buku['tahun']}\n"
            f"Rating: {selected_buku['rating']}/5"
        )
        messagebox.showinfo("Detail Buku", detail)
    except IndexError:
        messagebox.showerror("Error", "Pilih buku dari daftar untuk melihat detail!")

root = tk.Tk()
root.title("Rekomendasi Buku Berdasarkan Genre")
root.geometry("400x500")

tk.Label(root, text="Pilih Genre:", font=("Arial", 12)).pack(pady=10)
genre_var = tk.StringVar()
genre_dropdown = ttk.Combobox(root, textvariable=genre_var, state="readonly", font=("Arial", 10))
genre_dropdown['values'] = list(buku_data.keys())
genre_dropdown.pack(pady=5)

btn_cari = tk.Button(root, text="Cari Buku", command=cari_buku, font=("Arial", 10))
btn_cari.pack(pady=10)

tk.Label(root, text="Daftar Buku:", font=("Arial", 12)).pack(pady=10)
listbox_buku = tk.Listbox(root, font=("Arial", 10), width=50, height=15)
listbox_buku.pack(pady=10)
listbox_buku.bind("<<ListboxSelect>>", detail_buku)

tk.Label(root, text="Klik pada buku untuk melihat detailnya.", font=("Arial", 10), fg="gray").pack(pady=5)

root.mainloop()

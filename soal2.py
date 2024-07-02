class Solve:
    def __init__(self):
        self.n = int(input())
        self.a = list(input())
        self.b = list(input())

        print(self.get_min_operations())

    def get_min_operations(self):
        segments = 0
        i = 0

        while i < self.n:
            if self.a[i] > self.b[i]:
                segments += 1
                start = i
                while i < self.n and self.a[i] > self.b[i]:
                    i += 1
                end = i
                self.a[start:end], self.b[start:end] = self.b[start:end], self.a[start:end]
            else:
                i += 1
        return segments


if __name__ == "__main__":
    Solve()


'''
Algoritma.
1.  Mulai
2.  Inisialisasi variabel n, a, b dan jadikan variabel penerima input dengan ketentuan:
    n : diconversi ke tipe data number
    a : diconversi menjadi list
    b : diconversi menjadi list
3.  Panggil fungsi `get_min_operations` yang mana didalamnya melakukan hal sebagai berikut:
    1.  Inisialisasi variabel `segments` dan `i` serta atur nilai default 0
    2.  Lakukan perulangan menggunakan while untuk ketentuan (i < n)
    3.  Lakukan pengkondisian jika a[i] > b[i] maka lakukan langkah dibawah ini:
          1.  Increment variabel `segments`
          2.  Inisialisasi variabel `start` dengan nilai `i`
          3.  Lakukan pengulangan dengan syarat (i < n and a[i] > b[i]) kemudian increment variabel `i`
          4.  Inisialisasi variabel `end` dan atur nilainya dengan `i`
          5.  Tukar variabel `a` dan `b` dengan slicing menggunakan `start` sampai `end`
    4.  Jila salah maka hanya increment variabel `i`
    5.  Kembalikan variabel `segments`
4.  Selesai

O(N)
'''

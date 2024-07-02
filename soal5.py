class Solve:
    def __init__(self):
        n = int(input())
        v = list(map(int, input().split()))[:n]
        self.memo = {}
        print(self.maximum_pleasure(v))

    def maximum_pleasure(self, v, start=None):
        if start is None:
            a = self.maximum_pleasure(v, 0)
            b = self.maximum_pleasure(v, 1)
            return max(a, b)
        else:
            if start in self.memo:
                return self.memo[start]
            result = 0
            try:
                result = v[start] + self.maximum_pleasure(v, start + 2)
                self.memo[start] = result
            except:
                pass
            return result


if __name__ == "__main__":
    Solve()


'''
Algoritma.
1.  Mulia
2.  Inisialisasi variabel `n` dan `v` sebagai inputan
3.  Inisialisasi `memo` sebagai dictionary yang akan digunakan sebagai memorize
4.  Panggil fungsi `maximum_pleasure` dan fungsi ini memiliki dua argumen yaitu `v` sebagai list number
    dan `start` sebagai start index kemudian didalam fungsi menjalankan beberapa langkah sebagai berikut:
    1.  Lakukan pengecekan jika `start` sama dengan None maka dilakukan beberapa langkah berikut:
        1.  Inisialisasi variabel `a` dengan nilai nya memanggil fungsi dirinya sendiri dengan start nya adalah 0
        2.  Inisialisasi variabel `b` dengan nilai nya memanggil fungsi dirinya sendiri dengan start nya adalah 1
        3.  Return max dari `a` dan `b`
    2.  Jila salah maka lakukan beberapa langkah dibawah ini:
        1.  Jika `start` ada didalam `memo` maka return langsung `memo` dengan index `start`
        2.  Inisialisasi variabel `result` dengan default nilai 0
        3.  Lakukan try except ketikga except maka langsung pass saja
        4.  Perbarui variabel `result` dengan `v[start]` ditambah `maximum_pleasure(v, start + 2)`
        5.  Tambahkan `memo[start]` dengan `result`
        6.  Return result
5.  Selesai.


O(N)
'''

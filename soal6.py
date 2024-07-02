import sys


class Solve:
    def __init__(self) -> None:
        self.n = int(input())
        self.p = list(map(int, input().split()))[:self.n + 1]
        self.memo = [[-1 for _ in range(self.n + 1)]
                     for _ in range(self.n + 1)]
        print(self.matrix_chain_order())

    def matrix_chain_order(self):
        n = len(self.p) - 1
        m = [[0 for _ in range(n)]
             for _ in range(n)]

        for i in range(2, n + 1):
            for j in range(n - i + 1):
                k = j + i - 1
                m[j][k] = sys.maxsize
                for l in range(j, k):
                    q = m[j][l] + m[l+1][k] + self.p[j] * \
                        self.p[l+1] * self.p[k+1]
                    if q < m[j][k]:
                        m[j][k] = q

        return m[0][n-1]


if __name__ == "__main__":
    Solve()


'''
Algoritma:
1.  Inisialisasi variabel `n` dengan set sebagai inputan lalu di convert ke number
2.  Inisialisasi variabel `p` dengan set sebagai inputan lalu di convert ke list number
3.  Inisialisasi variabel `memo` dengan nilai matrix berordo (n + 1 X n + 1) lalu default elementnya
    yaitu -1
4.  Cetak hasil dari fungsi `matrix_chain_order` didalam fungsi ini menjalankan beberapa langkah berikut:
    1.  Inisialisasi variabel `n` dengan `len(p) - 1`
    2.  Inisialisasi variabel `m` dengan matrix berordo (n X n) dengan default nilai 0
    3.  Lakukan perulagnan ditampung dalam variabel `i` dengan `range(2, n + 1)`
    4.  Lakukan perulangan lagi ditampung dalam variabel `j` dengan `range(n - 1 + 1)`
    5.  Inisialisasi variabel `k` dengan nilai `j + i - 1`
    6.  Lakukan perulangan sebanyak `range(j, k)` lalu ditampung dalam variabel l
    7.  Inisialisasi variabel `q` dengan nilai `m[j][l] + m[l+1][k] + self.p[j] * \ self.p[l+1] * self.p[k+1]`
    8.  Jika `q` lebih kecil dari `m[j][k]` maka perbarui nilai `m[j][k]` dengan `q`
    9.  Return `m[0][n-1]`
5.  Selesai.

O(N ^ 3)
'''

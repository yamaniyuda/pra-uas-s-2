class Solve:
    def __init__(self):
        self.n = int(input())
        self.orders = []

        for _ in range(self.n):
            c, p, t, d = input().split()
            self.orders.append(
                (c, int(p), int(t) + int(d))
            )

        self.orders.sort(key=lambda x: (x[2], -x[1]))
        self.max_order()

    def max_order(self):
        profit = 0
        job_orders = self.orders

        try:
            for i in range(len(job_orders)):
                for j in range(i + 1, len(job_orders) - 1):
                    if job_orders[i][2] == job_orders[j][2]:

                        # pop melakukan iterasi didalamnya
                        job_orders.pop(
                            j if job_orders[i][1] >= job_orders[j][1] else i
                        )

                profit += job_orders[i][1]
        except:
            pass
        

        print(" ".join(item[0] for item in job_orders))
        print(profit)


if __name__ == "__main__":
    Solve()


'''
Algoritma:
1.  Mulai  
2.  Inisialisasi `n` dengan set sebagai inputan lalu di conversi ke number
3.  Inisialisasi `orders` dengan default value sebagai []
4.  Lakukan perulangan dengan `range(n)`
5.  Split nilai inputan dan masukan ke dalam variabel `c`, `p`, `t`, dan `d`
6.  Lalu tambahkan kedalam `orders` dengan nilai list sebagai berikut `(c, int(p), int(t) + int(d))`
7.  Lakukan sort pada order berdasarakan element ke 2 dari lalu urutkan berdasarkan yang terbesar  dari element ke - 1
8.  Panggil fungsi `max_order` dan didalamnya melakukan beberapa proses sebagai berikut:
    1.  Inisialisasi variabel `profit` dengan default 0
    2.  Inisialisasi variabel `job_orders` dengan nilai orders
    3.  Lalukan try except yang mana except akan memanggil pas saja
    4.  Lakukan perulangan dengan `range(len(job_orders))` lalu di tampung kedalam variabel `i`
    5.  Lakukan perulangan dengan `range(i + 1, len(job_orders) - 1)` lalu di tampung kedalam variabel `j`
    6.  Lakukan pengecekan `job_orders[i][2] == job_orders[j][2]` jika benar maka pop nilai dengan ketentuan `j if job_orders[i][1] >= job_orders[j][1] else i`
    7.  Perbarui variabel `profit` dengan `ob_orders[i][1]`
    8.  Print element ke 0 dari setiap element dari job_orders
    9.  Lalu tampilkan profit
9.  Selesa

O(n^3)
'''
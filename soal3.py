class Solve:
    def __init__(self):
        n = int(input())
        self.graph = dict()

        for _ in range(n):
            key = input()
            value = sorted(input().split())
            self.graph[key] = value

        self.source = input()
        self.bfs()

    def bfs(self):
        visited = [self.source]
        queue = [self.source]

        while queue:
            vertex = queue.pop(0)

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)

            print(vertex, end=" -> " if queue else None)


if __name__ == "__main__":
    Solve()


'''
Algoritma.
1.  Mulai
2.  Inisialisasi variabel `n` dan set sebagai inputan serta converter menjadi number
3.  Inisialisasi variabel `graph` dan atur nilai defaultnya yaitu dictionary
4.  Lakukan perulangan sebanyak `n` untuk membuat sebuah graph dengan variabel `key` dan `value` sebagai inputan
5.  Inisialisasi `source` dan set sebagai inputan yang akan digunakan sebagai titik awal
6.  Panggil fungsi `bfs` dan didalamnya dilakukan beberapa step sebagai berikut:
    1.  Inisialisasi `visited` dan `queue` dan set nilai default kedunya sebagai array dengan element pertama `source`
    2.  Lakukan perulangan while dengan queue:
        1.  Ambil `vertex` pertama dari `queue`
        2.  Lakukan perulangan dengan tetangga dari `vertex`
        3.  Jika `neighbor` tidak ada di daftar visited maka tambahkan `neighbor` ke `visited` dan `queue`
        4.  Print hasilnya

7.  Selesai 

O(V + E)
'''

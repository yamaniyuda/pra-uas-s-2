import sys
import heapq


class Solve:
    def __init__(self):
        N, M, self.A, self.B = list(map(str, input().split()))

        self.graph = {str(i): {} for i in range(1, int(N) + 1)}

        input_node = []

        for _ in range(int(M)):
            input_node.append(list(map(str, input().split())))

        for node in input_node:
            u, v, w = node[0], node[1], int(node[2])
            self.graph[u][v] = w
            self.graph[v][u] = w  # Make the graph undirected

        paths, min_distance = self.find_shortest_paths(self.A)
        self.print_avg_point(paths, min_distance, self.A, self.B)

    def get_nodes(self):
        return self.graph.keys()

    def get_neighbors(self, node):
        return self.graph[node].keys()

    def find_shortest_paths(self, start_node):
        pq = [(0, start_node, [start_node])]
        min_distance = {node: sys.maxsize for node in self.get_nodes()}
        min_distance[start_node] = 0
        all_paths = {node: [] for node in self.get_nodes()}
        all_paths[start_node] = [[start_node]]

        while pq:
            current_distance, current_node, path = heapq.heappop(pq)

            if current_distance > min_distance[current_node]:
                continue

            for neighbor in self.get_neighbors(current_node):
                distance = current_distance + \
                    self.graph[current_node][neighbor]
                if distance < min_distance[neighbor]:
                    min_distance[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor, path + [neighbor]))
                    all_paths[neighbor] = [path + [neighbor]]
                elif distance == min_distance[neighbor]:
                    all_paths[neighbor].append(path + [neighbor])
                    heapq.heappush(pq, (distance, neighbor, path + [neighbor]))

        return all_paths, min_distance

    def print_avg_point(self, all_paths, min_distance, start_node, target_node):
        if min_distance[target_node] == sys.maxsize:
            print(f"Tidak ada rute dari {start_node} ke {target_node}.")
        else:
            memo = {}

            for i in range(len(all_paths[target_node])):
                for j in range(len(all_paths[target_node][i])):
                    if all_paths[target_node][i][j] in memo:
                        memo[all_paths[target_node][i][j]] += 2
                    else:
                        memo[all_paths[target_node][i][j]] = 2

            for key in memo:
                memo[key] //= len(all_paths[target_node])

            sorted_data = {key: memo[key] for key in sorted(memo)}

            keys = list(sorted_data.keys())
            for i in range(1, int(keys[-1]) + 1):
                try:
                    print(sorted_data[str(i)])
                    # if keys[i] in sorted_data:
                except:
                    print(0)


if __name__ == '__main__':
    Solve()


'''
Algoritma:
1. Mulai
2. Inisialisasi variabel `N`, `M`, `A`, dan `B` dari input sebagai string
3. Inisialisasi variabel `graph` dan atur nilai defaultnya sebagai dictionary dengan key berupa node dan value berupa dictionary kosong
4. Lakukan perulangan sebanyak `M` untuk mendapatkan data edge `u`, `v`, dan `w` dari input
    1. Tambahkan edge ke graph untuk kedua arah (u ke v dan v ke u) dengan bobot `w`
5. Panggil fungsi `find_shortest_paths` dengan parameter `A` sebagai titik awal
    1. Inisialisasi priority queue `pq` dengan elemen (0, A, [A])
    2. Inisialisasi dictionary `min_distance` dengan key berupa node dan value berupa nilai maksimum
    3. Atur `min_distance[A]` ke 0
    4. Inisialisasi dictionary `all_paths` dengan key berupa node dan value berupa list kosong
    5. Atur `all_paths[A]` ke list yang berisi list [A]
    6. Lakukan perulangan while `pq` tidak kosong:
        1. Ambil elemen dengan jarak minimum `current_distance`, `current_node`, dan `path` dari `pq`
        2. Jika `current_distance` lebih besar dari `min_distance[current_node]`, lanjutkan ke iterasi berikutnya
        3. Lakukan perulangan untuk setiap `neighbor` dari `current_node`:
            1. Hitung jarak `distance` sebagai `current_distance` + bobot edge dari `current_node` ke `neighbor`
            2. Jika `distance` lebih kecil dari `min_distance[neighbor]`:
                1. Atur `min_distance[neighbor]` ke `distance`
                2. Tambahkan elemen (distance, neighbor, path + [neighbor]) ke `pq`
                3. Atur `all_paths[neighbor]` ke list yang berisi path + [neighbor]
            3. Jika `distance` sama dengan `min_distance[neighbor]`:
                1. Tambahkan path + [neighbor] ke `all_paths[neighbor]`
                2. Tambahkan elemen (distance, neighbor, path + [neighbor]) ke `pq`
7. Panggil fungsi `print_avg_point` dengan parameter `all_paths`, `min_distance`, `A`, dan `B`
    1. Jika `min_distance[B]` sama dengan nilai maksimum:
        1. Print bahwa tidak ada rute dari `A` ke `B`
    2. Jika tidak:
        1. Inisialisasi dictionary `memo`
        2. Lakukan perulangan untuk setiap jalur di `all_paths[B]`:
            1. Lakukan perulangan untuk setiap node di jalur tersebut:
                1. Tambahkan 2 ke nilai `memo[node]` jika node sudah ada di `memo`
                2. Jika tidak, atur nilai `memo[node]` ke 2
        3. Lakukan perulangan untuk setiap key di `memo`:
            1. Bagi nilai `memo[key]` dengan jumlah jalur di `all_paths[B]`
        4. Urutkan `memo` berdasarkan key
        5. Print setiap nilai dari `memo` yang sudah diurutkan. Jika key tidak ditemukan di `memo`, print 0
8. Selesai

O(V + E log V)
'''

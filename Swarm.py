import random

class DFO():
    def __init__(self, f, bounds, NP, max_evals, dt):
        self.f = f
        self.bounds = bounds
        self.NP = NP
        self.max_evals = max_evals
        self.dt = dt
        """
        Args:
            f: Fungsi objektif yang akan diminimalkan.
            bounds: Batas atas dan bawah untuk setiap dimensi.
            NP: Jumlah lalat dalam populasi.
            max_evals: Jumlah maksimum evaluasi fungsi.
            dt: Parameter ambang batas.
        """
    def calculate_dfo(self):
        # Inisialisasi populasi lalat secara acak
        flies = [[random.uniform(self.bounds[d][0], self.bounds[d][1]) for d in range(len(self.bounds))] for _ in range(self.NP)]
        fitness = [self.f(fly) for fly in flies]  # Hitung fitness awal
        evals = self.NP  # Karena sayasudah menghitung fitness untuk NP lalat

        while evals < self.max_evals:
            print(f"Evaluasi: {evals},  Fitness Terbaik: {min(fitness)}")
            # Menemukan lalat terbaik (sb)
            sb_index = fitness.index(min(fitness))  # Indeks lalat terbaik
            sb = flies[sb_index]  # Lalat terbaik

            # Menemukan tetangga terbaik (nb) untuk setiap lalat
            nb = []
            for i in range(self.NP):
                left = flies[i-1] if i > 0 else flies[-1]  # Tetangga kiri
                right = flies[i+1] if i < self.NP-1 else flies[0]  # Tetangga kanan
                nb.append(min([left, right], key=lambda fly: fitness[flies.index(fly)]))  # Menggunakan fitness untuk menentukan tetangga terbaik

            # Memperbaharui posisi lalat
            for i in range(self.NP):
                for d in range(len(self.bounds)):
                    tau = nb[i][d] + random.uniform(0, 1) * (sb[d] - flies[i][d])
                    if random.random() < self.dt:
                        tau = self.bounds[d][0] + random.random() * (self.bounds[d][1] - self.bounds[d][0])
                    flies[i][d] = tau

                # Menghitung fitness untuk lalat yang diperbaharui
                fitness[i] = self.f(flies[i])  # Update fitness untuk lalat yang diperbaharui
                evals += 1

        # Mengembalikan lalat terbaik setelah semua evaluasi selesai
        best_index = fitness.index(min(fitness))
        return flies[best_index], fitness[best_index]  # Kembalikan posisi dan fitness terbaik


# # Contoh penggunaan
# def sphere(x):
#     return sum([xi**2 for xi in x])

# bounds = [(-5.12, 5.12), (-5.12, 5.12)]

# NP = 20
# max_evals = 1000
# dt = 0.2

# fit = DFO(sphere, bounds, NP, max_evals, dt)
# best_fly = fit.calculate_dfo()

# print(best_fly)

    
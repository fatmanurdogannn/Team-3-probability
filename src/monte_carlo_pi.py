import numpy as np
import matplotlib.pyplot as plt

# 1. Ayarlar: Kaç nokta atacağız? (N ne kadar büyükse sonuç o kadar kesin olur)
n = 10000 

# 2. Rastgele (x, y) noktaları üretme [cite: 80]
# Her iki koordinat da 0 ile 1 arasında (Standart Uniform Dağılım) [cite: 80]
x = np.random.uniform(0, 1, n)
y = np.random.uniform(0, 1, n)

# 3. Noktaların daire içinde olup olmadığını kontrol etme [cite: 81]
# Formül: x^2 + y^2 <= 1 [cite: 81]
uzaklik = x**2 + y**2
icerdeki_noktalar = uzaklik <= 1

# 4. Pi Sayısını Tahmin Etme [cite: 82]
# Formül: 4 * (içerideki nokta sayısı / toplam nokta sayısı) [cite: 82]
pi_tahminleri = 4 * np.cumsum(icerdeki_noktalar) / np.arange(1, n + 1)
son_tahmin = pi_tahminleri[-1]

print(f"Tahmin edilen Pi değeri ({n} nokta ile): {son_tahmin}")

# 5. GRAFİK ÇİZİMİ [cite: 83]
plt.figure(figsize=(10, 6))
plt.plot(pi_tahminleri, label='Monte Carlo Tahmini')
plt.axhline(y=np.pi, color='r', linestyle='--', label=f'Gerçek Pi ({np.pi:.5f})') # Referans çizgisi [cite: 84]

plt.title(f'Monte Carlo Pi Tahmini Yakınsama Grafiği (n={n})')
plt.xlabel('Nokta Sayısı (n)')
plt.ylabel('Pi Tahmini')
plt.legend()
plt.grid(True)

# 6. Grafiği Kaydetme [cite: 91]
# Ödevde istenen klasör yapısına uygun isimle kaydediyoruz
plt.savefig('pi_estimation.png')
plt.show()

# 1protocol-Neuro-Master: Hybrid Neuromorphic Framework

![Neuromorphic](https://img.shields.io/badge/Tech-Neuromorphic-blue)
![Nengo](https://img.shields.io/badge/Theory-NEF-orange)

## 🌌 Proje Hakkında
**1protocol-Neuro-Master**, biyolojik sinir sistemlerinin çalışma prensiplerini modern hesaplama yöntemleriyle birleştiren bir araştırma framework'üdür. **Neural Engineering Framework (NEF)** temelleri üzerine inşa edilmiştir.

### Anahtar Özellikler:
* **Hibrit Mimari:** Nengo (Bilişsel Modelleme) ve Lava (Donanım Soyutlama) entegrasyonu.
* **NEF Prensipleri:** Sinyallerin yüksek doğrulukla spike dizilerine kodlanması ve deşifre edilmesi.
* **Gerçek Zamanlı Analiz:** Spike raster plot ve sinyal takibi.

---

## 🔬 Bilimsel Altyapı
Sistem, **Leaky Integrate-and-Fire (LIF)** nöron modellerini kullanır. Dinamik sistemlerin nöral temsili şu denklemle ifade edilir:

$$\dot{x} = f(x, u)$$

Nöron toplulukları, bu $x$ durumunu temsil eden ağırlıklı sinaptik bağlantıları (Decoders) optimize eder.

---

## 🛠️ Kurulum ve Kullanım

1. **Bağımlılıkları Yükleyin:**
   ```bash
   pip install nengo lava-nc numpy matplotlib
import matplotlib.pyplot as plt

def plot_results(sim, model):
    """Simülasyon sonuçlarını görselleştirir"""
    plt.figure(figsize=(12, 8))
    
    # 1. Grafik: Giriş Sinyali ve Çıktı (Decoded)
    plt.subplot(2, 1, 1)
    plt.title("Giriş Sinyali ve Nöral Temsil (NEF)")
    plt.plot(sim.trange(), sim.data[model.probe_input], 'r', label="Giriş (Stimulus)")
    plt.plot(sim.trange(), sim.data[model.probe_decoded], 'b', label="Nöral Çıktı (Decoded)")
    plt.legend()
    plt.grid(True)

    # 2. Grafik: Spike Aktivitesi (Raster Plot)
    plt.subplot(2, 1, 2)
    plt.title("Nöron Spike Aktivitesi (LIF Neurons)")
    from nengo.utils.matplotlib import rasterplot
    rasterplot(sim.trange(), sim.data[model.probe_neurons])
    plt.xlabel("Zaman (s)")
    plt.ylabel("Nöron İndeksi")

    plt.tight_layout()
    plt.savefig("data/simulation_result.png")
    print("📈 Grafik 'data/simulation_result.png' olarak kaydedildi.")
    plt.show()

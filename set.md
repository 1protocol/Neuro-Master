#!/bin/bash

# Proje İsmi
PROJECT_NAME="1protocol_neuro"

echo "🚀 Nöromorfik Ekosistem İnşa Ediliyor: $PROJECT_NAME"

# 1. Klasör Yapısını Oluştur
mkdir -p $PROJECT_NAME/{core,perception,models,utils,visuals,data}

# ---------------------------------------------------------
# 2. CORE: Lava (Low-level Hardware Interface)
# ---------------------------------------------------------
cat <<EOF > $PROJECT_NAME/core/lava_neuron.py
from lava.magma.core.process.process import AbstractProcess
from lava.magma.core.process.variable import Var
from lava.magma.core.process.ports.ports import InPort, OutPort

class ProtocolOneLava(AbstractProcess):
    """Donanım etkileşimi için temel Lava nöron iskeleti"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        shape = kwargs.get("shape", (1,))
        self.s_in = InPort(shape=shape)
        self.a_out = OutPort(shape=shape)
        self.v = Var(shape=shape, init=0)
        self.vth = Var(shape=shape, init=10)
EOF

# ---------------------------------------------------------
# 3. MODELS: Nengo (NEF Teorik Hesaplama)
# ---------------------------------------------------------
cat <<EOF > $PROJECT_NAME/models/nengo_engine.py
import nengo
import numpy as np

def create_nef_network():
    """Neural Engineering Framework tabanlı sinir ağı"""
    model = nengo.Network(label="1protocol_Nengo_Core")
    with model:
        # Girdi: Sinüs dalgası (Örn: Titreşim veya Görsel Hareket)
        stimulus = nengo.Node(lambda t: np.sin(10 * t))
        
        # Nöron Grubu: 100 LIF Nöronu
        ensemble = nengo.Ensemble(n_neurons=100, dimensions=1, 
                                  neuron_type=nengo.LIF())
        
        # Bağlantılar
        nengo.Connection(stimulus, ensemble)
        
        # Veri toplama noktaları (Probes)
        model.probe_input = nengo.Probe(stimulus)
        model.probe_neurons = nengo.Probe(ensemble.neurons) # Spike'lar
        model.probe_decoded = nengo.Probe(ensemble, synapse=0.01) # Filtrelenmiş çıktı
        
    return model
EOF

# ---------------------------------------------------------
# 4. VISUALS: Dashboard / Görselleştirme Modülü
# ---------------------------------------------------------
cat <<EOF > $PROJECT_NAME/visuals/dashboard.py
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
EOF

# ---------------------------------------------------------
# 5. UTILS: CSV Logger
# ---------------------------------------------------------
cat <<EOF > $PROJECT_NAME/utils/logger.py
import csv
import os

class NeuroLogger:
    def __init__(self, filename="data/neuro_data.csv"):
        self.filename = filename
        if not os.path.exists('data'): os.makedirs('data')
        
    def log(self, t, input_val, output_val):
        with open(self.filename, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([t, input_val, output_val])
EOF

# ---------------------------------------------------------
# 6. MAIN: Her Şeyi Birleştiren Ana Dosya
# ---------------------------------------------------------
cat <<EOF > $PROJECT_NAME/main.py
import nengo
from models.nengo_engine import create_nef_network
from utils.logger import NeuroLogger
from visuals.dashboard import plot_results

def run_system():
    print("--- 1protocol Neuromorphic Master System Başlatılıyor ---")
    
    # Sistem Bileşenleri
    model = create_nef_network()
    logger = NeuroLogger()
    
    # Simülasyonu Çalıştır
    with nengo.Simulator(model) as sim:
        print("🧠 Simülasyon koşturuluyor...")
        sim.run(1.0) # 1 saniyelik veri toplama
        
        # Verileri CSV'ye Yaz
        print("💾 Veriler kaydediliyor...")
        for i in range(len(sim.trange())):
            logger.log(sim.trange()[i], 
                       sim.data[model.probe_input][i][0], 
                       sim.data[model.probe_decoded][i][0])
    
    # Görsel Paneli Aç
    plot_results(sim, model)

if __name__ == "__main__":
    run_system()
EOF

# 7. Gereksinimler ve Yetkilendirme
echo -e "nengo\nlava-nc\nnumpy\nmatplotlib" > $PROJECT_NAME/requirements.txt
chmod +x $PROJECT_NAME/main.py

echo "-------------------------------------------------------"
echo "✅ Kurulum Başarıyla Tamamlandı!"
echo "1. Klasöre gir: cd $PROJECT_NAME"
echo "2. Bağımlılıkları kur: pip install -r requirements.txt"
echo "3. Sistemi başlat: python3 main.py"
echo "-------------------------------------------------------"

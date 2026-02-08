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

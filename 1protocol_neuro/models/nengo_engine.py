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

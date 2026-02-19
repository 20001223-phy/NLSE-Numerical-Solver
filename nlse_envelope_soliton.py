import numpy as np
import matplotlib.pyplot as plt

def plot_envelope_soliton():
    # Spatial domain parameters
    L = 30.0    
    N = 1000    
    x = np.linspace(-L/2, L/2, N)
    
    # 1. The Envelope: A localized sech pulse (Bright Soliton)
    width = 2.0
    envelope = 1.0 / np.cosh(x / width)
    
    # 2. The Carrier Wave: High-frequency oscillations
    k = 5.0  # Wave number
    carrier = np.cos(k * x)
    
    # 3. The Resulting Wave Packet (Modulated wave)
    modulated_wave = envelope * carrier

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(x, envelope, 'r--', label='Envelope (Slowly Varying)', linewidth=2)
    plt.plot(x, -envelope, 'r--', linewidth=2)
    plt.plot(x, modulated_wave, 'b', label='Modulated Carrier Wave', alpha=0.7)
    
    plt.title("Bright Envelope Soliton Profile", fontsize=14)
    plt.xlabel("Position (xi)", fontsize=12)
    plt.ylabel("Amplitude", fontsize=12)
    plt.legend(loc='upper right')
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    print("Generating Bright Envelope Soliton visualization...")
    plot_envelope_soliton()

from matplotlib.animation import FuncAnimation
from IPython.display import HTML
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

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# ... (keep your existing spatial domain and envelope variables) ...

# 1. Setup for Animation
fig, ax = plt.subplots(figsize=(10, 6))
line_envelope, = ax.plot([], [], 'r--', lw=2, label='Envelope')
line_carrier, = ax.plot([], [], 'b-', lw=1, alpha=0.6, label='Carrier')

def init():
    ax.set_xlim(-15, 15)
    ax.set_ylim(-1.2, 1.2)
    return line_envelope, line_carrier

# 2. Update function to show propagation (xi - u*tau)
def update(tau):
    u = 0.5  # Soliton velocity
    shift_xi = x - u * tau
    
    # Updated envelope and carrier based on shift
    env = 1.0 / np.cosh(shift_xi / width)
    car = env * np.cos(k * shift_xi)
    
    line_envelope.set_data(x, env)
    line_carrier.set_data(x, car)
    return line_envelope, line_carrier

# 3. Create Animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 100), init_func=init, blit=True)

# Display in Colab
HTML(ani.to_jshtml())

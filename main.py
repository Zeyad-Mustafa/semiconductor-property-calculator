import math

# Physical constants
k = 8.617333262145e-5  # Boltzmann constant in eV/K
q = 1.602e-19          # Charge of electron in C

def intrinsic_carrier_concentration(Nc, Nv, Eg, T):
    ni = math.sqrt(Nc * Nv) * math.exp(-Eg / (2 * k * T))
    return ni

def main():
    print("=== Semiconductor Property Calculator ===")

    T = float(input("Enter temperature (K): "))
    Eg = float(input("Enter bandgap energy (eV): "))
    Nc = float(input("Enter effective density of states in conduction band (per cm³): "))
    Nv = float(input("Enter effective density of states in valence band (per cm³): "))

    ni = intrinsic_carrier_concentration(Nc, Nv, Eg, T)
    print(f"\nIntrinsic Carrier Concentration (ni) = {ni:.2e} cm⁻³")

if __name__ == "__main__":
    main()

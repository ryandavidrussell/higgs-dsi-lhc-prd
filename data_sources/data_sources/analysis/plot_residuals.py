# =============================================================================
# LHC HIGGS ANALYSIS: RESIDUALS VISUALIZATION
# Generates a 4-panel plot of Data/Background vs Best-Fit Signal
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import warnings

warnings.filterwarnings("ignore")

# =============================================================================
# 1. HARDCODED DATA LOADERS (Same as Main Script)
# =============================================================================
def get_hww_data():
    Q = np.array([110.0, 135.0, 175.0, 225.0, 275.0, 325.0, 375.0, 425.0, 475.0, 525.0])
    val = np.array([0.452, 0.298, 0.156, 0.082, 0.045, 0.026, 0.015, 0.009, 0.005, 0.003])
    # Approximate diagonal errors for plotting
    err = np.sqrt(np.array([0.0021, 0.0010, 0.0008, 0.0007, 0.0006, 0.0005, 0.0004, 0.0003, 0.0002, 0.0001]))
    scale = (139.0 / 20.3) * 1000.0
    return val * scale, (err * scale), Q

def get_vbf_data():
    Q = np.array([110.0, 130.0, 155.0, 185.0, 225.0, 300.0, 400.0, 500.0])
    val = np.array([0.0786, 0.1175, 0.0738, 0.0258, 0.0254, 0.0079, 0.00097, 0.00031])
    err = np.array([0.041, 0.027, 0.017, 0.011, 0.0051, 0.0019, 0.00074, 0.00042])
    scale = 139.0 / 137.0
    return val * scale, err * scale, Q

def get_hgg_data():
    Q = np.array([70.0, 100.0, 160.0, 275.0])
    val = np.array([0.24, 0.188, 0.063, 0.0088])
    err = np.array([0.092, 0.045, 0.013, 0.0024])
    scale = (139.0 / 36.1) * 1000.0
    return val * scale, err * scale, Q

def get_hzz_data():
    Q = np.array([70.0, 100.0, 160.0, 275.0])
    val = np.array([0.0108, 0.0137, 0.0043, 0.00118])
    err = np.array([0.0074, 0.0050, 0.0019, 0.00071])
    scale = 139.0 / 36.1
    return val * scale, err * scale, Q

data_map = {
    "ggF H->WW": get_hww_data(),
    "VBF H->gg": get_vbf_data(),
    "ggF H->gg": get_hgg_data(),
    "ggF H->ZZ": get_hzz_data()
}

# =============================================================================
# 2. FIT ENGINE (To get baselines)
# =============================================================================
OMEGA_PHI = 2 * np.pi / np.log((1 + np.sqrt(5))/2)

def bg_model(x, a, b):
    return a * np.exp(-b * x)

def sig_model(x, a, b, amp, phi, gamma):
    bg = bg_model(x, a, b)
    u = np.log(x / 200.0)
    return bg * (1.0 + amp * np.exp(-gamma * u) * np.cos(OMEGA_PHI * u + phi))

# Fit Null to get B (Background)
bg_params = {}
for name, (val, err, Q) in data_map.items():
    def nll(p):
        return np.sum(((val - bg_model(Q, *p))/err)**2)
    res = minimize(nll, [np.max(val), 0.01], bounds=[(0,np.inf),(0,1)])
    bg_params[name] = res.x

# Fit Signal to get S (Signal)
# Using the 2.04 sigma result parameters as fixed reference to visualize the global fit
# Global Params from your run:
PHI_BEST = 0.082
GAMMA_BEST = 2.20
# Amplitudes from your run:
AMPS = {
    "ggF H->WW": 0.0233,
    "VBF H->gg": 0.1021,
    "ggF H->gg": -0.05, # Approx from the negative pull
    "ggF H->ZZ": -0.05  # Approx
}

# =============================================================================
# 3. PLOTTING
# =============================================================================
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

fig.suptitle(f"LHC Run 2 Higgs Residuals (Global Fit: $\Phi={PHI_BEST:.2f}$, $\gamma={GAMMA_BEST:.2f}$)", fontsize=16)

for i, (name, (val, err, Q)) in enumerate(data_map.items()):
    ax = axes[i]

    # 1. Calculate Background
    a, b = bg_params[name]
    B = bg_model(Q, a, b)

    # 2. Data Residuals (Relative)
    # (Data - BG) / BG
    res_data = (val - B) / B
    res_err  = err / B

    # 3. Signal Curve (Relative)
    # (Signal - BG) / BG = Modulation Term
    x_smooth = np.linspace(min(Q), max(Q), 100)
    B_smooth = bg_model(x_smooth, a, b)
    amp = AMPS.get(name, 0.0)
    S_smooth = sig_model(x_smooth, a, b, amp, PHI_BEST, GAMMA_BEST)
    res_curve = (S_smooth - B_smooth) / B_smooth

    # 4. Plot
    ax.errorbar(Q, res_data, yerr=res_err, fmt='o', color='black', label='Data - SM', capsize=3)
    ax.plot(x_smooth, res_curve, color='red', linewidth=2, label=f'Fit ($\\alpha={amp*100:.1f}\%$)')
    ax.axhline(0, linestyle='--', color='gray', alpha=0.5)

    # Styling
    ax.set_title(name, fontsize=12, fontweight='bold')
    ax.set_xlabel(r"$p_T^H$ [GeV]")
    ax.set_ylabel(r"(Data - SM) / SM")
    ax.set_xscale('log')
    ax.set_ylim(-0.5, 0.5) # Zoom in to see the wiggle
    ax.legend(loc='upper right', fontsize=9)
    ax.grid(True, which='both', linestyle=':', alpha=0.6)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("lhc_higgs_residuals_tug_of_war.png", dpi=300)
print("Plot saved to lhc_higgs_residuals_tug_of_war.png")
plt.show()

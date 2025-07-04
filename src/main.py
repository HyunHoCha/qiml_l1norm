import os
import sys
import math
import time
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import utils
from utils import *

'''
python3 main.py
'''

start_time = time.time()

# Configurations
n_list = [2 ** i for i in range(1, 4)]
p_list = np.linspace(1, 5, 401)
iters = 100  # iters for random A and x
matplotlib.rcParams['font.family'] = 'DejaVu Sans'
m = 1024

for is_gaussian in [True, False]:
    if is_gaussian: print("Gaussian distribution")
    if not is_gaussian: print("Uniform distribution")

    # sigma_f_squared = 1 if is_gaussian else 1 / 3
    sigma_f_squared = SIGMA_F_SQUARED(is_gaussian)
    rtpi = np.sqrt(np.pi)

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    save_path = os.path.join(base_dir, "gaussian") if is_gaussian else os.path.join(base_dir, "uniform")

    os.makedirs(save_path, exist_ok=True)

    for n in n_list:
        print(f"(n, m) = ({n}, {m})")
        estimate_data_list = []
        true_data_list = []
        for _ in range(iters):
            estimate_data = []
            true_data = []

            # A = np.random.randn(m, n) if is_gaussian else np.random.uniform(-1, 1, size=(m, n))
            # x = np.random.randn(n, 1) if is_gaussian else np.random.uniform(-1, 1, size=(n, 1))
            A = random_A(m, n, is_gaussian)
            x = random_x(n, is_gaussian)

            for p in p_list:
                mu_f_p = 2 ** (p / 2) * math.gamma((p + 1) / 2) / rtpi if is_gaussian else 1 / (p + 1)
                mu_f_p_tilde = sigma_f_squared ** p * 2 ** (p / 2) * math.gamma((p + 1) / 2) / rtpi
                estimate_data.append(n ** (p / 2) * mu_f_p ** 2 / mu_f_p_tilde)

                num = sum([np.linalg.norm(A[:, j] * x[j], ord=p) ** p for j in range(n)])
                den = np.linalg.norm((A @ x).flatten(), ord=p) ** p
                true_data.append(n ** (p - 1) * num / den)
            estimate_data_list.append(estimate_data)
            true_data_list.append(true_data)
        estimate_data_mean = [sum(group) / len(group) for group in zip(*estimate_data_list)]
        true_data_mean = [sum(group) / len(group) for group in zip(*true_data_list)]
        
        plt.figure()
        plt.plot(p_list, estimate_data_mean, label='estimate', linestyle='-', color='#00FF00', linewidth=3)
        plt.plot(p_list, true_data_mean, label='true', linestyle='--', color='blue', linewidth=3)
        plt.legend(fontsize=20)
        plt.title(rf'$n = {n}$', fontsize=20)
        plt.xlabel(r'$p$', fontsize=20)
        plt.ylabel(r'$\mathrm{\mathbb{E}}[M(p)]$', fontsize=20)
        plt.tick_params(axis='both', labelsize=15)
        plt.xticks([1, 2, 3, 4, 5])
        plt.grid(True)
        ax = plt.gca()
        ax.yaxis.get_offset_text().set_fontsize(15)
        plt.tight_layout()
        plt.savefig(os.path.join(save_path, f"theoretical_k{n}_compare.png"))
        plt.close()
print('Elapsed time:', time.time() - start_time)

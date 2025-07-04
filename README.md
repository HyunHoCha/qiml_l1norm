# Quantum Inspired Machine Learning (QIML) for Fast Vector Inner Product Approximation

This program uses **Quantum Inspired Machine Learning (QIML)** techniques to efficiently approximate vector inner products in logarithmic time by leveraging sampling-based methods.

---

## Features

- **Sampling-Based Acceleration**:
  - Achieves fast performance through sampling-based approximate computation.

- **Amplitude Encoding and L1 Sampling**:
  - Leverages amplitude encoding as used in quantum systems.
  - Extends beyond L2-norm sampling by supporting L1-norm sampling for better empirical performance.

- **Future Extensions**:
  - Suggests potential for generalizing to various QIML algorithms using optimal sampling strategies.

---

## Main Functions

- **Fast Approximate Inner Product Computation**:
  - Approximates vector inner products in logarithmic time using sampling-based methods.

- **Vector Storage and Query Support**:
  - Supports storing vectors and performing both query operations and sampling on them.

- **Support for Multiple Sampling Norms**:
  - Supports both L2-norm and L1-norm based sampling methods.

---

## How to Use

```bash
python3 main.py  # Run and compare L1 norm vs L2 norm sampling

# Neural Networks from Scratch: Personal Implementation
![Python](https://img.shields.io/badge/python-3.8%2B-blue) ![License](https://img.shields.io/badge/license-MIT-yellow) ![NumPy](https://img.shields.io/badge/numpy-required-green) ![Matplotlib](https://img.shields.io/badge/Matplotlib-required-green)

A concise, from-scratch Python/NumPy implementation inspired by Sentdex's *Neural Networks from Scratch* tutorial series.
Start of playlist: https://www.youtube.com/watch?v=Wo5dMEP_BbI&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3&index=1

## Summary
Minimal, modular implementation of neural network fundamentals (forward pass, activation functions, loss calculations). Intended as an educational piece to demonstrate understanding of ML building blocks and clean code organization.

## Highlights / Features
✅ **From-scratch math** - Forward & backward passes implemented with NumPy **(no PyTorch/TensorFlow)**.

✅ **Modular design** - Clear separation in: `layers`, `activations`, `losses`, etc. Easy to extend and unit-test.

✅ **Numerical care** - stable Softmax + log-loss, clipped/log-safe operations, and alternate loss functions implemented.

✅ **Runnable demo** - `neural_network.py` that prints losses and accuracy of a forward pass during training.

## Skills
Linear Algebra (vector calculus), Calculus, ML Fundamentals (loss functions, optimization), Python, NumPy, Algorithm design, Debugging, Data preprocessing, Model evaluation, Visualization (matplotlib), Version control (git), Experiment logging, Statistics, Problem solving

## Quick demo
Run the demo to see the example of loss and accuracy calculations. Can configure the data to run for your own forward step along with respective weights and biases.

```bash
# create & activate a venv (recommended)
python3 -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate      # Windows (PowerShell: .\.venv\Scripts\Activate.ps1)

# install deps
python -m pip install -r requirements.txt

# run the integrated script
python neural_network.py
```
**Author:** Nikhil Singla |
**GitHub:** `https://github.com/Nikhil-Singla/` |
**LinkedIn:** `https://www.linkedin.com/in/nsingla`
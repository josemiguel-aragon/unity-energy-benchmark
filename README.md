# Unity Energy Benchmark

This project provides an automated benchmarking pipeline to measure **runtime energy usage and performance** of Unity games or scenes compiled with **Mono vs IL2CPP** on **macOS with Apple Silicon** (M1/M2/M3).

It captures:

- 🔋 **CPU power consumption**
- 🧠 **CPU cluster frequency and active residency (E-Cluster & P-Cluster)**
- 🎮 **GPU power and frequency** (if available)
- ⏱ **Execution time**
- 💾 **Memory usage (max RSS)**
- 🎥 **Average FPS**, recorded in-game

---

## 🖥 Requirements

- macOS with Apple Silicon (M1/M2/M3)
- Unity project (Unity 2021+ recommended)
- GNU `time` installed via Homebrew:

```bash
brew install gnu-time

# Unity Energy Benchmark – Fantasy Kingdom Edition

This project contains a complete energy and performance benchmark based on Unity's **Fantasy Kingdom** demo scene. It analyzes energy performance on **macOS with Apple Silicon (M1/M2/M3)**.

The benchmark is fully integrated — no need to add scripts or modify the Unity project. Just build and run.

---

## 📊 Metrics captured

- 🔋 **CPU power consumption** (via `powermetrics`)
- 🎮 **GPU power and frequency** (via `powermetrics`)
- 🧠 **Cluster frequency and active residency** (E-Cluster and P-Cluster)
- 💾 **Peak memory usage**
- 🎥 **Average FPS**, recorded from within the app
- ⏱ **Execution time**

---

## 🖥 Requirements

- macOS with Apple Silicon (M1/M2/M3)
- Unity 2021.3+ (URP support)
- Fantasy Kingdom demo (already integrated)
- GNU `time` via Homebrew:

```bash
brew install gnu-time
```

## How to Run the Benchmark

### 1. Build the Unity Project

Build the Fantasy Kingdom scene

Make sure to:

- Target platform: **macOS**
- Architecture: **Apple Silicon** or **Universal**
- Keep the default 5-minute execution duration (already configured)

---

### 2. Run the Benchmark Script

Make the script executable:

```bash
chmod +x benchmark_unity_full.sh
```

Run the benchmark:

```bash
./benchmark_unity_full.sh ./Builds/Fantasy.app/Contents/MacOS/Fantasy 30 testing
```

Each iteration will:

- Start `powermetrics` in the background (1-second interval)
- Launch the Unity build
- Wait for automatic shutdown after 5 minutes
- Read average FPS from `/tmp/fps_log.txt`
- Collect runtime, memory, power, and frequency metrics
- Append a row to the output CSV file

---

## Output Files

You will get a CSV file:

```text
results_testing.csv
```

Each CSV will contain rows in the following format:
time(s),memory(KB),cpu_power(mW),freq_E(MHz),freq_P(MHz),freq_GPU(MHz),E-residency(%),P-residency(%),GPU(mW),Frame-rate(FPS)

## License
This project is released under the MIT License. You are free to use, modify, and share it for research, benchmarking, and educational purposes.

## Author
Developed by José M. Aragón-Jurado (GOAL Research Group)

Based on Unity’s official Fantasy Kingdom URP demo.

Feel free to open issues or submit pull requests for improvements or extensions.

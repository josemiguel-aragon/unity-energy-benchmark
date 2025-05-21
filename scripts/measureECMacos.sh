#!/bin/bash

# Uso:
# ./benchmark_unity_full.sh ./MyBuild.app/Contents/MacOS/MyBuild 5 il2cpp

executable=$1      # Ruta al binario
repeats=$2         # Número de repeticiones
tag=$3             # Etiqueta (ej. il2cpp, mono)

# Arrays de resultados
declare -a runtimes=()
declare -a powers=()
declare -a memories=()
declare -a e_clusters=()
declare -a p_clusters=()
declare -a gpu_powers=()
declare -a freq_e=()
declare -a freq_p=()
declare -a freq_gpu=()
declare -a fps_values=()

for i in $(seq 1 ${repeats}); do
    echo "▶️ Iteración $i..."

    # Limpieza
    rm -f powermetrics_raw.log runtime_metrics.tmp

    # Ejecuta powermetrics (1 muestra/s)
    sudo powermetrics -i 1  --hide-cpu-duty-cycle > powermetrics_raw.log &

    # Ejecuta binario y mide tiempo/memoria
    /opt/homebrew/opt/gnu-time/libexec/gnubin/time -f "%e,%M" -o runtime_metrics.tmp $executable

    # Termina powermetrics
    sudo pkill powermetrics
    sleep 0.1

    # ⚡ Energía
    power=$(grep "CPU Power" powermetrics_raw.log | awk '{ sum += $3 } END { if (NR > 0) print sum/NR; else print "0" }')

    # ⏱ Tiempo y 💾 Memoria
    time=$(cut -d',' -f1 runtime_metrics.tmp)
    mem=$(cut -d',' -f2 runtime_metrics.tmp)

    freq_e_avg=$(grep "E-Cluster HW active frequency" powermetrics_raw.log | awk '{ sum += $5 } END { if (NR > 0) print sum/NR; else print "0" }')
    freq_p_avg=$(grep "P-Cluster HW active frequency" powermetrics_raw.log | awk '{ sum += $5 } END { if (NR > 0) print sum/NR; else print "0" }')

    e_cluster=$(grep "E-Cluster HW active residency" powermetrics_raw.log | awk '{ sum += $5 } END { if (NR > 0) print sum/NR; else print "0" }')
    p_cluster=$(grep "P-Cluster HW active residency" powermetrics_raw.log | awk '{ sum += $5 } END { if (NR > 0) print sum/NR; else print "0" }')

    # 🎮 GPU Power 
    gpu_power=$(grep "GPU Power" powermetrics_raw.log | awk '{ sum += $3 } END { if (NR > 0) print sum/NR; else print "NA" }')
    # GPU frequency 
    freq_gpu_avg=$(grep "GPU HW active frequency" powermetrics_raw.log | awk '{ sum += $5 } END { if (NR > 0) print sum/NR; else print "NA" }')

    # 🖥️ Leer FPS desde archivo Unity
    fps=$(cat /tmp/fps_log.txt 2>/dev/null)
    [ -z "$fps" ] && fps="NA"  # En caso de que el archivo no exista
    rm -f /tmp/fps_log.txt

    # Acumula
    runtimes+=("$time")
    powers+=("$power")
    memories+=("$mem")
    e_clusters+=("$e_cluster")
    p_clusters+=("$p_cluster")
    freq_e+=("$freq_e_avg")
    freq_p+=("$freq_p_avg")
    gpu_powers+=("$gpu_power")
    freq_gpu+=("$freq_gpu_avg")
    fps_values+=("$fps")

    echo "✅ t=${time}s, mem=${mem}KB, power=${power}mW, Freq E=${freq_e_avg}MHz, Freq P=${freq_p_avg}MHz, E=${e_cluster}%, P=${p_cluster}%, GPU=${gpu_power}mW, Freq GPU=${freq_gpu_avg}MHz, Frame rate=${fps}FPS"

done

# Exporta resultados
paste -d',' \
    <(printf "%s\n" "${runtimes[@]}") \
    <(printf "%s\n" "${memories[@]}") \
    <(printf "%s\n" "${powers[@]}") \
    <(printf "%s\n" "${freq_e[@]}") \
    <(printf "%s\n" "${freq_p[@]}") \
    <(printf "%s\n" "${freq_gpu[@]}") \
    <(printf "%s\n" "${e_clusters[@]}") \
    <(printf "%s\n" "${p_clusters[@]}") \
    <(printf "%s\n" "${gpu_powers[@]}") \
        <(printf "%s\n" "${fps_values[@]}") \
    > results_${tag}.csv

echo "📁 Guardado: results_${tag}.csv"
echo "📊 Columnas: time(s), memory(KB), cpu_power(mW), freq_E(MHz), freq_P(MHz), E-residency(%), P-residency(%), GPU(mW), Frame rate(FPS)"

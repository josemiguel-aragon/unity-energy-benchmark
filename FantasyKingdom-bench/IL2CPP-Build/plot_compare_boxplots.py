import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import matplotlib.pylab as pylab
params = {'axes.labelsize': 22,
         'xtick.labelsize': 22,
         'ytick.labelsize': 22}
pylab.rcParams.update(params)


input_files = [
    "IL2CPP-Dev-FasterBuild-Release-Build",
    "IL2CPP-FasterBuild-Release-Build",
    "IL2CPP-Dev-FasterRuntime-Release-Build",
    "IL2CPP-FasterRuntime-Release-Build"
]

if __name__ == '__main__':
    labels = [
        "Dev-FB",
        "FB",
        "Dev-FR",
        "FR"
    ]

    tags = labels.copy()
    
    data_cpu_power = []
    data_gpu_power = []
    data_p_cpu_frequency = []
    data_gpu_frequency = []
    data_e_cpu_frequency = []
    data_fps = []
    
    
    
    df = pd.DataFrame()
    df2 = pd.DataFrame()
    
    for i,x in enumerate(input_files):
        count = 0
        df = pd.read_csv(f'results_{x}.csv', header=None, index_col=False, names=[ "time", "memory", "cpu_power", "freq_E", "freq_P",
        "GPU_freq", "E-residency", "P-residency", "GPU_power", "frame_rate"])
       
        data_cpu_power.append(df["cpu_power"]/1000)
        data_gpu_power.append(df["GPU_power"]/1000)
        data_p_cpu_frequency.append(df["freq_P"])
        data_gpu_frequency.append(df["GPU_freq"])
        data_e_cpu_frequency.append(df["freq_E"])
        data_fps.append(df["frame_rate"])


        df[x.replace('-','')] = data_cpu_power[-1]
        df2[x.replace('-','')] = data_gpu_power[-1]
            
            
    df.to_csv("cpu_power_measurements_df.csv")
    df2.to_csv("gpu_power_measurements_df.csv")
    
    fig, ax1 = plt.subplots(nrows=3, ncols=2, figsize=(20, 10.5))
    
    ax1[0,0].plot([i for i in range(1,len(input_files)+1)], np.median(np.array(data_cpu_power), axis=1), color='indianred', alpha=0.75, label="_no_legend")
    ax1[0,0].plot([i for i in range(1,len(input_files)+1)], np.array(data_cpu_power).min(axis=1), color='k', linestyle='dashed', linewidth=0.75, alpha=0.75, label='Line of best fit: Mean miliWatts Versus Optimization flag')
    ax1[0,0].plot([i for i in range(1,len(input_files)+1)], np.array(data_cpu_power).max(axis=1), color='k', linestyle='dashed', linewidth=0.75, alpha=0.75, label='_no_legend')
    ax1[0,0].fill_between([i for i in range(1,len(input_files)+1)], np.array(data_cpu_power).min(axis=1), np.array(data_cpu_power).max(axis=1), color='mediumseagreen', alpha=0.25, label="Range of Min and Max Mean miliWatts per Optimization flag")
    bp = ax1[0,0].boxplot(data_cpu_power, labels=tags, patch_artist=True)
    for patch in bp['boxes']:
        patch.set(facecolor='w')
    ax1[0,0].set_ylabel("CPU Power (W)")
    ax1[0,0].set_xticklabels(labels=tags, rotation=60, ha="right")
    
    
    ax1[0,1].plot([i for i in range(1,len(input_files)+1)], np.median(np.array(data_gpu_power), axis=1), color='indianred', alpha=0.75, label="_no_legend")
    ax1[0,1].plot([i for i in range(1,len(input_files)+1)], np.array(data_gpu_power).min(axis=1), color='k', linestyle='dashed', linewidth=0.75, alpha=0.75, label='Line of best fit: Runtime Versus Optimization flag')
    ax1[0,1].plot([i for i in range(1,len(input_files)+1)], np.array(data_gpu_power).max(axis=1), color='k', linestyle='dashed', linewidth=0.75, alpha=0.75, label='_no_legend')
    ax1[0,1].fill_between([i for i in range(1,len(input_files)+1)], np.array(data_gpu_power).min(axis=1), np.array(data_gpu_power).max(axis=1), color='mediumseagreen', alpha=0.25, label="Range of Min and Max Runtime per Optimization flag")
    bp = ax1[0,1].boxplot(data_gpu_power, labels=tags, patch_artist=True)
    for patch in bp['boxes']:
        patch.set(facecolor='w')
    ax1[0,1].set_ylabel("GPU Power (W)")
    ax1[0,1].set_xticklabels(labels=tags, rotation=60, ha="right")

    
    ax1[1,0].plot([i for i in range(1,len(input_files)+1)], np.median(np.array(data_p_cpu_frequency), axis=1), color='indianred', alpha=0.75, label="_no_legend")
    ax1[1,0].plot([i for i in range(1,len(input_files)+1)], np.array(data_p_cpu_frequency).min(axis=1), color='k', linestyle='dashed', linewidth=0.75, alpha=0.75, label='Line of best fit: Runtime Versus Optimization flag')
    ax1[1,0].plot([i for i in range(1,len(input_files)+1)], np.array(data_p_cpu_frequency).max(axis=1), color='k', linestyle='dashed', linewidth=0.75, alpha=0.75, label='_no_legend')
    ax1[1,0].fill_between([i for i in range(1,len(input_files)+1)], np.array(data_p_cpu_frequency).min(axis=1), np.array(data_p_cpu_frequency).max(axis=1), color='mediumseagreen', alpha=0.25, label="Range of Min and Max Runtime per Optimization flag")
    bp = ax1[1,0].boxplot(data_p_cpu_frequency, labels=tags, patch_artist=True)
    for patch in bp['boxes']:
        patch.set(facecolor='w')
    ax1[1,0].set_ylabel("P CPU Freq (MHz)")
    ax1[1,0].set_xticklabels(labels=tags, rotation=60, ha="right")
    
    ax1[1,1].plot([i for i in range(1,len(input_files)+1)], np.median(np.array(data_gpu_frequency), axis=1), color='indianred', alpha=0.75, label="_no_legend")
    ax1[1,1].plot([i for i in range(1,len(input_files)+1)], np.array(data_gpu_frequency).min(axis=1), color='k', linestyle='dashed', linewidth=0.75, alpha=0.75, label='Line of best fit: Runtime Versus Optimization flag')
    ax1[1,1].plot([i for i in range(1,len(input_files)+1)], np.array(data_gpu_frequency).max(axis=1), color='k', linestyle='dashed', linewidth=0.75, alpha=0.75, label='_no_legend')
    ax1[1,1].fill_between([i for i in range(1,len(input_files)+1)], np.array(data_gpu_frequency).min(axis=1), np.array(data_gpu_frequency).max(axis=1), color='mediumseagreen', alpha=0.25, label="Range of Min and Max Runtime per Optimization flag")
    bp = ax1[1,1].boxplot(data_gpu_frequency, labels=tags, patch_artist=True)
    for patch in bp['boxes']:
        patch.set(facecolor='w')
    ax1[1,1].set_ylabel("GPU Frew (MHz)")
    ax1[1,1].set_xticklabels(labels=tags, rotation=60, ha="right")
    
    
    ax1[2,0].plot([i for i in range(1,len(input_files)+1)], np.median(np.array(data_e_cpu_frequency), axis=1), color='indianred', alpha=0.75, label="_no_legend")
    ax1[2,0].plot([i for i in range(1,len(input_files)+1)], np.array(data_e_cpu_frequency).min(axis=1), color='k', linestyle='dashed', linewidth=0.75, alpha=0.75, label='Line of best fit: Runtime Versus Optimization flag')
    ax1[2,0].plot([i for i in range(1,len(input_files)+1)], np.array(data_e_cpu_frequency).max(axis=1), color='k', linestyle='dashed', linewidth=0.75, alpha=0.75, label='_no_legend')
    ax1[2,0].fill_between([i for i in range(1,len(input_files)+1)], np.array(data_e_cpu_frequency).min(axis=1), np.array(data_e_cpu_frequency).max(axis=1), color='mediumseagreen', alpha=0.25, label="Range of Min and Max Runtime per Optimization flag")
    bp = ax1[2,0].boxplot(data_e_cpu_frequency, labels=tags, patch_artist=True)
    for patch in bp['boxes']:
        patch.set(facecolor='w')
    ax1[2,0].set_ylabel("E CPU Freq (MHz)")
    ax1[2,0].set_xticklabels(labels=tags, rotation=60, ha="right")
    
    
    ax1[2,1].plot([i for i in range(1,len(input_files)+1)], np.median(np.array(data_fps), axis=1), color='indianred', alpha=0.75, label="_no_legend")
    ax1[2,1].plot([i for i in range(1,len(input_files)+1)], np.array(data_fps).min(axis=1), color='k', linestyle='dashed', linewidth=0.75, alpha=0.75, label='Line of best fit: Runtime Versus Optimization flag')
    ax1[2,1].plot([i for i in range(1,len(input_files)+1)], np.array(data_fps).max(axis=1), color='k', linestyle='dashed', linewidth=0.75, alpha=0.75, label='_no_legend')
    ax1[2,1].fill_between([i for i in range(1,len(input_files)+1)], np.array(data_fps).min(axis=1), np.array(data_fps).max(axis=1), color='mediumseagreen', alpha=0.25, label="Range of Min and Max Runtime per Optimization flag")
    bp = ax1[2,1].boxplot(data_fps, labels=tags, patch_artist=True)
    for patch in bp['boxes']:
        patch.set(facecolor='w')
    ax1[2,1].set_ylabel("Frame rate (FPS)")
    ax1[2,1].set_xticklabels(labels=tags, rotation=60, ha="right")
    
    
    fig.tight_layout(pad=1.5)


    plt.savefig(f"./improvementbpFantasyKingdom.png", dpi=300)
    
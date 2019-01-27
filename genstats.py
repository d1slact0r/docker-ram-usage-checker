from pip._internal import main
main(["install", "matplotlib", "numpy","pandas"])

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

log_path = "/stats/docker-logs.txt"

with open(log_path) as f:
    raw_data = f.readlines()
nrows = 8
n = len(raw_data) // nrows
data = []
for i in range(n):
    start = i * nrows
    end = start + nrows - 1
    d = raw_data[start:end]
    datum = {}
    datum['i'] = i
    for line in d:
        if line.count(',') != 1:
            continue
        name, stats = line.strip().split(',')
        stats = float(stats.split('/')[0].strip()[:-3])
        datum[name] = stats
    data.append(datum)

data = pd.DataFrame(data)
data['time (hour)'] = data['i'] * 10 / 60
ax = data.drop(columns='i').set_index('time (hour)').plot()
ax.set_ylabel('RAM Usage (MiB)')
ax.figure.savefig('/stats/plot.png')
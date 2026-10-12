import re, sys
import matplotlib.pyplot as plt

log = sys.argv[1]
steps, tr, va = [], [], []
for line in open(log):
    m = re.search(r'step (\d+): train loss ([\d.]+), val loss ([\d.]+)', line)
    if m:
        steps.append(int(m[1])); tr.append(float(m[2])); va.append(float(m[3]))

plt.plot(steps, tr, 'o-', label='train')
plt.plot(steps, va, 'o-', label='val')
plt.xlabel('iteration'); plt.ylabel('loss'); plt.legend(); plt.grid(alpha=.3)
plt.title('Baseline (shakespeare_char)')
plt.savefig(log.replace('.log', '.png'), dpi=150)
print('final val loss:', va[-1], '| best val loss:', min(va))
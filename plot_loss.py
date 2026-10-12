import os, re, sys
import matplotlib.pyplot as plt

log = sys.argv[1]
d = os.path.dirname(log); name = os.path.basename(d)  
steps, tr, va = [], [], []
for line in open(log):
    m = re.search(r'step (\d+): train loss ([\d.]+), val loss ([\d.]+)', line)
    if m:
        steps.append(int(m[1])); tr.append(float(m[2])); va.append(float(m[3]))

plt.plot(steps, tr, 'o-', label='train')
plt.plot(steps, va, 'o-', label='val')
plt.xlabel('iteration'); plt.ylabel('loss'); plt.legend(); plt.grid(alpha=.3)
plt.title(f"{name} (shakespeare_char)")
plt.savefig(os.path.join(d, f"{name}.png"), dpi=150)
print('final val loss:', va[-1], '| best val loss:', min(va))
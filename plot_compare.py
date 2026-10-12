import re, sys
import matplotlib.pyplot as plt

out_png, names = sys.argv[1], sys.argv[2:]
plt.figure(figsize=(8, 4.5))
for n in names:
    s, tr, va = [], [], []
    for line in open(f'out/{n}/train.log'):
        m = re.search(r'step (\d+): train loss ([\d.]+), val loss ([\d.]+)', line)
        if m:
            s.append(int(m[1])); tr.append(float(m[2])); va.append(float(m[3]))
    p = plt.plot(s, va, 'o-', ms=3, label=f'{n} val')
    plt.plot(s, tr, '--', color=p[0].get_color(), alpha=.6, label=f'{n} train')
    i = va.index(min(va))
    print(f'{n:10s} best val {va[i]:.4f} @ step {s[i]}   final val {va[-1]:.4f}')
plt.xlabel('iteration'); plt.ylabel('loss'); plt.ylim(0.5, 2.5)
plt.legend(); plt.grid(alpha=.3); plt.tight_layout(); plt.savefig(out_png, dpi=150)
print('saved', out_png)

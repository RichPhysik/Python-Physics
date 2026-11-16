# %%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.ticker import MultipleLocator

plt.rcParams["font.family"] = "STIXGeneral"
plt.rcParams["mathtext.fontset"] = "stix"

def projectile_motion(v0, theta, k, dt, g): 
    angle = np.radians(theta)
    vx, vy = v0 * np.cos(angle), v0 * np.sin(angle)
    x, y = 0, 0
    xs, ys = [x], [y]

    while y>= 0:
        ax = -k * vx # acceleration in x-direction
        ay = g - k * vy # acceleration in y-direction 
        vx += ax * dt # velocity in x-direction
        vy += ay * dt # velocity in y-direction
        x += vx * dt # position in x-direction
        y += vy * dt # position in y-direction
        xs.append(x)
        ys.append(y)
        if y < 0:
            break
    return np.array(xs), np.array(ys)

x, y = projectile_motion(v0=30, theta=45, k=0.1, dt=0.1, g=-9.81)
x0, y0 = projectile_motion(v0=30, theta=45, k=0, dt=0.1, g=-9.81)   # no drag

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(x, y, color="red", linewidth=1, label="With drag")
ax.plot(x0, y0, color="green", linewidth=1, label="No drag")

ax.set_title("Projectile Motion with and without Drag", fontsize=16, fontweight="bold")
ax.set_xlabel("x (m)", fontsize=13, fontweight="bold")
ax.set_ylabel("y (m)", fontsize=13, fontweight="bold")

# grid: major every 10 m / 5 m, minor lines in between
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(MultipleLocator(2))
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(MultipleLocator(1))
ax.grid(which="major", linestyle="-", linewidth=0.8, alpha=0.6)
ax.grid(which="minor", linestyle=":", linewidth=0.5, alpha=0.4)
ax.set_xlim(0, 100)
ax.set_ylim(0, 30)

ax.tick_params(which="both", direction="in", top=True, right=True)
ax.legend(prop={"weight": "bold", "size": 12})

plt.tight_layout()
plt.show()
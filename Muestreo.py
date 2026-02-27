import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go

f1 = 10  # f1 = 10Hz... T1 = 1/10 = 0.1s
fs1 = 10*f1   # Ts = 1/fs = Delta =
Delta1 = 1/fs1 # Delta = 1/20 = 0.05s
t1 = np.arange(0, 0.3+Delta1, Delta1)
x1_t = np.cos(2*np.pi*f1*t1)

f2 = 30  # f1 = 10Hz... T1 = 1/10 = 0.1s
fs2 = 10*f2   # Ts = 1/fs = Delta =
Delta2 = 1/fs2 # Delta = 1/20 = 0.05s
t2 = np.arange(0, (3/f2)+Delta2, Delta2)
x2_t = np.cos(2*np.pi*f2*t2)

f3 = 50  # f1 = 10Hz... T1 = 1/10 = 0.1s
fs3 = 10*f3   # Ts = 1/fs = Delta =
Delta3 = 1/fs3 # Delta = 1/20 = 0.05s
t3 = np.arange(0, (3/f3)+Delta3, Delta3)
x3_t = np.cos(2*np.pi*f3*t3)

plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.plot(t1, x1_t)
plt.subplot(1,3,2)
plt.plot(t2, x2_t)
plt.subplot(1,3,3)
plt.plot(t3, x3_t)
plt.show()

fig = go.Figure()
fig.add_trace(go.Scatter(x=t1, y=x1_t, mode='lines', name='f1=10Hz'))
fig.update_layout(
    title="Señal Sinusoidal",
    xaxis_title="Time (s)",
    yaxis_title="mV"
    showlegend=True
)
fig.show()

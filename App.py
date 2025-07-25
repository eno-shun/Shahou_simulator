import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🎯 斜方投射simulator")

v0 = st.slider("初速度 v₀ (m/s)", 0, 40, 20)
theta_deg = st.slider("発射角度 θ (度)", 0, 90, 45)
g = st.slider("重力加速度 g (m/s²)", 0.1, 20.0, 9.8)

theta_rad = np.radians(theta_deg)
vx = v0 * np.cos(theta_rad)
vy = v0 * np.sin(theta_rad)
T = 2 * vy / g
t = np.linspace(0, T, num=300)
x = vx * t
y = vy * t - 0.5 * g * t**2

range_ = max(x)
max_height = (vy**2) / (2 * g)

st.markdown(f"**飛距離** ≈ {range_:.2f} m")
st.markdown(f"**最高点** ≈ {max_height:.2f} m")

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("distance x (m)")
ax.set_ylabel("high y (m)")
ax.set_title(f"v₀ = {v0} m/s, θ = {theta_deg}°, g = {g} m/s²")
ax.set_xlim(0, 60)     # 横軸：距離（x）
ax.set_ylim(0, 25)     # 縦軸：高さ（y）

ax.set_aspect('equal')
st.pyplot(fig)

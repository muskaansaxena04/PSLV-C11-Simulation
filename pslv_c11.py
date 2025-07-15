import numpy as np
import matplotlib.pyplot as plt

# stage 1

g0 = 9.80665 # m/s^2
Isp = 237 # s (sea level) - specific impulse
Ve = Isp * g0 # m/s - exhaust velocity

stage1_mass = 320000 # kg
propellant_mass_core = 138000 # kg - HTPB Solid Propellant
thrust_core = 4910000 # N
burn_time_core = 98 # s

num_boosters = 6
propellant_mass_per_booster = 12000 # kg
propellant_mass_boosters = num_boosters * propellant_mass_per_booster
total_propellant = propellant_mass_core + propellant_mass_boosters

dry_mass = stage1_mass - total_propellant
wet_mass = propellant_mass_core + dry_mass

thrust_per_booster = 720000 # N
thrust_boosters_initial = thrust_per_booster * 4 # at T = 0
thrust_boosters_full = thrust_per_booster * 6 # after T = 25 s
burn_time_boosters = 49 # s

fig, axs = plt.subplots(2, 2, figsize = (12,8))
(ax1, ax2, ax3, ax4) = axs.flatten()

def thrust_profile(t):

    if t < 25 :
        return thrust_core + thrust_boosters_initial
    
    elif t < 49 :
        return thrust_core + thrust_boosters_full
    
    elif t < burn_time_core :
        return thrust_core
    
    else :
        return 0
    
t = np.linspace(0, 120, 1000)

def thrust_profile_array(t_array):
    return np.array([thrust_profile(ti) for ti in t_array])

thrust = thrust_profile_array(t)
ax1.plot(t, thrust/1000, color = '#350E1D', alpha = 0.7)
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Thrust (kN)")
ax1.set_title("Thrust vs Time")

mass_flow_core = thrust_core / Ve # kg/s
mass_flow_booster = thrust_per_booster / Ve

def mass_over_time(t) :
    core_burned = min(t, burn_time_core) * mass_flow_core
    boosters_burned = min(t, burn_time_boosters) * mass_flow_booster * num_boosters
    total_mass = stage1_mass - core_burned - boosters_burned
    return max(total_mass, dry_mass) # Booster burn ends at 49 s

mass = np.array([mass_over_time(ti) for ti in t])

ax2.plot(t, mass / 1000, color = '#D54B00', alpha = 0.7)
ax2.set_title("Mass vs Time")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Mass (Tonnes)")

def acceleration_over_time(t) :
    m = mass_over_time(t)
    T = thrust_profile(t)
    a = (T / m) - g0
    return a

acceleration = np.array([acceleration_over_time(ti) for ti in t])

ax3.plot(t, acceleration, color = '#800E13', alpha = 0.7)
ax3.set_title('Acceleration vs Time')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Acceleration (m/s^2)')

dt = t[1] - t[0]
velocity = np.cumsum(acceleration * dt)

ax4.plot(t, velocity, color = '#2B35AF', alpha = 0.7)
ax4.set_title('Velocity vs Time')
ax4.set_xlabel('Time (s)')
ax4.set_ylabel('Velocity (m/s)')

# Tsiolkovsky Rocket Equation
initial_mass = stage1_mass
final_mass = dry_mass
delta_v = Ve * np.log(initial_mass / final_mass)
print(f"Delta v for the PSLV C11 Stage 1 determined by the Tsiolkovsky Equation is : {delta_v : .2f} m/s")

plt.tight_layout()
plt.savefig("PSLV-C11.png", dpi = 300)
plt.show()
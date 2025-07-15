# PSLV-C11-Simulation
Python simulation of the PSLV-C11 Stage 1 burn using real-world physics equations and ISRO data.

A Python-based physics simulation of the first-stage burn of ISRO's PSLV-C11 launch vehicle. This project visualizes core rocket dynamics like **thrust**, **mass decay**, **acceleration**, **velocity** and calculates the **delta-v** using the Tsiolkovsky rocket equation, all based on publicly available ISRO data and fundamental aerospace principles.

## Simulation Features

- Thrust vs Time (realistic thrust profile including booster ignition stages)
- Mass vs Time (propellant consumption modeled dynamically)
- Acceleration vs Time (net vertical acceleration)
- Velocity vs Time (via numerical integration)
- Delta-v calculation using the Tsiolkovsky Rocket Equation

All plots are generated using **Matplotlib** and **NumPy** for smooth and high-resolution output.

## Tools & Libraries Used

- Python 3.x
- NumPy
- Matplotlib

## Physics Modeled

- Thrust stages based on PSLV-XL config:
  Core stage + 6 strap-on boosters (4 ignited at launch, 2 after 25s)
- Mass reduction over time due to fuel burn
- Net acceleration:
  a(t) = T(t) / m(t) - g0
- Velocity (v) calculated from acceleration using:
  velocity = np.cumsum(acceleration * dt)
- Delta v via Tsiolkovsky Equation
  Δv = Ve * ln(m0/mf)

## Data Assumptions

- Based on publicly available information from ISRO and reliable secondary sources
- Assumes a lift-off mass of ~320 tonnes
- Booster timing: 4 ignite at T=0s, 2 ignite at T=25s
- Burnout: Boosters (49s), Core (98s)

## Disclaimer

This is an educational simulation for learning purposes. Some parameters are estimated due to limited publicly available data.

## Graphical Results

<img width="800" alt="PSLV-C11" src="https://github.com/user-attachments/assets/48b12a52-8ef5-4c16-86fc-0c7b666a14c6" />

## License

This project is an open-source under the MIT License.

## Author

Muskaan Saxena

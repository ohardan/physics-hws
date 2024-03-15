import streamlit as st
import numpy as np
from math import log, e


def convert(value, prefix):
    index = {
        "p": 10**12,
        "n": 10**9,
        "u": 10**6,
        "m": 10**3,
        "c": 10**2,
        "k": 10**-3,
        "M": 10**-6,
        "G": 10**-9,
    }

    return value * index[prefix]


def q1():
    st.header("Q1", divider="gray")
    st.write(
        "A ...... wire has a resistance of ...R... Ω at ...T1...°C. Determine its resistance (in Ω) at ...T2...°C. The temperature coefficient of resistivity for ...... wire is ...α... (°C)-1. (Assume that the temperature coefficient of resistivity was measured using the reference temperature 20°C.)"
    )

    st.subheader("Data:")
    resistance = st.number_input(
        "Enter R (Ω): ",
        value=5.50,
        step=0.01,
    )
    temp1 = st.number_input(
        "Enter T1 (°C): ",
        value=10.0,
        step=0.01,
    )
    temp2 = st.number_input(
        "Enter T2 (°C): ",
        value=410.0,
        step=0.01,
    )
    alpha = st.number_input(
        "Enter α temprature coefficient (°C^-1):",
        value=4.50e-3,
        step=1e-3,
        format="%e",
    )

    # calculations
    resistance_at_20 = resistance / (1 + alpha * (temp1 - 20))
    resistance_at_temp2 = resistance_at_20 * (1 + alpha * (temp2 - 20))

    st.subheader("Answers:")
    st.write("The resistance at T2 is (Ω):")
    st.code(f"{resistance_at_temp2:.2f}")


def q2():
    st.header("Q2", divider="gray")
    st.write(
        "An iron wire has a cross-sectional area equal to ...A... m^2. Carry out the following steps to determine the drift speed of the conduction electrons in the wire if it carries a current of ...I... A."
    )

    st.subheader("Data:")
    area = st.number_input(
        "Enter A (m^2): ",
        value=1.1e-5,
        step=1e-5,
        format="%e",
    )
    current = st.number_input(
        "Enter I (A): ",
        value=31.0,
        step=0.1,
    )

    # calculations
    kg_per_mol = 55.8e-3
    iron_density = 7.87e3
    molar_density = iron_density / kg_per_mol
    number_density = molar_density * 6.02e23
    conduction_electrons = 2 * number_density
    drift_speed = current / (1.6e-19 * area * 2 * 8.5e28)

    st.subheader("Answers:")

    st.write("a) The kilograms in 1.00 mole of iron (kg/mol):")
    st.code(f"{kg_per_mol:.2e}")

    st.write("b) The molar density of iron is (mol/m^3):")
    st.code(f"{molar_density:.2e}")

    st.write("c) The number density of iron atoms (atoms/m^3):")
    st.code(f"{number_density:.2e}")

    st.write("d) The number density of conduction electrons (electrons/m^3):")
    st.code(f"{conduction_electrons:.2e}")

    st.write("e) The drift speed of the conduction electrons is (m/s):")
    st.code(f"{drift_speed:.2e}")


def q3():
    st.header("Q3", divider="gray")
    st.write(
        "A well-insulated electric water heater warms ...m... kg of water from 20.0°C to ...T...°C in ...t... min"
    )

    st.subheader("Data:")
    temprature1 = 20
    mass = st.number_input("Enter m (kg): ", value=129.0, step=0.1)
    temprature2 = st.number_input("Enter T (°C): ", value=45.0, step=0.1)
    time = st.number_input("Enter t (min): ", value=23.0, step=0.1)
    voltage = 240.0
    specific_heat = 4186
    temprature3 = 100
    latent_heat = 2260e3

    # calculations
    energy = mass * specific_heat * (temprature2 - temprature1)
    power = energy / (time * 60)
    current = power / voltage
    resistance = voltage / current
    energy2 = mass * specific_heat * (temprature3 - temprature2)
    time2 = energy2 / power
    energy3 = mass * (specific_heat * (temprature3 - temprature1) + latent_heat)
    time3 = energy3 / power

    st.subheader("Answers:")

    st.write("c) The resistance of the heater is (Ω):")
    st.code(f"{resistance:.2f}")

    st.write("e) The time required to boil the water is (min):")
    st.code(f"{time2 / 60:.2f}")

    st.write("f) The total time required is (min):")
    st.code(f"{time3 / 60:.2f}")


def q4():
    st.header("Q4", divider="gray")
    st.write(
        "A ...... wire has a length of 1.50 m and a cross sectional area of ...A... mm^2. If the resistivity of ...... is ...p... Ω · m and a potential difference of ...V... V is maintained across its length, determine the current in the wire (in A)."
    )

    st.subheader("Data:")
    length = 1.5
    area = st.number_input(
        "Enter A (mm^2): ",
        value=0.340,
        step=0.001,
        format="%.3f",
    )
    resistivity = st.number_input(
        "Enter resistivity (p) (Ω·m): ",
        value=1.70e-8,
        step=1e-8,
        format="%e",
    )
    voltage = st.number_input(
        "Enter V (V): ",
        value=0.700,
        step=0.001,
        format="%.3f",
    )

    # calculations
    current = (voltage * area * 1e-6) / (resistivity * length)

    st.subheader("Answers:")

    st.write("The Current (A):")
    st.code(f"{current:.2f}")


def q5():
    st.header("Q5", divider="gray")
    st.write(
        "A ...l...-km-long high-voltage transmission line 2.00 cm in diameter carries a steady current of ...I... A. If the conductor is copper with a free charge density of 8.50 * 10^28 electrons per cubic meter, how many years does it take one electron to travel the full length of the cable? (Use 3.156 * 10^7 for the number of seconds in a year.)"
    )

    st.subheader("Data:")
    free_charge_density = 8.50e28
    diameter = 2.00e-2
    seconds_in_year = 3.156e7
    length = st.number_input("Enter cable length (km): ", value=230.0, step=0.1)
    current = st.number_input("Enter current (A): ", value=1050.0, step=0.1)

    # calculations
    area = np.pi * (diameter / 2) ** 2
    drift_speed = current / (1.6e-19 * area * free_charge_density)
    time = (length * 1e3) / drift_speed
    years = time / seconds_in_year

    st.subheader("Answers:")
    st.write("The time required to travel the full length of the cable is (yr):")
    st.code(f"{years:.2f}")


if __name__ == "__main__":
    st.title("HW05 - Chapter 26")
    q1()
    q2()
    q3()
    q4()
    q5()

import streamlit as st
import numpy as np
from math import log, e


def convert(value, prefix):
    index = {
        "p": 10**12,
        "n": 10**9,
        "u": 10**6,
        "m": 10**3,
        "k": 10**-3,
        "M": 10**-6,
        "G": 10**-9,
    }

    return value * index[prefix]


def q1():
    st.header("Q1", divider="gray")
    st.write(
        "A ...C...-nF parallel-plate capacitor is charged to an initial potential difference ΔVi = 100 V and is then isolated. The dielectric material between the plates is ....., with a dielectric constant of ...K..."
    )

    st.subheader("Data:")
    capacitance = st.number_input("Enter C (nF): ", value=1.5, step=0.01)
    dielectric_constant = st.number_input(
        "Enter K (dielectric constant): ", value=5.00, step=0.01
    )

    # calculations
    energy_no_plate = (0.5) * (capacitance * 10**-9) * (100**2)
    energy_with_plate = (
        (0.5) * (capacitance * 10**-9) * (100**2) * (dielectric_constant)
    )
    work_remove_plate = energy_with_plate - energy_no_plate
    potential_difference = dielectric_constant * 100

    st.subheader("Answers:")
    st.write("a) The work done is (µJ):")
    st.code(f"{convert(work_remove_plate, 'u'):.2f}")
    st.write("b) The potential difference is (V):")
    st.code(f"{potential_difference:.2f}")


def q2():
    st.header("Q2", divider="gray")
    st.write(
        f"a) A ...C...-µF capacitor is connected to a ...V...-V battery. How much energy is stored in the capacitor?"
    )
    st.write(
        "b) Had the capacitor been connected to a 6.00-V battery, how much energy would have been stored?"
    )

    st.subheader("Data:")
    capacitance = st.number_input("Enter C (µF): ", value=2.00, step=0.01)
    voltage = st.number_input("Enter V (V): ", value=12.0, step=0.1)

    # calculations
    energy1 = (0.5) * (capacitance * 10**-6) * (voltage**2)
    energy2 = (0.5) * (capacitance * 10**-6) * (6**2)

    st.subheader("Answers:")
    st.write("a) The energy stored is (µJ):")
    st.code(f"{convert(energy1, 'u'):.2f}")
    st.write("b) The energy stored is (µJ):")
    st.code(f"{convert(energy2, 'u'):.2f}")


def q3():
    st.header("Q3", divider="gray")
    st.write(
        "A small, rigid object carries positive and negative ...C... nC charges. It is oriented so that the positive charge has coordinates (-1.20 mm, ...y1... mm) and the negative charge is at the point (...x2... mm, -1.30 mm)."
    )

    st.subheader("Data:")
    charge = st.number_input("Enter C (nC): ", value=2.00, step=0.01)
    x1 = st.number_input("Enter x2 (mm): ", value=1.70, step=0.01)
    y1 = -1.3  # st.number_input("Enter y2 (mm): ", value=-1.30, step=0.01)
    x2 = -1.2  # st.number_input("Enter x1 (mm): ", value=-1.20, step=0.01)
    y2 = st.number_input("Enter y1 (mm): ", value=1.00, step=0.01)

    # calculations
    dipole_moment_x = charge * 10**-9 * (x2 - x1) * 10**-3
    dipole_moment_y = charge * 10**-9 * (y2 - y1) * 10**-3
    dipole_moment = np.array([dipole_moment_x, dipole_moment_y])

    field = np.array([7800, -4900])

    torque = np.cross(dipole_moment, field)

    pe = np.dot(np.negative(dipole_moment), field)
    pe_max_min = 2 * np.linalg.norm(pe)

    st.subheader("Answers:")

    st.write("a) The dipole moment is (i then j):")
    st.code(f"{dipole_moment_x}")
    st.code(f"{dipole_moment_y}")

    st.write("b) The torque is (in k direction):")
    st.code(f"{torque:.3e}")

    st.write("c) The potential energy is (J):")
    st.code(f"{pe:.3e}")

    st.write("d) The difference between max and min potential energy is (J):")
    st.code(f"{pe_max_min:.3e}")


def q4():
    st.header("Q4", divider="gray")
    st.write(
        "An electrical engineering student creates a circuit as shown in the figure. Find the following. (Assume C1 = ..... µF and C2 = ..... µF.)"
    )

    st.subheader("Data:")
    c_1 = st.number_input("Enter C1 (µF): ", value=33.00, step=0.01)
    c_2 = st.number_input("Enter C2 (µF): ", value=3.93, step=0.01)
    c_3 = 6.00
    v_tot = 9.00

    # calculations
    c_tot = 1 / ((1 / (c_2 + c_3)) + 2 * (1 / c_1))
    q_tot = c_tot * v_tot
    q_1 = q_tot
    q_2 = q_tot * (c_2 / (c_2 + c_3))
    q_3 = q_tot * (c_3 / (c_2 + c_3))
    v_1 = q_1 / c_1
    v_2 = q_2 / c_2
    v_3 = q_3 / c_3

    st.subheader("Answers:")

    st.write("a) The equivalent capacitance (µF):")
    st.code(f"{c_tot:.3f}")

    st.write("b) The individual charges (µC) (C1r, C1l, C2, 6µF) respectively:")
    st.code(f"{q_1:.3f}")
    st.code(f"{q_1:.3f}")
    st.code(f"{q_2:.3f}")
    st.code(f"{q_3:.3f}")

    st.write("c) The individual potential diff (V) (C1r, C1l, C2, 6µF) respectively:")
    st.code(f"{v_1:.3f}")
    st.code(f"{v_1:.3f}")
    st.code(f"{v_2:.3f}")
    st.code(f"{v_3:.3f}")


def q5():
    st.header("Q5", divider="gray")
    st.write(
        "A ...l...-m length of coaxial cable has an inner conductor that has a diameter of 2.58 mm and carries a charge of 8.10 µC. The surrounding conductor has an inner diameter of 7.27 mm and a charge of -8.10 µC. Assume the region between the conductors is air."
    )

    st.subheader("Data:")
    l = st.number_input("Enter cable length (m): ", value=65.0, step=0.1)
    inner_d = 2.58e-3
    outer_d = 7.27e-3
    q = 8.1e-6

    # calculations
    c = l / (2 * 9e9 * log(outer_d / inner_d, e))
    v = q / c

    st.subheader("Answers:")
    st.write("a) The equivalent capacitance (nF):")
    st.code(f"{convert(c, 'n'):.3f}")
    st.write("b) The potential diff (kV):")
    st.code(f"{convert(v, 'k'):.3f}")


if __name__ == "__main__":
    st.title("HW04 - Chapter 25")
    q1()
    q2()
    q3()
    q4()
    q5()

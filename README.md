# Cocotb Digital Designs

This repository contains various **digital design examples** written in **Verilog**, along with their corresponding **Cocotb Python testbenches** for simulation and verification. The designs are simulated using **Icarus Verilog** and waveform outputs are viewed with **GTKWave**.

---

## Repository Contents

- `verilog/` : Verilog HDL source files for digital circuits.
- `testbench/` : Cocotb Python testbenches to verify the Verilog designs.
- `waveforms/` : Sample waveform files (.vcd) generated from simulation (optional).

---

## Features

- Example digital circuits such as shift registers, counters, FSMs, etc.
- Python-based testbenches leveraging the Cocotb framework.
- Automated clock generation, stimulus, and assertions in testbenches.
- Compatible with open-source tools: Icarus Verilog and GTKWave.
- Easy to extend for custom designs and tests.

---

## Prerequisites

Make sure the following tools are installed:

- **Python 3.6+**
- **Cocotb** (`pip install cocotb`)
- **Icarus Verilog** (`iverilog`)
- **GTKWave**

---

## How to Run Simulations

1. Navigate to the project directory.

2. Compile the Verilog design:

```bash
iverilog -o sim.vvp verilog/your_design.v

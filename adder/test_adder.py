# test_adder.py
import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def adder_basic_test(dut):
    """Test adder with random inputs"""
    for _ in range(10):
        a = random.randint(0, 15)
        b = random.randint(0, 15)
        dut.a.value = a
        dut.b.value = b

        await Timer(2, units='ns')

        assert dut.sum.value == a + b, f"Adder result incorrect: {a} + {b} != {dut.sum.value}"


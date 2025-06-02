import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def two_bit_comp(dut):
    for a in range(4):
        for b in range(4):
            dut.a.value = a
            dut.b.value = b

            await Timer(1, units="ns")

            assert ((dut.a_greater.value == (a > b)) and
                    (dut.b_greater.value == (b > a)) and
                    (dut.equal.value == (a == b))), \
                f"Test failed for a={a}, b={b} → a_greater={dut.a_greater.value}, b_greater={dut.b_greater.value}, equal={dut.equal.value}"


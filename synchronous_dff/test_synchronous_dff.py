import cocotb
from cocotb.triggers import RisingEdge, Timer
from cocotb.clock import Clock

@cocotb.test()
async def test_synchronous_dff(dut):
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    dut.rst.value = 1
    dut.d.value = 0
    await Timer(15, units='ns')
    dut.rst.value = 0
    await Timer(10, units='ns')

    test_data = [0, 1, 1, 1, 0, 1, 1, 0]

    for val in test_data:
        dut.d.value = val
        await RisingEdge(dut.clk)
        await Timer(1, units='ns')
        assert dut.q.value == val, f"d={val}, but q={int(dut.q.value)}"
        dut._log.info(f"D={val}, Q={int(dut.q.value)}")



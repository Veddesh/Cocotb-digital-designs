import cocotb
from cocotb.triggers import Timer,RisingEdge
from cocotb.clock import Clock

@cocotb.test()

async def test_lfsr_4bit(dut):
    clock=Clock(dut.clk,10,units='ns')
    cocotb.start_soon(clock.start())

    dut.rst.value=1
    await Timer(10,units='ns')
    dut.rst.value=0
    await Timer(1000,units='ns')


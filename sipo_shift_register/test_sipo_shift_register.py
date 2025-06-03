import cocotb

from cocotb.triggers import Timer,RisingEdge
from cocotb.clock import Clock

@cocotb.test()

async def test_sipo_shift_register(dut):
    clock=Clock(dut.clk,10,units='ns')
    cocotb.start_soon(clock.start())
    dut.rst.value=1
    await Timer(10,units='ns')
    dut.rst.value=0
    await Timer(10,units='ns')
    test=[0,1,1,0,1,1,1,1,1,0,0,0,0]

    for i in test:
       dut.serial_in.value=i
       await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)


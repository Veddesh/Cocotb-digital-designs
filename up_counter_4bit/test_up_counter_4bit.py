import cocotb
from cocotb.triggers import Timer, RisingEdge
from cocotb.clock import Clock

@cocotb.test()

async def test_up_counter_4bit(dut):
   clock=Clock(dut.clk,10,units='ns')
   cocotb.start_soon(clock.start())


   dut.rst.value=0
   await Timer(15,units='ns')
   dut.rst.value=1
   await Timer(15,units='ns')
   dut.rst.value=0

   for i in range(16):
      assert dut.count.value==i
      await RisingEdge(dut.clk)
      await Timer(1,units='ns') 
   

   await Timer(45,units='ns')      



import cocotb

from cocotb.triggers import Timer

@cocotb.test()

async def test_four_one_mux(dut):
    for a in range(2):
      for b in range(2):
         for c in range(2):
           for d in range(2):
             for s in range(4):
               dut.a.value=a
               dut.b.value=b
               dut.c.value=c
               dut.d.value=d
               dut.s.value=s
               await Timer(10,units='ns')

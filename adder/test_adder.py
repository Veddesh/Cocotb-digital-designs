 
import cocotb

from cocotb.triggers import Timer

@cocotb.test()
async def adder_test(dut):
   for a in range(0,15):
       for b in range(0,15):
           dut.a.value=a
           dut.b.value=b
           await Timer(1,units='ps')
           c=a+b
           assert dut.sum.value==a+b, f"Test failed: for the inputs {a} and {b} the expected output is {c} but the value got is {dut.sum.value}"



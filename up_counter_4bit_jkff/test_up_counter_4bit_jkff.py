import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_up_counter_4bit_jkff(dut):
    

    
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    
    dut.reset.value = 1
    await RisingEdge(dut.clk)  # Wait one clock cycle
    await Timer(1,units='ns')    
    dut.reset.value = 0
    
    

    # Run for 20 clock cycles, printing the counter value
    for cycle in range(20):
        await RisingEdge(dut.clk)
        await Timer(1,units='ns')
        count = dut.q.value.integer
        dut._log.info(f"Cycle {cycle+1}: Counter value = {count:04b}")


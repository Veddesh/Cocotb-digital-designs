import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure


@cocotb.test()
async def test_logic_gates(dut):
    """Test AND, OR, and NOT gates"""

    # Test case 1: a = 0, b = 0
    dut.a.value = 0
    dut.b.value = 0
    await Timer(2, units='ns')
    assert dut.and_out.value == 0, "AND failed for 0,0"
    assert dut.or_out.value == 0, "OR failed for 0,0"
    assert dut.not_out.value == 1, "NOT failed for a=0"

    # Test case 2: a = 1, b = 0
    dut.a.value = 1
    dut.b.value = 0
    await Timer(2, units='ns')
    assert dut.and_out.value == 0, "AND failed for 1,0"
    assert dut.or_out.value == 1, "OR failed for 1,0"
    assert dut.not_out.value == 0, "NOT failed for a=1"

    # Test case 3: a = 1, b = 1
    dut.a.value = 1
    dut.b.value = 1
    await Timer(2, units='ns')
    assert dut.and_out.value == 1, "AND failed for 1,1"
    assert dut.or_out.value == 1, "OR failed for 1,1"
    assert dut.not_out.value == 0, "NOT failed for a=1"

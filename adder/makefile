# Makefile
TOPLEVEL_LANG = verilog
VERILOG_SOURCES = $(shell pwd)/adder.v
TOPLEVEL = adder
MODULE = test_adder

SIM = icarus
WAVES = 1

include $(shell cocotb-config --makefiles)/Makefile.sim

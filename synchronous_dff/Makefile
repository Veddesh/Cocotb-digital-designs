TOPLEVEL_LANG =verilog
VERILOG_SOURCES = $(shell pwd)/synchronous_dff.v
TOPLEVEL =synchronous_dff
MODULE = test_synchronous_dff

SIM = icarus
WAVES=1

include $(shell cocotb-config --makefiles)/Makefile.sim

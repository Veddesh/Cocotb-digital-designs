module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build/synchronous_dff.fst");
    $dumpvars(0, synchronous_dff);
end
endmodule

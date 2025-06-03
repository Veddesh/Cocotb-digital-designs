module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build/four_one_mux.fst");
    $dumpvars(0, four_one_mux);
end
endmodule

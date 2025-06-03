module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build/lfsr_4bit.fst");
    $dumpvars(0, lfsr_4bit);
end
endmodule

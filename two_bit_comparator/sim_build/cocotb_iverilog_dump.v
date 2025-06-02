module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build/two_bit_comparator.fst");
    $dumpvars(0, two_bit_comparator);
end
endmodule

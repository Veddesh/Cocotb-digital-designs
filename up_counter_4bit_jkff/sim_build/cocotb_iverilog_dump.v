module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build/up_counter_4bit_jkff.fst");
    $dumpvars(0, up_counter_4bit_jkff);
end
endmodule

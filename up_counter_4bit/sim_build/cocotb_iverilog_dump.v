module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build/up_counter_4bit.fst");
    $dumpvars(0, up_counter_4bit);
end
endmodule

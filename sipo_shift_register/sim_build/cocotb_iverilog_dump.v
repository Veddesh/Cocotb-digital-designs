module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build/sipo_shift_register.fst");
    $dumpvars(0, sipo_shift_register);
end
endmodule

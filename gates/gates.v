module gates (
    input  wire a,
    input  wire b,
    output wire and_out,
    output wire or_out,
    output wire not_out
);

    assign and_out = a & b;
    assign or_out  = a | b;
    assign not_out = ~a;

initial begin
        $dumpfile("dump.vcd");   // Name of the VCD dump file
        $dumpvars(0, gates);     // Dump all variables in this module and below
    end
endmodule

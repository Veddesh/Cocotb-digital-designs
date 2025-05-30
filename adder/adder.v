// adder.v
module adder (
    input  logic [3:0] a,
    input  logic [3:0] b,
    output logic [4:0] sum
);
    assign sum = a + b;
initial begin
        $dumpfile("dump.vcd");
        $dumpvars(0, adder);
    end

endmodule

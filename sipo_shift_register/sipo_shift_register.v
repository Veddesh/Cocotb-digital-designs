module dff (
    input clk,
    input rst,
    input d,
    output reg q
);

always @(posedge clk or posedge rst) begin
    if (rst)
        q <= 0;
    else
        q <= d;
end

endmodule

module sipo_shift_register (
    input clk,
    input rst,
    input serial_in,
    output [3:0] parallel_out
);

wire q0, q1, q2, q3;

dff dff0 (.clk(clk), .rst(rst), .d(serial_in), .q(q0));
dff dff1 (.clk(clk), .rst(rst), .d(q0), .q(q1));
dff dff2 (.clk(clk), .rst(rst), .d(q1), .q(q2));
dff dff3 (.clk(clk), .rst(rst), .d(q2), .q(q3));

assign parallel_out = {q3, q2, q1, q0};

endmodule

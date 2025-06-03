module dff4(
    input clk,
    input rst,
    input d,
    output reg q
);

always @(posedge clk or posedge rst) begin
    if (rst)
        q <= 1'b1;
    else
        q <= d;
end

endmodule

module lfsr_4bit(
    input clk,
    input rst,
    output [3:0] q
);

wire d0, d1, d2, d3; 
wire q0, q1, q2, q3;  

assign d3=q2;
assign d2=q1;
assign d1=q0;
assign d0=q3^q2;

dff4 dff0(.clk(clk), .rst(rst), .d(d0), .q(q0));
dff4 dff1(.clk(clk), .rst(rst), .d(d1), .q(q1));
dff4 dff2(.clk(clk), .rst(rst), .d(d2), .q(q2));
dff4 dff3(.clk(clk), .rst(rst), .d(d3), .q(q3));

assign q = {q3, q2, q1, q0};
endmodule


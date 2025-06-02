module two_bit_comparator(
    input wire [1:0] a,
    input wire [1:0] b,
    output reg a_greater,
    output reg b_greater,
    output reg equal
);

always @(*) begin
    if (a == b) begin
        a_greater = 0;
        b_greater = 0;
        equal = 1;
    end else if (a > b) begin
        a_greater = 1;
        b_greater = 0;
        equal = 0;
    end else begin
        a_greater = 0;
        b_greater = 1;
        equal = 0;
    end
end

endmodule


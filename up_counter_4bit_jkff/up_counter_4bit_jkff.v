 module jk_ff(
    input clk,
    input reset,
    input j,
    input k,
    output reg q
);
    always @(posedge clk or posedge reset) begin
        if (reset)
            q <= 0;
        else begin
            case ({j,k})
                2'b00: q <= q;      // hold state
                2'b01: q <= 0;      // reset
                2'b10: q <= 1;      // set
                2'b11: q <= ~q;     // toggle
            endcase
        end
    end
endmodule


module up_counter_4bit_jkff(
    input clk,
    input reset,
    output [3:0] q
);
    wire j0, k0, j1, k1, j2, k2, j3, k3;

    assign j0 = 1'b1;               // LSB toggles every clock
    assign k0 = 1'b1;

    assign j1 = q[0];               // toggle when Q0 = 1
    assign k1 = q[0];

    assign j2 = q[0] & q[1];        // toggle when Q0 & Q1 = 1
    assign k2 = q[0] & q[1];

    assign j3 = q[0] & q[1] & q[2]; // toggle when Q0 & Q1 & Q2 = 1
    assign k3 = q[0] & q[1] & q[2];

    jk_ff ff0(.clk(clk), .reset(reset), .j(j0), .k(k0), .q(q[0]));
    jk_ff ff1(.clk(clk), .reset(reset), .j(j1), .k(k1), .q(q[1]));
    jk_ff ff2(.clk(clk), .reset(reset), .j(j2), .k(k2), .q(q[2]));
    jk_ff ff3(.clk(clk), .reset(reset), .j(j3), .k(k3), .q(q[3]));
endmodule


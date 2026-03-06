'default_nettype none

module perc (
    input wire [7:0]    surrounding_percs,
    input wire          init_state;
    input wire          clk,
    input wire          reset_n,
    output wire         state,
);

    wire [7:0] weight1;
    wire [7:0] weight2;
    wire [8:0] sum;

    //weighted sum (changed to 4 so i don't have to deal with decimals)]

    assign weight1 = (4 * surrounding_percs[0]) + (4 * surrounding_percs[1]) + (4 * surrounding_percs[2]) + (4 * surrounding_percs[3]);
    assign weight2 = (surrounding_percs[4] + surrounding_percs[5] + surrounding_percs[6] + surrounding_percs[7]);

    assign sum = weight1 + weight2;

    //activation function and flip flop??

    wire [7:0] next_state;

    assign next_state = (!(sum < 4) || (sum >= 4 && sum <= 10) || !(sum > 10));

    always @(posedge clk) begin

        if (reset_n) begin
            state <= init_state;
        end else begin
            state <= next_state;
        end
    end



endmodule
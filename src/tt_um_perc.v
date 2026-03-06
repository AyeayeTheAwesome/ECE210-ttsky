`default_nettype none

module tt_um_perc (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

  // All output pins must be assigned. If not used, assign to 0.
  assign uio_out[6:0] = 0;
  assign uio_oe  = 8'b01110001;

  // List all unused inputs to prevent warnings
  wire _unused = &{ena, 1'b0};

  perc perc0 (.surrounding_percs({uo_out[1], uo_out[3], 1'b0, 1'b0, uo_out[4], 1'b0, 1'b0, 1'b0}), .init_state(ui_in[0]), .clk(clk), .reset_n(rst_n), .state(uo_out[0]));
  perc perc1 (.surrounding_percs({uo_out[0], uo_out[2], uo_out[4], 1'b0, uo_out[3], uo_out[5], 1'b0, 1'b0}), .init_state(ui_in[0]), .clk(clk), .reset_n(rst_n), .state(uo_out[1]));
  perc perc2 (.surrounding_percs({uo_out[1], uo_out[5], 1'b0, 1'b0, uo_out[4], 1'b0, 1'b0, 1'b0}), .init_state(ui_in[0]), .clk(clk), .reset_n(rst_n), .state(uo_out[2]));
  perc perc3 (.surrounding_percs({uo_out[0], uo_out[4], uo_out[6], 1'b0, uo_out[1], uo_out[7], 1'b0, 1'b0}), .init_state(ui_in[0]), .clk(clk), .reset_n(rst_n), .state(uo_out[3]));
  perc perc4 (.surrounding_percs({uo_out[1], uo_out[3], uo_out[5], uo_out[7], uo_out[0], uo_out[3], uo_out[6], uio_out[7]}), .init_state(ui_in[0]), .clk(clk), .reset_n(rst_n), .state(uo_out[4]));
  perc perc5 (.surrounding_percs({uo_out[2], uo_out[4], uio_out[7], 1'b0, uo_out[1], uo_out[7], 1'b0, 1'b0}), .init_state(ui_in[0]), .clk(clk), .reset_n(rst_n), .state(uo_out[5]));
  perc perc6 (.surrounding_percs({uo_out[3], uo_out[7], 1'b0, 1'b0, uo_out[4], 1'b0, 1'b0, 1'b0}), .init_state(ui_in[0]), .clk(clk), .reset_n(rst_n), .state(uo_out[6]));
  perc perc7 (.surrounding_percs({uo_out[4], uo_out[6], uio_out[7], 1'b0, uo_out[3], uo_out[5], 1'b0, 1'b0}), .init_state(ui_in[0]), .clk(clk), .reset_n(rst_n), .state(uo_out[7]));
  perc perc8 (.surrounding_percs({uo_out[5], uo_out[7], 1'b0, 1'b0, uo_out[4], 1'b0, 1'b0, 1'b0}), .init_state(uio_in[0]), .clk(clk), .reset_n(rst_n), .state(uio_out[7]));


endmodule

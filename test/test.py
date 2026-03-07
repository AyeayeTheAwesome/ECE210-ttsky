# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    clock = Clock(dut.clk, 1, units="ns")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0  #i flipped the reset lol #ok nvm changed it back
    await ClockCycles(dut.clk, 10)
    #dut.rst_n.value = 1   #need input values set before reset goes low

    dut._log.info("Test project behavior")

    # Set the input values you want to test
    dut.ui_in.value = int("10000010", 2)  #turns binary into int
    dut.uio_in.value = int("10000000", 2)  #9th perceptron cell set

    dut.rst_n.value = 1  #set perceptron in motion
    dut.uio_in.value = 1; #allow initial state to be set

    await ClockCycles(dut.clk, 1)

    dut._log.info("Init value: " + str(dut.ui_in.value))
    dut._log.info("| " + bin(dut.ui_in.value)[2:3] + " | " + bin(dut.ui_in.value)[3:4] + " | " + bin(dut.ui_in.value)[4:5] + " |")
    dut._log.info("| " + bin(dut.ui_in.value)[5:6] + " | " + bin(dut.ui_in.value)[6:7] + " | " + bin(dut.ui_in.value)[7:8] + " |")
    dut._log.info("| " + bin(dut.ui_in.value)[8:9] + " | " + bin(dut.ui_in.value)[9:10] + " | " + bin(dut.uio_in.value)[2:3] + " |")

    for i in range(5): #loop it a bunch
    
        # Wait for one clock cycle to see the output values
        await ClockCycles(dut.clk, 1)
        dut.uio_in.value = 0; #allow game to play


        # start printing out perceptron grid
        dut._log.info("current out: " + bin(dut.uo_out.value))

        dut._log.info("| " + bin(dut.uo_out.value)[2:3] + " | " + bin(dut.uo_out.value)[3:4] + " | " + bin(dut.uo_out.value)[4:5] + " |")
        dut._log.info("| " + bin(dut.uo_out.value)[5:6] + " | " + bin(dut.uo_out.value)[6:7] + " | " + bin(dut.uo_out.value)[7:8] + " |")
        dut._log.info("| " + bin(dut.uo_out.value)[8:9] + " | " + bin(dut.uo_out.value)[9:10] + " | " + bin(dut.uio_out.value)[9:10] + " |")

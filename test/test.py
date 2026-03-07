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
    dut.uio_in.value = int("00000011", 2)  #9th perceptron cell set, enable init state to be set

    dut.rst_n.value = 1  #set perceptron in motion
    #dut.uio_in.value = 1; #allow initial state to be set

    await ClockCycles(dut.clk, 1)
    dut.uio_in.value = int("00000001", 2)  #alr set


    a = bin(dut.ui_in.value)
    b = bin(dut.uio_in.value)
    x = format(int(dut.ui_in.value), '08b')
    y = format(int(dut.uio_in.value), '08b')

    dut._log.info("Init value: " + str(dut.uio_in.value)[7] + str(dut.ui_in.value))
    dut._log.info("| " + x[7] + " | " + x[6] + " | " + x[5] + " |")
    dut._log.info("| " + x[4] + " | " + x[3] + " | " + x[2] + " |")
    dut._log.info("| " + x[1] + " | " + x[0] + " | " + y[7] + " |")

    for i in range(5): #loop it a bunch
    
        # Wait for one clock cycle to see the output values
        await ClockCycles(dut.clk, 1)

        # start printing out perceptron grid
        dut._log.info("current out: " + bin(dut.uo_out.value) + bin(dut.uo_out.value))

        #dut._log.info("| " + bin(dut.uo_out.value)[2:3] + " | " + bin(dut.uo_out.value)[3:4] + " | " + bin(dut.uo_out.value)[4:5] + " |")
        #dut._log.info("| " + bin(dut.uo_out.value)[5:6] + " | " + bin(dut.uo_out.value)[6:7] + " | " + bin(dut.uo_out.value)[7:8] + " |")
        #dut._log.info("| " + bin(dut.uo_out.value)[8:9] + " | " + bin(dut.uo_out.value)[9:10] + " | " + bin(dut.uio_out.value)[9:10] + " |")

        x = format(int(dut.uo_out.value), '08b')
        y = format(int(dut.uio_out.value), '08b')
        dut._log.info("| " + x[7] + " | " + x[6] + " | " + x[5] + " |")
        dut._log.info("| " + x[4] + " | " + x[3] + " | " + x[2] + " |")
        dut._log.info("| " + x[1] + " | " + x[0] + " | " + y[0] + " |")

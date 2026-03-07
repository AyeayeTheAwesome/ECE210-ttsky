<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

We use a basic model of a perceptron, where it takes in inputs from the surrounding perceptrons (4 orthogonal, 4 diagonal, some values are
zeroed out for perceptrons on the edge of the grid). These inputs are multiplied by the weights inside perc.v, where orthogonal perceptrons
have more effect on the perceptron's next state than diagonal ones. Once this weighted sum is calculated, if the weighted sum is within
the perceptron's "goldilocks zone" (between 4 and 10 for these perceptrons), the perceptron will be 'alive' in the next state! Otherwise,
(to simulate loneliness or overcrowding) the perceptron will be 'dead' next round. After reset is done, a bit is used to hold the perceptron's
in an init hold state, where the initial states can be passed through the ui_in channels. After the uio_in bit goes low, the perceptrons can
start taking in inputs and changing state, simulating a version of Conways Game of Life!

## How to test

In the test.py cocotb ile in the test directory, edit the ui_in binary value on line 28 as well as the rightmost least-significant
bit of uio_in on line 29 to set the initial value of the 9 perceptrons. Edit the for loop value on line 48 in order to see more
or less iterations of the game.

## External hardware

You can link up a 3x3 led matrix if you want to see the Game of Life in action!

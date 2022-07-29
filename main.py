import sys
from Brain import Brain  # shows error but is fine; once cython takes over, Brain will be pulled from Brain.c
import numpy as np
from time import sleep
from pprint import pprint


class Mode:
    encoding = 1
    decoding = 2


def show_grid():
    grid = np.asarray(b.grid_view)
    print()
    for item in grid:
        print(item)
    print()


def translate_data(data, possible_values, mode):
    if mode == Mode.encoding:
        temp = []
        for item in data:
            for value in possible_values:
                if item == value:
                    temp.append(1)
                else:
                    temp.append(0)
        return temp
    elif mode == Mode.decoding:
        temp = []
        for i in range(0, len(data), len(possible_values)):
            temp2 = []
            for j in range(len(possible_values)):
                if data[i + j] == 1:
                    temp2.append(possible_values[j])
            if len(temp2) == 1:
                temp.append(temp2[0])
            elif len(temp2) == 0:
                temp.append("N/A")
            else:
                temp.append("&".join(temp2))
        return temp
    else:
        print(f"Invalid Mode! {mode}")
        return


def manual_loop():
    while True:
        outVals = b.loop_no_while()
        if outVals is not None:
            return outVals
        # sleep(1)
        # input("Press Enter to continue...")


numInputs = 4
numOutputs = 2

allInData = [[0, 0], [0, 1], [1, 0], [1, 1]]
possibleValues = [0, 1]

b = Brain((10, 10), num_inputs=numInputs, num_outputs=numOutputs)
b.populate()

print(f"{b.get_number_neurons()} Neurons in brain")
ends = [[str(f).split(":")[0] for f in np.asarray(b.inputs)], [str(f).split(":")[0] for f in np.asarray(b.outputs)]]
print(f"ENDS: {ends} \n")

# b.grow_neurons()

show_grid()

# b.loop()

# show_grid()

for i in range(len(allInData)):
    for j in range(100):
        inValues = translate_data(data=allInData[i], possible_values=possibleValues, mode=Mode.encoding)
        b.set_inputs(inValues)

        outValues = manual_loop()
        outData = translate_data(data=outValues, possible_values=possibleValues, mode=Mode.decoding)

    print(f"IN: {allInData[i]}")
    print(f"OUT: {outData}\n")

# show_grid()

# manual_loop()

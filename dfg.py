from helper import WireNode, InputNode, GateNode



# generate circuit graph from net
def Simulate(Inputs, Outputs, CircuitVar, input_array, expected_output_array, outputs_file_name):
    InputNodes = []
    # OutputNodes = []
    CircuitNodes = {}
    Wires = {}

    for input in Inputs:
        temp_wire = WireNode(wire_id=input) # generate a wire that is connected to input
        Wires[input] = temp_wire            # add that wire in Wires dictionary
        input_node = InputNode(wire=temp_wire) # create input Node  
        InputNodes.append(input_node)    

    for gate in CircuitVar:   # loop over the main circuit specification
        temp = gate.split()
        gate_id = temp[0]       # gate_id - x1/x2/x3 etc.
        gate_type = temp[1]     # gate_type - or_2/and_2/not etc
        input1_wire_id = temp[2]
        if(gate_type == 'not'):
            input2_wire_id = None
            output_wire_id = temp[3]
        else:
            input2_wire_id = temp[3]
            output_wire_id = temp[4]

        if(output_wire_id in Wires.keys()):                 # check if this wire is already create
            pass                                             # if not then create it
        else:
            temp_wire = WireNode(wire_id=output_wire_id)
            Wires[output_wire_id] = temp_wire

        # create gate node - inputs wires are passed as wire id but output wire node instance is passed
        gate_node = GateNode(gate_id, gate_type, input1_wire_id, input2_wire_id, Wires[output_wire_id])

        CircuitNodes[gate_id] = gate_node

        if(input1_wire_id in Wires.keys()):                     # check if this wire is already create
            Wires[input1_wire_id].add_next(gate_node)           # if not then create it
        else: 
            temp_wire = WireNode(wire_id=input1_wire_id)
            Wires[input1_wire_id] = temp_wire
            temp_wire.add_next(gate_node)

        if(input2_wire_id and input2_wire_id in Wires.keys()):  # check if this wire is already create
            Wires[input2_wire_id].add_next(gate_node)           # if not then create it
        elif(input2_wire_id): 
            temp_wire = WireNode(wire_id=input2_wire_id)
            Wires[input2_wire_id] = temp_wire
            temp_wire.add_next(gate_node)


    with open(outputs_file_name, 'w') as output_file:
        output_file.write("INPUT            EXPECTED            ACTUAL\n\n")
        for idx1, input_state in enumerate(input_array):
            input_vector = [int(char) for char in input_state]
            expected_output_vector = [int(char) for char in expected_output_array[idx1]]
            for idx2, input_node in enumerate(InputNodes):
                input_node.drive(input_vector[idx2])
            
            actual_output_vector = []
            actual_output_string = ""
            for idx3, output_id in enumerate(Outputs):
                actual_output_string += str(Wires[output_id].val)
                actual_output_vector.append(Wires[output_id].val)
            # print('input vector', input_vector)
            # print('expected output', expected_output_vector)
            # print('actual output', actual_output_vector)
         
            # print("------------")

            output_file.write(input_state)
            output_file.write("         ")
            output_file.write(expected_output_array[idx1])
            output_file.write("         ")
            output_file.write(actual_output_string)
            output_file.write('\n')

        s = "---------- check " + outputs_file_name + " for results ----------"
        print(s)
     




   # for key in Wires.keys():
            #     print(Wires[key].Id, Wires[key].val)
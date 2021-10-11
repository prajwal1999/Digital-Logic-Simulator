import sys
import getopt

from dfg import Simulate    


if __name__=="__main__":
    net_file_name = None
    inputs_file_name = None
    outputs_file_name = 'main.log'
    input_array = []
    expected_output_array = []
    Inputs = []
    Outputs = []
    CircuitVar = []
    argv = sys.argv[1:]
    opts = None

    if(argv[0] == '-h' or argv[0] == '--help'):
        print('-f <circuit_file>')
        print('-i <inputs and expected output file>')
        print('-o <output file to store simulation result>')

    try:
        opts, args = getopt.getopt(argv, "f:i:o")
        if(len(opts) == 0):
            print("No arguments given")
            print("type -h or --help to get options")
    except:
        pass

    # read net file
    if(opts):
        for opt, arg in opts:
            if opt in ['-f']: net_file_name = arg
            if opt in ['-i']: inputs_file_name = arg
            if opt in ['-o']: outputs_file_name = arg
    
    if not net_file_name: print("circuit file not provided")
    if not inputs_file_name: print("inputs file not provided")


    if(inputs_file_name):
        with open(inputs_file_name) as input_file:
            input_file_content = input_file.readlines()
            for input_line in input_file_content:
                s = input_line.split('\n')[0].split(" ")
                input_array.append(s[0])
                expected_output_array.append(s[1])

    if(net_file_name):
        with open(net_file_name) as net_file:
            net_file_content = net_file.readlines()
            store_circuit = False
            for net_line in net_file_content:
                if(net_line.find('!') > -1): net_line = net_line.split('!')[0]
                if(net_line.find('.inputs') == 0):
                    Inputs = net_line.split(".inputs")[1].split('\n')[0].split()
                
                elif(net_line.find('.outputs') == 0):
                    Outputs = net_line.split(".outputs")[1].split('\n')[0].split()

                elif(net_line.find('.end circuit') == 0): store_circuit = False

                if(store_circuit):
                    temp = net_line.split('\n')[0]
                    if(temp != ''): CircuitVar.append(temp)

                elif(net_line.find('.circuit') == 0): store_circuit = True


    # print(Inputs)
    # print(Outputs)
    # print(CircuitVar)
    # check if in any connection there is wire crossover

    # find DFG for circuit
    Simulate(Inputs, Outputs, CircuitVar, input_array, expected_output_array, outputs_file_name)
from gates import AND_2, OR_2, NAND_2, NOR_2, NOT, XNOR_2, XOR_2

class InputNode():
    def __init__(self, wire):
        self.wire = wire
        self.val = None

    def drive(self, val):
        self.val = val
        # print("input node drived with id - ", self.wire.Id, 'value - ', self.val)
        self.wire.drive(val)
        return

class WireNode():
    def __init__(self, wire_id):
        self.Id = wire_id
        self.val = 0
        self.next = []
    
    def add_next(self,nxt):
        if(nxt not in self.next): 
            self.next.append(nxt)
    
    def drive(self, val):
        self.val = val
        # print("wire node drived with id - ", self.Id, 'value - ', self.val)
        if(len(self.next) == 0):
            return
        for next_gate in self.next:             # drive its next
            next_gate.calc(self.Id, self.val)
        return


class GateNode():
    def __init__(self, gate_id, type, input1, input2, output):
        self.Id = gate_id
        self.input1_wire = input1
        self.input2_wire = input2
        self.output_wire = output
        self.output_val = None
        self.input1_val = 0
        self.input2_val = 0
        self.type = type

    def calc(self, in_wire_id, in_val):
        if(in_wire_id == self.input1_wire): self.input1_val = in_val
        if(in_wire_id == self.input2_wire): self.input2_val = in_val

        if(self.type == 'and_2'): 
            t = AND_2()
            t.drive(self.input1_val, self.input2_val)
            self.output_val = t.output
        if(self.type == 'or_2'): 
            t = OR_2()
            t.drive(self.input1_val, self.input2_val)
            self.output_val = t.output
        if(self.type == 'not'): 
            t = NOT()
            t.drive(self.input1_val)
            self.output_val = t.output
        
        # print('calc done on ', self.type, 'output wire id - ', self.output_wire.Id)
        self.output_wire.drive(self.output_val)
        return

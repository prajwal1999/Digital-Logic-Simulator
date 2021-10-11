class AND_2():
    def __init__(self):
        self.input1 = 0
        self.input2 = 0
        self.output = 0

    def drive(self, input_1, input_2):
        self.input1 = input_1
        self.input2 = input_2
        if(input_1==1 and input_2==1): self.output = 1
        else: self.output = 0

class NAND_2():
    def __init__(self):
        self.input1 = 0
        self.input2 = 0
        self.output = 1

    def drive(self, input_1, input_2):
        self.input1 = input_1
        self.input2 = input_2
        if(input_1==1 and input_2==1): self.output = 0
        else: self.output = 1

class OR_2():
    def __init__(self):
        self.input1 = 0
        self.input2 = 0
        self.output = 0

    def drive(self, input_1, input_2):
        self.input1 = input_1
        self.input2 = input_2
        if(input_1==0 and input_2==0): self.output = 0
        else: self.output = 1


class NOR_2():
    def __init__(self):
        self.input1 = 0
        self.input2 = 0
        self.output = 1

    def drive(self, input_1, input_2):
        self.input1 = input_1
        self.input2 = input_2
        if(input_1==0 and input_2==0): self.output = 1
        else: self.output = 0


class XOR_2():
    def __init__(self):
        self.input1 = 0
        self.input2 = 0
        self.output = 0

    def drive(self, input_1, input_2):
        self.input1 = input_1
        self.input2 = input_2
        if(input_1 == input_2): self.output = 0
        else: self.output = 1

class XNOR_2():
    def __init__(self):
        self.input1 = 0
        self.input2 = 0
        self.output = 1

    def drive(self, input_1, input_2):
        self.input1 = input_1
        self.input2 = input_2
        if(input_1 == input_2): self.output = 1
        else: self.output = 0

class NOT():
    def __init__(self):
        self.input = 0
        self.output = 1

    def drive(self, input_1):
        self.input = input_1
        if(input_1 == 0): self.output = 1
        else: self.output = 0
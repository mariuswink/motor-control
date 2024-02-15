class Block():
    def __init__(self, name):
        print("Created Block: ", name)
        self.name = name
        self.inputs = []
        self.outputs = []

    def print(self):
        print("[ ", end="")
        for input in self.inputs:
            print(input.name, end=" ")
        print("]", end="")
        print("->", self.name, "->", end=" ")
        print("[ ", end="")
        for output in self.outputs:
            print(output.name , end=" ")
        print("]")

    def connectInput(self, input: object):
        if self.isConnectedTo(input):
            return
        self.inputs.append(input)

    def connectOutput(self, output: object):
        if self.isConnectedTo(output):
            return
        self.outputs.append(output)
        output.connectInput(self)

    def isConnectedTo(self, node: object) -> bool:
        return (node in self.outputs or node in self.inputs)

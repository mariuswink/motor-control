class System:
    def __init__(self, name, blocks):
        print("System: ", name)
        self.blocks = blocks
        for block in blocks:
            block.print()
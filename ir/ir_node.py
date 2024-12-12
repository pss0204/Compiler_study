class IRNode:
    def __init__(self, op_type, inputs, params=None):
        self.op_type = op_type
        self.inputs = inputs
        self.params = params or {}
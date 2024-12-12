from ir.ir_node import IRNode
import numpy as np

def build_toy_model_ir():
    input_node = IRNode(op_type='Input', inputs=[], params={'shape': (2,)})
    linear_node = IRNode(op_type='Linear', inputs=[input_node], params={'W': np.random.randn(1, 2), 'b': np.random.randn(1)})
    relu_node = IRNode(op_type='Relu', inputs=[linear_node])
    return [input_node, linear_node, relu_node]
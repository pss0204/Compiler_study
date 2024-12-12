from ir.ir_node import IRNode
import numpy as np

def build_toy_model_ir(model):
    ir_nodes = []
    input_node = IRNode(
        op_type='Input',
        inputs=[], 
        params={'shape': (2,)}
    )
    ir_nodes.append(input_node)
    
    previous_node = input_node
    for layer in model.layers:
        if layer['type'] == 'Linear':
            linear_node = IRNode(
                op_type='Linear',
                inputs=[previous_node],
                params={'W': layer['params']['W'], 'b': layer['params']['b']}
            )
            ir_nodes.append(linear_node)
            previous_node = linear_node
        elif layer['type'] == 'Relu':
            relu_node = IRNode(
                op_type='Relu',
                inputs=[previous_node]
            )
            ir_nodes.append(relu_node)
            previous_node = relu_node
        # 다른 레이어 타입 추가 가능
    return ir_nodes
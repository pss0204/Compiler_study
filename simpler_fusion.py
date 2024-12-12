from ir.ir_node import IRNode

def fuse_linear_relu(ir_nodes):
    fused_ir = []
    skip = False
    for i in range(len(ir_nodes)):
        if skip:
            skip = False
            continue
        if ir_nodes[i].op_type == 'Linear' and i+1 < len(ir_nodes) and ir_nodes[i+1].op_type == 'Relu':
            fused_node = IRNode(op_type='LinearRelu', inputs=ir_nodes[i].inputs, params=ir_nodes[i].params)
            fused_ir.append(fused_node)
            skip = True
        else:
            fused_ir.append(ir_nodes[i])
    return fused_ir
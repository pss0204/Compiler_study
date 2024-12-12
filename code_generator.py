def generate_numpy_code(ir_nodes):
    code_lines = []
    for node in ir_nodes:
        if node.op_type == 'Input':
            code_lines.append("# 입력 받기")
        elif node.op_type == 'Linear':
            code_lines.append(f"output_linear = np.dot(W, input_vec) + b")
        elif node.op_type == 'Relu':
            code_lines.append("output_relu = np.maximum(output_linear, 0)")
        elif node.op_type == 'LinearRelu':
            code_lines.append("output = np.maximum(np.dot(W, input_vec) + b, 0)")
    code_lines.append("return output_relu if 'output_relu' in locals() else output")
    return "\n".join(code_lines)
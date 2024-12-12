from frontend import build_toy_model_ir
from simpler_fusion import fuse_linear_relu
from code_generator import generate_numpy_code
from toy_model import ToyModel
import numpy as np
import textwrap

model = ToyModel()# 모델 생성

# IR 생성s
ir = build_toy_model_ir(model)

# 최적화 적용
optimized_ir = fuse_linear_relu(ir)

# 코드 생성
generated_code = generate_numpy_code(optimized_ir)
exec_globals = {
    "np": np, 
    "W": optimized_ir[1].params['W'], 
    "b": optimized_ir[1].params['b']
}
indented_code = textwrap.indent(generated_code, "    ")
# 컴파일된 함수 정의
exec(f"""
def compiled_model(input_vec):
    {indented_code}
    print("W:", W)
    print("b:", b)
    print("output before relu:", np.dot(W, input_vec) + b)
    return output
""", exec_globals)

compiled_model = exec_globals['compiled_model']

# 테스트
input_vec = np.array([1.0, -1.0])
output = compiled_model(input_vec)
print("출력:", output)
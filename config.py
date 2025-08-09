"""
配置模块 - 管理三段论验证的全局设置
"""

from enum import Enum

class InterpretationType(Enum):
    """解释类型枚举"""
    ARISTOTELIAN = "aristotelian"  # 亚里士多德解释
    BOOLEAN = "boolean"           # 布尔解释

# 全局配置变量
INTERPRETATION = InterpretationType.BOOLEAN

def set_interpretation(interpretation_type):
    """设置解释类型"""
    global INTERPRETATION
    if isinstance(interpretation_type, InterpretationType):
        INTERPRETATION = interpretation_type
    else:
        raise ValueError(f"无效的解释类型: {interpretation_type}")

def get_interpretation():
    """获取当前解释类型"""
    return INTERPRETATION

def is_aristotelian():
    """检查是否使用亚里士多德解释"""
    return INTERPRETATION == InterpretationType.ARISTOTELIAN

def is_boolean():
    """检查是否使用布尔解释"""
    return INTERPRETATION == InterpretationType.BOOLEAN

def get_interpretation_name():
    """获取解释类型的中文名称"""
    if INTERPRETATION == InterpretationType.ARISTOTELIAN:
        return "亚里士多德解释"
    else:
        return "布尔解释"

# 示例用法
if __name__ == "__main__":
    print(f"当前解释: {get_interpretation_name()}")

    # 切换回亚里士多德解释
    set_interpretation(InterpretationType.ARISTOTELIAN)
    print(f"切换后解释: {get_interpretation_name()}")

    # 切换到布尔解释
    set_interpretation(InterpretationType.BOOLEAN)
    print(f"切换后解释: {get_interpretation_name()}")

#!/usr/bin/env python3
"""
测试配置模块的功能
"""

from config import (
    set_interpretation, get_interpretation, is_aristotelian, is_boolean,
    InterpretationType, get_interpretation_name
)

def test_config():
    """测试配置功能"""
    print("=== 测试配置模块 ===")

    # 测试默认设置
    print(f"默认解释: {get_interpretation_name()}")
    assert is_aristotelian() == False
    assert is_boolean() == True

    # 测试切换到亚里士多德解释
    set_interpretation(InterpretationType.ARISTOTELIAN)
    print(f"切换后解释: {get_interpretation_name()}")
    assert is_aristotelian() == True
    assert is_boolean() == False

    # 测试切换回布尔解释
    set_interpretation(InterpretationType.BOOLEAN)
    print(f"再次切换后解释: {get_interpretation_name()}")
    assert is_aristotelian() == False
    assert is_boolean() == True

    # 测试错误输入
    try:
        set_interpretation("invalid")
        assert False, "应该抛出异常"
    except ValueError as e:
        print(f"正确捕获错误: {e}")

    print("✓ 所有测试通过!")

if __name__ == "__main__":
    test_config()

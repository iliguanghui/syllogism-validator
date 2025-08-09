#!/usr/bin/env python3
"""
演示亚里士多德解释和布尔解释的差异
"""

from syllogism import Syllogism, PropositionType
from config import set_interpretation, InterpretationType, get_interpretation_name
from validate_all import generate_all_syllogisms
from validation_rules import is_valid_syllogism

def compare_interpretations():
    """比较两种解释的差异"""
    print("=== 亚里士多德解释 vs 布尔解释 ===\n")

    # 生成所有三段论
    all_syllogisms = generate_all_syllogisms()

    # 分别用两种解释验证
    aristotelian_valid = get_valid_syllogisms(InterpretationType.ARISTOTELIAN, all_syllogisms)
    boolean_valid = get_valid_syllogisms(InterpretationType.BOOLEAN, all_syllogisms)

    print(f"亚里士多德解释有效三段论数量: {len(aristotelian_valid)}")
    print(f"布尔解释有效三段论数量: {len(boolean_valid)}")

    # 找出差异
    only_aristotelian = [syl for syl in aristotelian_valid if syl.get_figure_and_mood() not in [s.get_figure_and_mood() for s in boolean_valid]]
    only_boolean = [syl for syl in boolean_valid if syl.get_figure_and_mood() not in [s.get_figure_and_mood() for s in aristotelian_valid]]

    print(f"\n仅在亚里士多德解释中有效的三段论: {len(only_aristotelian)}")
    for syl in only_aristotelian:
        print(f"  {syl.get_figure_and_mood()}")

    print(f"\n仅在布尔解释中有效的三段论: {len(only_boolean)}")
    for syl in only_boolean:
        print(f"  {syl.get_figure_and_mood()}")

    # 展示具体差异示例
    if only_aristotelian:
        print(f"\n=== 差异示例 ===")
        print("以下三段论在亚里士多德解释中有效，但在布尔解释中无效:")
        for i, syl in enumerate(only_aristotelian[:3], 1):  # 只显示前3个
            print(f"\n示例 {i}: {syl.get_figure_and_mood()}")
            print(syl)
            print("原因: 亚里士多德解释假设存在性，允许从全称前提推出特称结论")

def get_valid_syllogisms(interpretation_type, all_syllogisms):
    """获取在指定解释下有效的三段论"""
    set_interpretation(interpretation_type)

    valid_syllogisms = []
    for syl in all_syllogisms:
        if is_valid_syllogism(syl):
            valid_syllogisms.append(syl)

    return valid_syllogisms

def show_specific_examples():
    """展示具体的三段论示例"""
    print("\n=== 具体示例分析 ===")

    # 创建一个可能存在差异的三段论示例
    # AAI-1: 所有M是P，所有S是M，因此某些S是P
    example = Syllogism(PropositionType.A, PropositionType.A, PropositionType.I, 0, 1)

    print(f"示例三段论: {example.get_figure_and_mood()}")
    print(example)

    # 在两种解释下检查
    for interp_type in [InterpretationType.ARISTOTELIAN, InterpretationType.BOOLEAN]:
        set_interpretation(interp_type)
        is_valid = is_valid_syllogism(example)
        print(f"\n在{get_interpretation_name()}下: {'有效' if is_valid else '无效'}")
        if not is_valid and interp_type == InterpretationType.BOOLEAN:
            print("  原因: 布尔解释不允许从两个全称前提推出特称结论")

if __name__ == "__main__":
    compare_interpretations()
    show_specific_examples()

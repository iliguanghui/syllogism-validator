#!/usr/bin/env python3
"""
测试验证规则模块的功能
"""

from syllogism import Syllogism, PropositionType
from config import set_interpretation, InterpretationType
from validation_rules import (
    middle_term_distributed_once,
    no_illicit_distribution,
    no_two_negative_premises,
    negative_premise_negative_conclusion,
    existential_import_rule,
    get_all_validation_rules,
    is_valid_syllogism
)

def test_individual_rules():
    """测试各个规则函数"""
    print("=== 测试各个规则函数 ===")

    # 测试中项周延规则
    print("\n1. 测试中项周延规则:")
    # AAA-1: M A P, S A M -> S A P (中项M在大前提中作主项，周延)
    syl1 = Syllogism(PropositionType.A, PropositionType.A, PropositionType.A, 0, 1)
    print(f"  {syl1.get_figure_and_mood()}: {middle_term_distributed_once(syl1)}")

    # III-1: M I P, S I M -> S I P (中项M都不周延)
    syl2 = Syllogism(PropositionType.I, PropositionType.I, PropositionType.I, 0, 1)
    print(f"  {syl2.get_figure_and_mood()}: {middle_term_distributed_once(syl2)}")

    # 测试非法周延规则
    print("\n2. 测试非法周延规则:")
    # AAA-1: 合法
    print(f"  {syl1.get_figure_and_mood()}: {no_illicit_distribution(syl1)}")

    # 测试两个否定前提规则
    print("\n3. 测试两个否定前提规则:")
    # EEE-1: E E E (两个否定前提)
    syl3 = Syllogism(PropositionType.E, PropositionType.E, PropositionType.E, 0, 1)
    print(f"  {syl3.get_figure_and_mood()}: {no_two_negative_premises(syl3)}")

    # AEE-1: A E E (一个否定前提)
    syl4 = Syllogism(PropositionType.A, PropositionType.E, PropositionType.E, 0, 1)
    print(f"  {syl4.get_figure_and_mood()}: {no_two_negative_premises(syl4)}")

    # 测试否定前提否定结论规则
    print("\n4. 测试否定前提否定结论规则:")
    # AAA-1: 肯定前提肯定结论
    print(f"  {syl1.get_figure_and_mood()}: {negative_premise_negative_conclusion(syl1)}")

    # AEE-1: 否定前提否定结论
    print(f"  {syl4.get_figure_and_mood()}: {negative_premise_negative_conclusion(syl4)}")

    # AEA-1: 否定前提肯定结论 (应该无效)
    syl5 = Syllogism(PropositionType.A, PropositionType.E, PropositionType.A, 0, 1)
    print(f"  {syl5.get_figure_and_mood()}: {negative_premise_negative_conclusion(syl5)}")

def test_existential_import():
    """测试存在性假设规则在两种解释下的差异"""
    print("\n=== 测试存在性假设规则 ===")

    # AAI-1: 两个全称前提，特称结论
    syl = Syllogism(PropositionType.A, PropositionType.A, PropositionType.I, 0, 1)

    # 亚里士多德解释
    set_interpretation(InterpretationType.ARISTOTELIAN)
    result_aristotelian = existential_import_rule(syl)
    print(f"亚里士多德解释下 {syl.get_figure_and_mood()}: {result_aristotelian}")

    # 布尔解释
    set_interpretation(InterpretationType.BOOLEAN)
    result_boolean = existential_import_rule(syl)
    print(f"布尔解释下 {syl.get_figure_and_mood()}: {result_boolean}")

def test_get_all_rules():
    """测试获取所有规则的函数"""
    print("\n=== 测试获取所有规则 ===")
    rules = get_all_validation_rules()
    print(f"总共有 {len(rules)} 个规则:")
    for name, func in rules:
        print(f"  - {name}")

def test_is_valid_syllogism():
    """测试三段论有效性判断函数"""
    print("\n=== 测试三段论有效性判断 ===")

    # 经典有效三段论
    barbara = Syllogism(PropositionType.A, PropositionType.A, PropositionType.A, 0, 1)  # AAA-1
    celarent = Syllogism(PropositionType.E, PropositionType.A, PropositionType.E, 0, 1)  # EAE-1

    # 无效三段论
    invalid = Syllogism(PropositionType.I, PropositionType.I, PropositionType.I, 0, 1)  # III-1

    print("在亚里士多德解释下:")
    set_interpretation(InterpretationType.ARISTOTELIAN)
    print(f"  {barbara.get_figure_and_mood()}: {is_valid_syllogism(barbara)}")
    print(f"  {celarent.get_figure_and_mood()}: {is_valid_syllogism(celarent)}")
    print(f"  {invalid.get_figure_and_mood()}: {is_valid_syllogism(invalid)}")

    print("在布尔解释下:")
    set_interpretation(InterpretationType.BOOLEAN)
    print(f"  {barbara.get_figure_and_mood()}: {is_valid_syllogism(barbara)}")
    print(f"  {celarent.get_figure_and_mood()}: {is_valid_syllogism(celarent)}")
    print(f"  {invalid.get_figure_and_mood()}: {is_valid_syllogism(invalid)}")

if __name__ == "__main__":
    test_individual_rules()
    test_existential_import()
    test_get_all_rules()
    test_is_valid_syllogism()
    print("\n✓ 所有测试完成!")

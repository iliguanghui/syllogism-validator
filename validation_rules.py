"""
三段论验证规则模块
包含所有用于验证三段论有效性的规则函数
"""

from syllogism import PropositionType
from config import is_boolean, InterpretationType


def middle_term_distributed_once(syl):
    """
    规则1: 中项至少周延一次
    全称命题主项周延，否定命题谓项周延
    """
    # 检查大前提中的中项是否周延
    major_distributes_middle = (
        (syl.major_position == 0 and syl.major_type in [PropositionType.A, PropositionType.E]) or
        (syl.major_position == 1 and syl.major_type in [PropositionType.E, PropositionType.O])
    )

    # 检查小前提中的中项是否周延
    minor_distributes_middle = (
        (syl.minor_position == 0 and syl.minor_type in [PropositionType.A, PropositionType.E]) or
        (syl.minor_position == 1 and syl.minor_type in [PropositionType.E, PropositionType.O])
    )

    return major_distributes_middle or minor_distributes_middle


def no_illicit_distribution(syl):
    """
    规则2: 禁止非法周延
    前提中不周延的项在结论中不得周延
    """
    # 检查大项P在前提中是否周延
    p_distributed_in_major = (
        (syl.major_position == 1 and syl.major_type in [PropositionType.A, PropositionType.E]) or
        (syl.major_position == 0 and syl.major_type in [PropositionType.E, PropositionType.O])
    )

    # 检查大项P在结论中是否周延
    p_distributed_in_conclusion = syl.conclusion_type in [PropositionType.E, PropositionType.O]

    # 检查小项S在前提中是否周延
    s_distributed_in_minor = (
        (syl.minor_position == 1 and syl.minor_type in [PropositionType.A, PropositionType.E]) or
        (syl.minor_position == 0 and syl.minor_type in [PropositionType.E, PropositionType.O])
    )

    # 检查小项S在结论中是否周延
    s_distributed_in_conclusion = syl.conclusion_type in [PropositionType.A, PropositionType.E]

    # 如果在结论中周延，在前提中也必须周延
    return (not p_distributed_in_conclusion or p_distributed_in_major) and \
           (not s_distributed_in_conclusion or s_distributed_in_minor)


def no_two_negative_premises(syl):
    """
    规则3: 禁止两个否定前提
    不能从两个否定前提得出结论
    """
    major_negative = syl.major_type in [PropositionType.E, PropositionType.O]
    minor_negative = syl.minor_type in [PropositionType.E, PropositionType.O]
    return not (major_negative and minor_negative)


def negative_premise_negative_conclusion(syl):
    """
    规则4: 否定前提否定结论
    如果有一个前提是否定的，那么结论必须是否定的
    """
    major_negative = syl.major_type in [PropositionType.E, PropositionType.O]
    minor_negative = syl.minor_type in [PropositionType.E, PropositionType.O]
    has_negative_premise = major_negative or minor_negative
    negative_conclusion = syl.conclusion_type in [PropositionType.E, PropositionType.O]

    if is_boolean():
        return (not has_negative_premise) or negative_conclusion
    else:
        # 如果两个前提都是肯定的，那么结论必须是肯定的
        return has_negative_premise == negative_conclusion


def existential_import_rule(syl):
    """
    规则5: 存在性假设规则
    这是亚里士多德解释和布尔解释的主要区别

    布尔解释：两个全称前提不能得出特称结论
    亚里士多德解释：允许从全称前提推出特称结论（假设存在性）
    """
    if is_boolean():
        # 布尔解释：禁止从两个全称前提推出特称结论
        major_universal = syl.major_type in [PropositionType.A, PropositionType.E]
        minor_universal = syl.minor_type in [PropositionType.A, PropositionType.E]
        particular_conclusion = syl.conclusion_type in [PropositionType.I, PropositionType.O]
        return not (major_universal and minor_universal and particular_conclusion)
    else:
        # 亚里士多德解释：允许从全称前提推出特称结论
        return True


def get_all_validation_rules():
    """
    获取所有验证规则的列表
    返回: [(规则名称, 规则函数), ...]
    """
    return [
        ("中项至少周延一次", middle_term_distributed_once),
        ("禁止非法周延", no_illicit_distribution),
        ("禁止两个否定前提", no_two_negative_premises),
        ("否定前提否定结论", negative_premise_negative_conclusion),
        ("存在性假设规则", existential_import_rule),
    ]


def apply_all_rules(syllogism, checker=None):
    """
    对三段论应用所有验证规则

    参数:
        syllogism: 要验证的三段论
        checker: 可选的SyllogismChecker实例，如果不提供会创建新的

    返回:
        dict: 规则名称到验证结果的映射
    """
    if checker is None:
        from rule_checker import SyllogismChecker
        checker = SyllogismChecker()

    # 添加所有规则
    for rule_name, rule_func in get_all_validation_rules():
        checker.add_rule(rule_name, rule_func)

    # 执行验证
    return checker.check(syllogism)


def is_valid_syllogism(syllogism):
    """
    检查三段论是否有效

    参数:
        syllogism: 要验证的三段论

    返回:
        bool: 如果所有规则都通过则返回True，否则返回False
    """
    results = apply_all_rules(syllogism)
    return all(results.values())


# 示例用法和测试
if __name__ == "__main__":
    from syllogism import Syllogism, PropositionType
    from config import set_interpretation, InterpretationType, get_interpretation_name

    print("=== 验证规则模块测试 ===")

    # 创建一个经典的有效三段论 AAA-1 (Barbara)
    barbara = Syllogism(
        PropositionType.A, PropositionType.A, PropositionType.A, 0, 1
    )

    print(f"测试三段论: {barbara.get_figure_and_mood()}")
    print(barbara)

    # 在两种解释下测试
    for interp_type in [InterpretationType.ARISTOTELIAN, InterpretationType.BOOLEAN]:
        set_interpretation(interp_type)
        print(f"\n在{get_interpretation_name()}下:")

        results = apply_all_rules(barbara)
        print("规则验证结果:")
        for rule_name, result in results.items():
            status = "✓" if result else "✗"
            print(f"  {status} {rule_name}: {result}")

        is_valid = is_valid_syllogism(barbara)
        print(f"整体有效性: {'有效' if is_valid else '无效'}")

    print("\n=== 测试一个可能存在差异的三段论 ===")

    # 创建 AAI-1，这在亚里士多德解释中有效，在布尔解释中无效
    aai_1 = Syllogism(
        PropositionType.A, PropositionType.A, PropositionType.I, 0, 1
    )

    print(f"测试三段论: {aai_1.get_figure_and_mood()}")
    print(aai_1)

    for interp_type in [InterpretationType.ARISTOTELIAN, InterpretationType.BOOLEAN]:
        set_interpretation(interp_type)
        print(f"\n在{get_interpretation_name()}下:")

        is_valid = is_valid_syllogism(aai_1)
        print(f"整体有效性: {'有效' if is_valid else '无效'}")

        if not is_valid and interp_type == InterpretationType.BOOLEAN:
            print("  原因: 布尔解释不允许从两个全称前提推出特称结论")

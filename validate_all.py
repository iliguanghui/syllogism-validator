from syllogism import Syllogism, PropositionType
from rule_checker import SyllogismChecker

def generate_all_syllogisms():
    """生成所有可能的三段论组合"""
    all_syllogisms = []
    types = [PropositionType.A, PropositionType.E, PropositionType.I, PropositionType.O]
    positions = [0, 1]
    
    for major_type in types:
        for minor_type in types:
            for conclusion_type in types:
                for major_pos in positions:
                    for minor_pos in positions:
                        all_syllogisms.append(Syllogism(major_type, minor_type, conclusion_type, major_pos, minor_pos))

    return all_syllogisms

def main():
    # 生成所有组合
    all_syllogisms = generate_all_syllogisms()
    print(f"生成了 {len(all_syllogisms)} 种三段论组合")

    # 创建检查器并添加规则
    checker = SyllogismChecker()

    def middle_term_distributed_once(syl):
        """中项至少周延一次 全称命题主项周延，否定命题谓项周延"""
        major_distributes_middle = (syl.major_position == 0 and syl.major_type in [PropositionType.A, PropositionType.E]) or (syl.major_position == 1 and syl.major_type in [PropositionType.E, PropositionType.O])
        minor_distributes_middle = (syl.minor_position == 0 and syl.minor_type in [PropositionType.A, PropositionType.E]) or (syl.minor_position == 1 and syl.minor_type in [PropositionType.E, PropositionType.O])
        return major_distributes_middle or minor_distributes_middle

    def no_illicit_distribution(syl):
        """前提中不周延的项在结论中不得周延"""
        # 检查大项P在前提中是否周延
        p_distributed_in_major = (syl.major_position == 1 and syl.major_type in [PropositionType.A, PropositionType.E]) or (syl.major_position == 0 and syl.major_type in [PropositionType.E, PropositionType.O])
        # 检查大项P在结论中是否周延
        p_distributed_in_conclusion = syl.conclusion_type in [PropositionType.E, PropositionType.O]

        # 检查小项S在前提中是否周延
        s_distributed_in_minor = (syl.minor_position == 1 and syl.minor_type in [PropositionType.A, PropositionType.E]) or (syl.minor_position == 0 and syl.minor_type in [PropositionType.E, PropositionType.O])
        # 检查小项S在结论中是否周延
        s_distributed_in_conclusion = syl.conclusion_type in [PropositionType.A, PropositionType.E]

        # 如果在结论中周延，在前提中也必须周延
        return (not p_distributed_in_conclusion or p_distributed_in_major) and (not s_distributed_in_conclusion or s_distributed_in_minor)

    def no_two_negative_premises(syl):
        """不能从两个否定前提得出结论"""
        major_negative = syl.major_type in [PropositionType.E, PropositionType.O]
        minor_negative = syl.minor_type in [PropositionType.E, PropositionType.O]
        return not (major_negative and minor_negative)

    def negative_premise_negative_conclusion(syl):
        """否定前提与否定结论对应"""
        major_negative = syl.major_type in [PropositionType.E, PropositionType.O]
        minor_negative = syl.minor_type in [PropositionType.E, PropositionType.O]
        has_negative_premise = major_negative or minor_negative
        negative_conclusion = syl.conclusion_type in [PropositionType.E, PropositionType.O]

        # 如果有一个前提是否定的，那么结论必须是否定的
        return (not has_negative_premise) or negative_conclusion

    def no_particular_from_universal(syl):
        """两个全称前提得不出特称结论"""
        major_universal = syl.major_type in [PropositionType.A, PropositionType.E]
        minor_universal = syl.minor_type in [PropositionType.A, PropositionType.E]
        particular_conclusion = syl.conclusion_type in [PropositionType.I, PropositionType.O]

        return not (major_universal and minor_universal and particular_conclusion)

    checker.add_rule("中项至少周延一次", middle_term_distributed_once)
    checker.add_rule("禁止非法周延", no_illicit_distribution)
    checker.add_rule("禁止两个否定前提", no_two_negative_premises)
    checker.add_rule("禁止从否定推肯定", negative_premise_negative_conclusion)
    checker.add_rule("禁止全称前提特称结论", no_particular_from_universal)

    # 检验所有组合
    valid_syllogisms = []
    for syl in all_syllogisms:
        results = checker.check(syl)
        if all(results.values()):  # 所有规则都通过
            valid_syllogisms.append(syl)

    # 打印有效组合
    print(f"\n找到 {len(valid_syllogisms)} 个有效的三段论:")
    for i, syl in enumerate(valid_syllogisms, 1):
        print(f"\n=== 有效三段论 {i} ===")
        print(syl)

if __name__ == "__main__":
    main()

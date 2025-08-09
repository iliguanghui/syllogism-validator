from syllogism import Syllogism, PropositionType
from rule_checker import SyllogismChecker
from config import get_interpretation, is_aristotelian, is_boolean, set_interpretation, InterpretationType, get_interpretation_name
from validation_rules import get_all_validation_rules, is_valid_syllogism

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

def main(interpretation_type=None):
    # 设置解释类型
    if interpretation_type:
        set_interpretation(interpretation_type)

    print(f"使用 {get_interpretation_name()}")

    # 生成所有组合
    all_syllogisms = generate_all_syllogisms()
    print(f"生成了 {len(all_syllogisms)} 种三段论组合")

    # 检验所有组合 - 使用规则模块中的函数
    valid_syllogisms = []
    for syl in all_syllogisms:
        if is_valid_syllogism(syl):
            valid_syllogisms.append(syl)

    # 打印有效组合
    print(f"\n找到 {len(valid_syllogisms)} 个有效的三段论:")
    for i, syl in enumerate(valid_syllogisms, 1):
        print(f"\n=== 有效三段论 {i} ===")
        print(syl)

if __name__ == "__main__":
    import sys

    # 检查命令行参数
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg in ['aristotelian', 'a', '亚里士多德']:
            main(InterpretationType.ARISTOTELIAN)
        elif arg in ['boolean', 'b', '布尔']:
            main(InterpretationType.BOOLEAN)
        elif arg in ['both', 'compare', '比较']:
            print("=== 比较两种解释的结果 ===\n")
            print("1. 亚里士多德解释:")
            main(InterpretationType.ARISTOTELIAN)
            print("\n" + "="*50 + "\n")
            print("2. 布尔解释:")
            main(InterpretationType.BOOLEAN)
        else:
            print("用法: python3 validate_all.py [aristotelian|boolean|both]")
            print("  aristotelian, a, 亚里士多德 - 使用亚里士多德解释")
            print("  boolean, b, 布尔 - 使用布尔解释")
            print("  both, compare, 比较 - 比较两种解释")
    else:
        # 默认使用亚里士多德解释
        main()

from syllogism import Syllogism, PropositionType
from config import get_interpretation, is_aristotelian, is_boolean, InterpretationType

class SyllogismChecker:
    def __init__(self):
        self.rules = []

    def add_rule(self, name, check_function):
        """添加检查规则"""
        self.rules.append((name, check_function))

    def check(self, syllogism):
        """对三段论应用所有规则"""
        results = {}
        for rule_name, rule_func in self.rules:
            try:
                results[rule_name] = rule_func(syllogism)
            except Exception as e:
                results[rule_name] = f"错误: {e}"
        return results

# 示例用法
if __name__ == "__main__":
    checker = SyllogismChecker()

    # 定义规则
    def check_figure_1(syl):
        """检查第一格"""
        return syl.major_position == 0 and syl.minor_position == 1

    def check_aaa_valid(syl):
        """检查AAA是否有效"""
        return (syl.major_type == PropositionType.A and
                syl.minor_type == PropositionType.A and
                syl.conclusion_type == PropositionType.A)

    checker.add_rule("第一格", check_figure_1)
    checker.add_rule("AAA模式", check_aaa_valid)

    # 测试
    syl = Syllogism(PropositionType.A, PropositionType.A, PropositionType.A, 0, 1)

    results = checker.check(syl)
    print(f"三段论:\n{syl}")
    print("检查结果:")
    for rule, result in results.items():
        print(f"  {rule}: {result}")
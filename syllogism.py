from enum import Enum

class PropositionType(Enum):
    A = "A"  # 全称肯定
    E = "E"  # 全称否定
    I = "I"  # 特称肯定
    O = "O"  # 特称否定

class Syllogism:
    def __init__(self, major_type, minor_type, conclusion_type, 
                 major_position, minor_position):
        self.major_type = major_type          # 大前提类型(AEIO)
        self.minor_type = minor_type          # 小前提类型(AEIO)
        self.conclusion_type = conclusion_type # 结论类型(AEIO)
        self.major_position = major_position   # 大前提中项位置: 0=主项, 1=谓项
        self.minor_position = minor_position   # 小前提中项位置: 0=主项, 1=谓项
    
    def get_figure_and_mood(self):
        """获取格和式，如AAA-1"""
        mood = f"{self.major_type.value}{self.minor_type.value}{self.conclusion_type.value}"
        if self.major_position == 0 and self.minor_position == 1:
            figure = 1
        elif self.major_position == 1 and self.minor_position == 1:
            figure = 2
        elif self.major_position == 0 and self.minor_position == 0:
            figure = 3
        else:
            figure = 4
        return f"{mood}-{figure}"
    
    def __str__(self):
        name = self.get_figure_and_mood()
        # 大前提: M和P的位置
        if self.major_position == 0:
            major_line = f"M {self.major_type.value} P"
        else:
            major_line = f"P {self.major_type.value} M"
        
        # 小前提: S和M的位置
        if self.minor_position == 0:
            minor_line = f"M {self.minor_type.value} S"
        else:
            minor_line = f"S {self.minor_type.value} M"
        
        # 结论: S和P
        conclusion_line = f"S {self.conclusion_type.value} P"
        
        return f"{name}\n{major_line}\n{minor_line}\n-----\n{conclusion_line}"

# 示例用法
if __name__ == "__main__":
    syl = Syllogism(PropositionType.A, PropositionType.A, PropositionType.A, 0, 0)
    print(syl)
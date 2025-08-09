# Syllogism Validator

A Python-based tool for validating classical syllogisms according to Aristotelian logic rules. This project generates all possible syllogistic combinations and identifies which ones are logically valid under both Aristotelian and Boolean interpretations.

## Overview

This project implements a comprehensive syllogism validation system that:
- Models syllogistic propositions using the traditional AEIO classification
- Generates all possible syllogistic combinations (256 total)
- Applies classical logical rules to determine validity
- Supports both Aristotelian and Boolean interpretations
- Identifies valid syllogistic forms under each interpretation

## Features

- **Complete Syllogism Modeling**: Represents syllogisms with major premise, minor premise, and conclusion
- **Four Proposition Types**: Supports A (universal affirmative), E (universal negative), I (particular affirmative), and O (particular negative) propositions
- **Four Figures**: Handles all four syllogistic figures based on middle term position
- **Dual Interpretation Support**: Validates syllogisms under both Aristotelian and Boolean interpretations
- **Rule-Based Validation**: Implements fundamental rules of valid syllogisms with interpretation-specific differences
- **Comprehensive Testing**: Validates all 256 possible syllogistic combinations
- **Comparison Tools**: Provides utilities to compare results between interpretations

## Key Differences Between Interpretations

### Aristotelian Interpretation (Traditional)
- Assumes existential import for universal statements
- Allows deriving particular conclusions from universal premises
- Typically yields more valid syllogistic forms

### Boolean Interpretation (Modern)
- Does not assume existential import
- Prohibits deriving particular conclusions from universal premises alone
- More restrictive, yielding fewer valid forms

## Project Structure

```
syllogism-validator/
├── syllogism.py           # Core syllogism data structure and representation
├── rule_checker.py        # Rule-based validation framework
├── config.py             # Global configuration for interpretation types
├── validation_rules.py   # All validation rules in a separate module
├── validate_all.py       # Main script to validate all combinations
├── demo_interpretations.py # Demonstration of interpretation differences
├── test_config.py        # Tests for configuration module
├── test_validation_rules.py # Tests for validation rules
└── README.md             # This file
```

## Installation

No external dependencies required. This project uses only Python standard library.

```bash
git clone <repository-url>
cd syllogism-validator
```

## Usage

### Basic Usage

Run the main validation script with default (Aristotelian) interpretation:

```bash
python3 validate_all.py
```

### Specify Interpretation Type

```bash
# Use Aristotelian interpretation
python3 validate_all.py aristotelian

# Use Boolean interpretation
python3 validate_all.py boolean

# Compare both interpretations
python3 validate_all.py both
```

### Compare Interpretations

Run the demonstration script to see differences:

```bash
python3 demo_interpretations.py
```

### Example Output

```
使用 亚里士多德解释
生成了 256 种三段论组合

找到 24 个有效的三段论:

=== 有效三段论 1 ===
AAA-1
M A P
S A M
-----
S A P
```

### Using Individual Components

#### Setting Interpretation Type

```python
from config import set_interpretation, InterpretationType, get_interpretation_name

# Set to Aristotelian interpretation
set_interpretation(InterpretationType.ARISTOTELIAN)
print(f"Current interpretation: {get_interpretation_name()}")

# Set to Boolean interpretation
set_interpretation(InterpretationType.BOOLEAN)
print(f"Current interpretation: {get_interpretation_name()}")
```

#### Creating a Syllogism

```python
from syllogism import Syllogism, PropositionType

# Create AAA-1 syllogism (Barbara)
syl = Syllogism(
    major_type=PropositionType.A,      # All M are P
    minor_type=PropositionType.A,      # All S are M
    conclusion_type=PropositionType.A, # All S are P
    major_position=0,                  # M is subject in major premise
    minor_position=1                   # M is predicate in minor premise
)

print(syl)  # Displays the syllogism in standard form
```

#### Custom Rule Checking

```python
from rule_checker import SyllogismChecker

checker = SyllogismChecker()

# Add custom rule
def check_first_figure(syl):
    return syl.major_position == 0 and syl.minor_position == 1

checker.add_rule("First Figure", check_first_figure)

# Check syllogism
results = checker.check(syl)
print(results)
```

## Validation Rules

The system implements fundamental rules of valid syllogisms:

1. **Middle Term Distribution**: The middle term must be distributed at least once in the premises
2. **No Illicit Distribution**: Terms that are not distributed in premises cannot be distributed in the conclusion
3. **No Two Negative Premises**: Cannot derive a conclusion from two negative premises
4. **Negative Premise Rule**: If one premise is negative, the conclusion must be negative
5. **Existential Import Rule**:
   - **Aristotelian**: Allows particular conclusions from universal premises
   - **Boolean**: Prohibits particular conclusions from universal premises alone

## Syllogistic Notation

- **Proposition Types**:
  - A: Universal Affirmative (All S are P)
  - E: Universal Negative (No S are P)
  - I: Particular Affirmative (Some S are P)
  - O: Particular Negative (Some S are not P)

- **Figures**: Determined by middle term position
  - Figure 1: M-P, S-M
  - Figure 2: P-M, S-M
  - Figure 3: M-P, M-S
  - Figure 4: P-M, M-S

- **Standard Form**: Each syllogism is displayed as `MOOD-FIGURE` (e.g., AAA-1)

## Valid Syllogistic Forms

### Aristotelian Interpretation
Typically identifies 24 valid forms, including traditional forms like:
- AAA-1 (Barbara), EAE-1 (Celarent), AII-1 (Darii), EIO-1 (Ferio)
- Plus additional forms with particular conclusions from universal premises

### Boolean Interpretation
Typically identifies 15 valid forms, the traditional "unconditionally valid" forms:
- AAA-1 (Barbara), EAE-1 (Celarent), AII-1 (Darii), EIO-1 (Ferio)
- And others that don't rely on existential import

## Technical Details

- **Language**: Python 3
- **Dependencies**: None (uses only standard library)
- **Architecture**: Object-oriented design with separation of concerns
- **Configuration**: Global interpretation settings with easy switching
- **Testing**: Exhaustive validation of all 256 possible combinations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source. Please check the repository for license details.

## Educational Use

This tool is particularly useful for:
- Logic and philosophy students learning syllogistic reasoning
- Educators teaching classical vs. modern logic
- Researchers studying formal logic systems
- Anyone interested in automated logical reasoning
- Comparative studies of different logical interpretations

## Future Enhancements

Potential improvements could include:
- Support for additional logical interpretations
- Integration with natural language processing
- Web-based interface
- Extended logical rule sets
- Performance optimizations for larger rule sets
- Graphical visualization of syllogistic relationships

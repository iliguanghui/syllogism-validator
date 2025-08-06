# Syllogism Validator

A Python-based tool for validating classical syllogisms according to Aristotelian logic rules. This project generates all possible syllogistic combinations and identifies which ones are logically valid.

## Overview

This project implements a comprehensive syllogism validation system that:
- Models syllogistic propositions using the traditional AEIO classification
- Generates all possible syllogistic combinations (256 total)
- Applies classical logical rules to determine validity
- Identifies the 15 valid syllogistic forms

## Features

- **Complete Syllogism Modeling**: Represents syllogisms with major premise, minor premise, and conclusion
- **Four Proposition Types**: Supports A (universal affirmative), E (universal negative), I (particular affirmative), and O (particular negative) propositions
- **Four Figures**: Handles all four syllogistic figures based on middle term position
- **Rule-Based Validation**: Implements five fundamental rules of valid syllogisms
- **Comprehensive Testing**: Validates all 256 possible syllogistic combinations

## Project Structure

```
syllogism-validator/
├── syllogism.py        # Core syllogism data structure and representation
├── rule_checker.py     # Rule-based validation framework
├── validate_all.py     # Main script to validate all combinations
└── README.md          # This file
```

## Installation

No external dependencies required. This project uses only Python standard library.

```bash
git clone <repository-url>
cd syllogism-validator
```

## Usage

### Basic Usage

Run the main validation script to see all valid syllogisms:

```bash
python3 validate_all.py
```

This will output:
- Total number of generated combinations (256)
- All 15 valid syllogistic forms with their traditional notation

### Example Output

```
生成了 256 种三段论组合

找到 15 个有效的三段论:

=== 有效三段论 1 ===
AAA-1
M A P
S A M
-----
S A P

=== 有效三段论 2 ===
AEE-4
P A M
M E S
-----
S E P
```

### Using Individual Components

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

The system implements five fundamental rules of valid syllogisms:

1. **Middle Term Distribution**: The middle term must be distributed at least once in the premises
2. **No Illicit Distribution**: Terms that are not distributed in premises cannot be distributed in the conclusion
3. **No Two Negative Premises**: Cannot derive a conclusion from two negative premises
4. **Negative Premise Rule**: If one premise is negative, the conclusion must be negative
5. **Universal-Particular Rule**: Cannot derive a particular conclusion from two universal premises

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

The system identifies 15 traditionally valid syllogistic forms, including:
- AAA-1 (Barbara)
- EAE-1 (Celarent)
- AII-1 (Darii)
- EIO-1 (Ferio)
- And 11 others across all four figures

## Technical Details

- **Language**: Python 3
- **Dependencies**: None (uses only standard library)
- **Architecture**: Object-oriented design with separation of concerns
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
- Educators teaching classical logic
- Researchers studying formal logic systems
- Anyone interested in automated logical reasoning

## Future Enhancements

Potential improvements could include:
- Support for non-standard syllogistic forms
- Integration with natural language processing
- Web-based interface
- Extended logical rule sets
- Performance optimizations for larger rule sets

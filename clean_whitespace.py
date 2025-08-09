#!/usr/bin/env python3
"""
清理项目中所有文件的行尾空白字符
"""

import os
import re
from pathlib import Path

def clean_file(file_path):
    """清理单个文件的行尾空白字符"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 移除行尾空白字符
        lines = content.splitlines()
        cleaned_lines = [line.rstrip() for line in lines]
        cleaned_content = '\n'.join(cleaned_lines)

        # 如果文件原本以换行符结尾，保持这个换行符
        if content.endswith('\n'):
            cleaned_content += '\n'

        # 只有在内容发生变化时才写入文件
        if content != cleaned_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            return True
        return False
    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {e}")
        return False

def main():
    """主函数"""
    project_root = Path(__file__).parent

    # 要处理的文件扩展名
    extensions = ['.py', '.md', '.txt', '.yml', '.yaml', '.json']

    cleaned_files = []
    total_files = 0

    print("开始清理行尾空白字符...")

    for ext in extensions:
        for file_path in project_root.glob(f"*{ext}"):
            if file_path.is_file():
                total_files += 1
                if clean_file(file_path):
                    cleaned_files.append(file_path.name)
                    print(f"✓ 已清理: {file_path.name}")

    print(f"\n处理完成!")
    print(f"总共检查了 {total_files} 个文件")
    print(f"清理了 {len(cleaned_files)} 个文件")

    if cleaned_files:
        print("\n已清理的文件:")
        for filename in cleaned_files:
            print(f"  - {filename}")
    else:
        print("没有发现需要清理的文件")

if __name__ == "__main__":
    main()

import os
import hashlib

def generate_md5(file_path, output_dir):
    # 打开文件并计算 MD5 哈希值
    with open(file_path, 'rb') as f:
        md5_hash = hashlib.md5(f.read()).hexdigest()

    # 创建输出文件并写入哈希值
    output_file = os.path.join(output_dir, f'{os.path.basename(file_path)}.md5')
    with open(output_file, 'w') as f:
        f.write(md5_hash)

def batch_generate_md5(input_dir, output_dir):
    # 遍历输入目录下的所有文件
    for root, _, files in os.walk(input_dir):
        for file in files:
            file_path = os.path.join(root, file)
            # 判断是否是文件（而非目录）
            if os.path.isfile(file_path):
                generate_md5(file_path, output_dir)

# 使用示例
input_dir = './'  # 输入目录路径
output_dir = './'  # 输出目录路径
batch_generate_md5(input_dir, output_dir)
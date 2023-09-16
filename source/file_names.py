import os
import json

# 假设你的目录路径是 '/path/to/your/directory'
directory_path = './'

# 用于存储文件名的字典
file_names = {}

# 遍历目录中的文件
for filename in os.listdir(directory_path):
    # 我们只对 .txz 文件感兴趣
    if filename.endswith('.txz'):
        # 从文件名中提取 'alien' 部分
        alien_name = filename.split('-')[0]
        file_names[alien_name] = filename  # 将 'alien' 名称和完整文件名保存到字典中

# 将字典输出为 JSON 格式
with open('file_names.json', 'w') as f:
    json.dump(file_names, f)
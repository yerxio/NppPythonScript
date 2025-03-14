# -*- coding: utf-8 -*-
from Npp import editor, console
import json

def convert_to_json():
    # 读取文件内容
    text = editor.getText()
    console.write("原始文本内容:\n{}\n".format(text))

    try:
        # 将文本按行分割
        lines = text.strip().split('\n')
        
        # 创建一个字典来存储键值对
        data = {}

        # 遍历每一行
        for line in lines:
            # 分割键和值
            key, value = line.strip().split(',', 1)
            
            # 如果键已经存在，则将值添加到列表中
            if key in data:
                if isinstance(data[key], list):
                    data[key].append(value)
                else:
                    data[key] = [data[key], value]
            else:
                data[key] = value

        # 将字典转换为 JSON 格式
        json_text = json.dumps(data, indent=4, ensure_ascii=False)
        
        # 替换文件内容
        editor.setText(json_text)
        console.write("转换成功，已替换为 JSON\n")
    except Exception as e:
        console.write("转换失败: {}\n".format(str(e)))

# 调用函数进行转换
convert_to_json()
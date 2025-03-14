# -*- coding: utf-8 -*-
from Npp import editor, console
import json
import ast

def convert_to_json():
    text = editor.getText()  # 读取文件内容
    console.write("原始文本内容:\n{}\n".format(text))  # 在 Notepad++ 控制台输出原始文本内容

    try:
        # 使用 ast.literal_eval 安全地解析文本为 Python 对象（字典或列表）
        data = ast.literal_eval(text)
        
        if isinstance(data, (dict, list)):  # 检查是否是字典或列表
            # 将 Python 对象转换为 JSON 格式的字符串
            json_text = json.dumps(data, indent=4, ensure_ascii=False)
            editor.setText(json_text)  # 替换文件内容
            console.write("转换成功，已替换为 JSON\n")
        else:
            console.write("错误：文件内容不是一个有效的 Python 字典或列表\n")
    except Exception as e:
        console.write("转换失败: {}\n".format(str(e)))

# 调用函数进行转换
convert_to_json()
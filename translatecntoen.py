# 导入 google.cloud.translate 库
from google.cloud import translate

# 创建一个翻译客户端
client = translate.TranslationServiceClient()

# 定义项目 ID
project_id = "YOUR_PROJECT_ID"

# 定义父资源
parent = f"projects/{project_id}/locations/global"

# 定义源语言和目标语言
source_language = "zh"
target_language = "en"

# 定义要翻译的文本，可以是一个列表
text = ["你好，世界！", "今天天气怎么样？"]

# 遍历每个文本
for t in text:
    # 调用 translate_text 方法并获取响应
    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [t],
            "source_language_code": source_language,
            "target_language_code": target_language,
        }
    )
    # 从响应中获取翻译结果
    result = response.translations[0].translated_text
    # 打印原文和译文
    print(t, "->", result)
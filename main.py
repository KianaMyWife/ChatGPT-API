import openai

SECRET_KEY = "XX"  # 替换你的API key
openai.api_key = SECRET_KEY

history = []

while True:
    input_text = input("user:")
    history.append({'role': 'user', 'content': input_text})

    # API参数文档:https://platform.openai.com/docs/api-reference/chat/create

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=history,
    )

    # 返回的一个completion示例,后面包含参数解释
    # {
    #     "choices": [
    #         {
    #             "finish_reason": "stop",
    #             "index": 0,
    #             "message": {
    #                 "content": "\n\n\u4f60\u597d\uff0c\u6709\u4ec0\u4e48\u9700\u8981\u6211\u5e2e\u5fd9\u7684\u5417\uff1f",
    #                 "role": "assistant"
    #             }
    #         }
    #     ],
    #     "created": 1678267810,
    #     "id": "chatcmpl-6rkPa92PsXkksXlJnDFkT4X1k09qm",
    #     "model": "gpt-3.5-turbo-0301",
    #     "object": "chat.completion",
    #     "usage": {
    #         "completion_tokens": 19,
    #         "prompt_tokens": 9,
    #         "total_tokens": 28
    #     }
    # 相关参数解释(来自chatgpt):
    # - "choices": 这是一个数组，其中包含多个聊天响应，每个响应都是一个对象。在这个 JSON 对象中，它只包含单个响应。每个聊天响应都包含以下键值对：
    #       - "finish_reason": 这是一个字符串，表示生成响应的原因。它的值是 "stop"，表示聊天对话已经结束。
    #       - "index": 这是一个整数，表示聊天响应的索引。
    #       - "message": 这是一个对象，表示聊天响应的具体内容。它包含以下键值对：
    #           - "content": 这是一个字符串，表示聊天响应的文本内容。这个字符串使用了 Unicode 转义序列，需要将它们转换回原始文本。
    #           - "role": 这是一个字符串，表示聊天响应的角色。在这个对象中，它的值是 "assistant"，表示这个响应是由聊天机器人生成的。
    # - "created": 这是一个整数，表示响应的创建时间。它是一个 Unix 时间戳，表示从 1970 年 1 月 1 日 00:00:00 UTC 到当前时间的秒数。
    # - "id": 这是一个字符串，表示聊天响应的唯一标识符。它由 API 自动分配，并用于跟踪和管理聊天对话。
    # - "model": 这是一个字符串，表示使用的语言模型。在这个对象中，它的值是 "gpt-3.5-turbo-0301"，表示使用了 GPT-3.5 Turbo 语言模型。
    # - "object": 这是一个字符串，表示对象类型。在这个对象中，它的值是 "chat.completion"，表示这个对象是一个聊天响应。
    # - "usage": 这是一个对象，表示 API 的使用情况统计信息。它包含以下键值对：
    #       - "completion_tokens": 这是一个整数，表示用于生成聊天响应的令牌数。
    #       - "prompt_tokens": 这是一个整数，表示用于生成聊天响应的提示文本令牌数。
    #       - "total_tokens": 这是一个整数，表示生成聊天响应所使用的总令牌数。

    return_text = completion.choices[0].message.content
    return_text = return_text.lstrip('\n')
    history.append({'role': 'assistant', 'content': return_text})
    print("bot:", return_text)

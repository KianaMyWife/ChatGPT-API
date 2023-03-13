import openai

SECRET_KEY = "XX"  # 替换你的API key 可在https://platform.openai.com/account/api-keys创建,只有在创建时能看,关了之后再也看不到了,如果忘记了,再新建一个
openai.api_key = SECRET_KEY

history = []

while True:
    input_text = input("user:")
    history.append({'role': 'user', 'content': input_text})

    # API参数文档:https://platform.openai.com/docs/api-reference/chat/create
    # openai.ChatCompletion.create包含的参数:
    # - model:模型种类,目前只有 gpt-3.5-turbo 和 gpt-3.5-turbo-0301 ####必填
    # - messages 发送给chatgpt的消息,格式类似:  ###必填
    #     messages=[
    #     {"role": "system", "content": "You are a helpful assistant."},
    #     {"role": "user", "content": "Who won the world series in 2020?"},
    #     {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    #     ]
    #    role只有以上三个参数
    #
    # - temperature:默认为1,可选0-2,控制聊天机器人生成的文本的创造性程度。较高的值会产生更加创造性的响应，但也可能会导致不准确或不相关的响应。
    # - top-p : 默认为1 一般不动,控制聊天机器人在生成响应时选择的标记的数量。较高的top_p值会导致响应的多样性和创造性增加，但也可能会导致响应不准确或不相关。
    # - n : 为每个输入消息生成多少个聊天完成选项,默认为1
    # - stream : 是否以流式数据发送,默认为false
    # - stop : string 或者 array,m默认为null具体没看明白什么意思,原为:Up to 4 sequences where the API will stop generating further tokens.
    # - max_token : 返回的最大token长度,最长为4096,默认没说多少,较高的max_tokens值会产生更长的响应，但也可能会导致响应不相关或不准确。
    # - presence_penalty : 控制聊天机器人生成响应时是否使用特定的词汇或主题。较高的presence_penalty值会导致聊天机器人更少地使用特定的词汇或主题。
    # - frequency_penalty : 控制聊天机器人生成响应时在文本中重复使用相同词汇的程度。较高的frequency_penalty值会导致聊天机器人更少地重复使用相同的词汇。
    # - logit_bits : 根据chatgpt的说法:用来控制聊天机器人生成响应时对某些单词或主题的偏好程度。具体来说，logit_bias是一个字典，它的键是单词或主题，值是偏好程度。这些偏好可以是正数或负数，
    # 分别表示偏好或不偏好某个单词或主题。例如，如果您希望聊天机器人在生成响应时更注重"科技"方面的话题，可以将"科技"设置为偏好的主题，并在logit_bias参数中为其指定一个正数值。
    # 需要注意的是，logit_bias参数的值会影响聊天机器人生成响应时对不同单词和主题的选择。如果您不确定如何设置logit_bias参数，可以尝试使用默认值或者进行一些实验来了解不同值对聊天机器人响应的影响。
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
    # 需要将机器人的回答和你的提问再次发送回去,否则无法联系上下文
    history.append({'role': 'assistant', 'content': return_text})
    print("bot:", return_text)

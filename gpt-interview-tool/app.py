import openai

# # 设置你的 OpenAI API 密钥
# openai.api_key = "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"  # 替换为你的真实密钥
#
# def generate_interview_questions(role: str, language: str = "中文", num_questions: int = 5) -> str:
#     """
#     基于职位生成常见面试问题及参考答案。
#     :param role: 职位名，例如“Python后端工程师”
#     :param language: 中文 or English
#     :param num_questions: 生成的题目数量
#     :return: 生成内容字符串
#     """
#     prompt = (
#         f"请为“{role}”这个职位生成{num_questions}个常见面试问题，"
#         f"并为每个问题提供参考答案。用{language}回答，格式如下：\n"
#         f"问题1：...\n答案：...\n问题2：...\n答案：...\n"
#     )
#
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",  # 你也可以改成 "gpt-4"
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0.7,
#             max_tokens=1000,
#         )
#         return response['choices'][0]['message']['content']
#     except Exception as e:
#         return f"生成失败：{e}"
#
# # 示例调用
# if __name__ == "__main__":
#     job_title = input("请输入目标职位（如：Python后端工程师）：")
#     result = generate_interview_questions(job_title)
#     print("\n生成的面试问题与答案：\n")
#     print(result)
import openai
import streamlit as st
OPENAI_API_KEY = "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"  # 替换为你的真实密钥

# 设置你的 OpenAI API Key（建议用 st.secrets 保存）
openai.api_key = st.secrets["OPENAI_API_KEY"]  # 在 .streamlit/secrets.toml 设置你的 key

st.set_page_config(page_title="gpt-interview-tool 面试题生成器", page_icon="🧠")
st.title("🧠 gpt-interview-tool 面试题生成器")

st.markdown("""
这是一款基于 ChatGPT 的自动面试题生成器。

- 📌 输入职位名称，如“Python后端工程师”
- 📄 自动生成常见面试问题 + 答案
""")

# 用户输入
job_title = st.text_input("请输入目标职位：", placeholder="例如：数据分析师")
num_questions = st.slider("问题数量：", 3, 10, 5)
language = st.radio("输出语言：", ["中文", "English"])

if st.button("生成面试题") and job_title:
    with st.spinner("正在生成，请稍候..."):
        prompt = (
            f"请为“{job_title}”这个职位生成{num_questions}个常见面试问题，"
            f"并为每个问题提供参考答案。用{language}回答，格式如下：\n"
            f"问题1：...\n答案：...\n问题2：...\n答案：...\n"
        )

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=1500,
            )
            content = response['choices'][0]['message']['content']
            st.success("生成成功！")
            st.text_area("面试题与参考答案：", content, height=400)
        except Exception as e:
            st.error(f"生成失败：{e}")
else:
    st.info("请填写职位名称后点击按钮生成面试题。")


import os
from dotenv import load_dotenv

load_dotenv()
from openai import OpenAI
import pyupbit

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
upbit = pyupbit.Upbit(os.getenv("UPBIT_ACCESS_KEY"), os.getenv("UPBIT_SECRET_KEY"))

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",
        },
        {
            "role": "user",
            "content": "Compose a poem that explains the concept of recursion in programming.",
        },
    ],
)

# OpenAPI 연결
print(completion.choices[0].message)

# 업비트 연결
krw = upbit.get_balance("KRW")
print(krw)

# 5-13.Pandas_test

import pandas as pd

# 데이터프레임(2차원 리스트)
df = pd.DataFrame([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
print(df)
print(type(a))


# 시리즈(1차원 리스트)
s = pd.Series([1.0, 3.0, 5.0, 7.0, 9.0])
print(s)
print(type(s))


## 키, 몸무게, 성별 데이터프레임 생성하기
df1 = pd.DataFrame({
    "weight": [ 80.0, 70.4, 65.5, 45.9, 51.2, 72.5 ],
    "height": [ 170,  180,  155,  143,  154,  160  ],
    "gender": [ "f",  "m",  "m",  "f",  "f",  "m"  ]
})

# 1) 몸무게와 키 목록 추출하기
print("몸무게와 키 목록\n", df1[["weight","height"]])

# 2) slicing(시작, 끝-1, 증분) 인덱싱은 0부터
print("df1[2:4]\n", df1[2:4])
print("df1[3:]\n", df1[3:])

# 3) filtering
print("키가 160이상\n", df1[df1.height >= 160])
print("남성\n", df1[df1.gender == 'm'])

# 4) sorting
print("--- 키로 정렬\n", df1.sort_values(by="height"))
print("--- 몸무게로 정렬\n", df1.sort_values(by="weight", ascending=False))

# 5) transepose (행과 열의 반전)
print(df1)
print(df1.T)

# 6) 키와 몸무게 정규화하기(값-최소값)/(최대값-최소값)
def norm(df1, key):
    c = df1[key]
    v_max = c.max()
    v_min = c.min()
    print(key, "=", v_min, "~", v_max)
    df1[key] = (c - v_min) / (v_max - v_min)

norm(df1, "weight")
norm(df1, "height")
print(df1)

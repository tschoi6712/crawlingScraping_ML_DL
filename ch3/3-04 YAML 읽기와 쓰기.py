# 3-04 YAML 읽기와 쓰기

"""
애플리케이션 설정 파일을 작성할 때 많이 사용 : 웹프레임워크 Ruby on Rails(루비), 심포니(PHP)
"""

import yaml

## YAML 읽기

# YAML 정의하기 ---- (※1)
yaml_str = """
Date: 2017-03-10
PriceList:
    -
        item_id: 1000
        name: Banana
        color: yellow
        price: 800
    -
        item_id: 1001
        name: Orange
        color: orange
        price: 1400
    -
        item_id: 1002
        name: Apple
        color: red
        price: 2400
"""

# YAML 분석하기 --- (※2)
data = yaml.load(yaml_str, Loader=yaml.FullLoader)

# 이름과 가격 출력하기 --- (※3)
for item in data['PriceList']:
    print(item["name"], item["price"])
    

## YAML 쓰기
    
# 파이썬 데이터를 YAML 데이터로 출력하기
customer = [
    { "name": "InSeong", "age": "24", "gender": "man" },
    { "name": "Akatsuki", "age": "22", "gender": "woman" },
    { "name": "Harin", "age": "23", "gender": "man" },
    { "name": "Yuu", "age": "31", "gender": "woman" }
]

# 파이썬 데이터를 YAML 데이터로 변환하기
yaml_str = yaml.dump(customer)
print(yaml_str)
print("--- --- ---")

# YAML 데이터를 파이썬 데이터로 변환하기
data = yaml.load(yaml_str)

# 이름 출력하기
for p in data:
    print(p["name"])


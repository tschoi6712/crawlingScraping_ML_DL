# 3-10 데이터베이스(sqlite)_1

import sqlite3

# sqlite 데이터베이스 연결하기 --- (※1)
dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath)

# 데이터베이스를 조작하는 커서를 추출하고 쿼리문 생성 --- (※2)
cur = conn.cursor()
cur.executescript("""
DROP TABLE IF EXISTS items;       /* items 테이블이 이미 있다면 제거하기 */
CREATE TABLE items(               /* 테이블 생성하기 */
    item_id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    price INTEGER
);
                                  /* 데이터 넣기 */
INSERT INTO items(name, price)VALUES('Apple', 800);
INSERT INTO items(name, price)VALUES('Orange', 780);  
INSERT INTO items(name, price)VALUES('Banana', 430);
""")

# 위의 조작을 데이터베이스에 반영하기 --- (※3)
conn.commit()

# 데이터 추출하기 --- (※4)
cur = conn.cursor()
cur.execute("SELECT item_id,name,price FROM items")
item_list = cur.fetchall()

# 출력하기
for it in item_list:
    print(it)
# 6-11.N-gram_test

'''n-gram은 n개의 연속적인 단어 나열을 의미(갖고 있는 코퍼스에서 n개의 단어 뭉치 단위로 끊어서 이를 하나의 토큰으로 간주)'''

def ngram(s, num):
    res = []
    slen = len(s) - num + 1
    for i in range(slen):
        ss = s[i:i+num]
        res.append(ss)
    return res

def diff_ngram(sa, sb, num):
    a = ngram(sa, num)
    b = ngram(sb, num)
    r = []
    cnt = 0
    for i in a:
        for j in b:
            if i == j:
                cnt += 1
                r.append(i)
    return cnt / len(a), r

a = "오늘 강남에서 맛있는 스파게티를 먹었다."
b = "강남에서 먹었던 오늘의 스파게티는 맛있었다."

# 2-gram
r2, word2 = diff_ngram(a, b, 2)
print("2-gram:", r2, word2)

# 3-gram
r3, word3  = diff_ngram(a, b, 3)
print("3-gram:", r3, word3)
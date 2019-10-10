# 6-05.Word2vec_wiki.model

from gensim.models import word2vec

data = word2vec.Text8Corpus("wiki.wakati")
model = word2vec.Word2Vec(data, size=100)
model.save("wiki.model")
print("ok")

# 위키모델 사용하기
from gensim.models import word2vec
model = word2vec.Word2Vec.load('D:/1.Workspace/1.Python_ws/2_3.MachineDeepLearningPython/Kowiki_model/wiki.model')

model.wv.most_similar(positive=["Python", "파이썬"])

model.wv.most_similar(positive=["아빠", "여성"], negative=["남성"])[0]

model.wv.most_similar(positive=["왕자", "여성"], negative=["남성"])[0:5]

model.wv.most_similar(positive=["서울", "일본"], negative=["한국"])[0:5]

model.wv.most_similarr(positive=["서울", "중국"], negative=["한국"])[0]

model.wv.most_similar(positive=["오른쪽", "남자"], negative=["왼쪽"])[0]

model.wv.most_similar(positive=["서울", "맛집"], negative=["남성"])[0:5]

model("고양이")
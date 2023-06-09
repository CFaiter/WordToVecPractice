import gensim
import time

from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

start = time.time()
# モデルをロード
model = gensim.models.KeyedVectors.load_word2vec_format('./content/model.vec',binary=False)
end = time.time()
# 解答
ans = "ナポリタン"
# qで終了
while(True):
    start1 = time.time()
    w1 = input("Enter word 1(かな or カナ or 漢字): ")
    if w1 == "q":
        break
    print(f'{w1}と'+f'{ans}の違い')
    target = model.similarity(w1, ans)
    if(target < 0):
        target = 0
    end2 = time.time()
    ans = str(Decimal(str(target*100)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
    print(ans+"%")
    print("所要時間(比較): "+ str(end2-start1))

print("所要時間(モデルダウンロード): "+ str(end-start))

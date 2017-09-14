import re
import difflib
import numpy as np

"""
複数文字列を含む配列において、類似度と尤度の組み合わせから」、もっともよい認識結果の要素をえらぶ
get_similarity():類似度を計算して返す
output_data():認識結果を決定
"""
text_array = ["りんご！！","りんご。","ぱいなっぷる","レブロンジェームズ","りんご","とらい","あいしん","白猫テニスくそ","りんごたべたい","りんごりら"]
likelihood = [2,3,0,0,4,0,0,0,1,0]
difference = [0]*10
result = []
#それぞれの要素の類似度を表示
def get_similarity(text_array):
    #文字列配列の中からそれぞれ類似度を計算して表示
    for i in range(len(text_array)):
        difference = [0 for i in range(len(text_array))]
        for j in range(len(text_array)):
            #i番目の要素について、全要素との類似度を計算
            difference[i] += difflib.SequenceMatcher(None,text_array[i],text_array[j]).ratio()
            #全要素との類似度を格納していく
        result.append(sum(difference))
        #print(difference)
    return result

#print(get_similarity(text_array))
result = get_similarity(text_array)

def output_data(text_array,result,likelihood):
    #numpyに
    nplikelihood = np.array(likelihood)
    npresult = np.array(result)
    #もっとも類似度、尤度が大きいインデックスをとってくる
    correct_index_likelihood = np.argmax(nplikelihood)
    correct_index_result = np.argmax(npresult)
    #尤度の高い順に並べ替え
    nplikelihood = nplikelihood.argsort()[::-1]
    #print(nplikelihood)
    #print("likelihood",correct_index_likelihood,"Similarity:",correct_index_result
    #correct_indexと類似度計算ででたindexが一致するならそれを表示しない場合は尤度が二番目の要素を出力
    if correct_index_likelihood ==  correct_index_result:
        return (text_array[correct_index_likelihood])
    else:
        return (text_array[nplikelihood[1]])

print(output_data(text_array,result,likelihood))

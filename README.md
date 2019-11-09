AtCoder
====
AtCoder:https://atcoder.jp/users/aikiyy 

## Reference
- [AtCoderの問題を分類しました - Qiita](https://qiita.com/KoyanagiHitoshi/items/32dc42d8c5ee75339e54#%E9%99%A4%E6%B3%95)

## DataStructure
- 無向グラフ構造の中での島の数・橋の数を出す
  - ABC075 C
- bit全探索
  - ABC002 D
  
## Algorithms
- しゃくとり
  - ABC032 C
- つるかめ算
  - ABC006 C
- いもす法
  - ABC017 C
- 二分探索
  - ABC030 C
- フェルマーの小定理
  - ABC034 C
- 最小公倍数
  - ABC118 C
- 深さ優先探索(DFS)
  - ATC001 A
- 幅優先探索(BFS)
  - ABC088 D
- 区間スケジューリング
  - ABC103 D
- DP
  - ナップザック問題
    - ABC015 D
  
## Way of Thinking
- ABC117 C

## Modules
| Module | Content |
|--|--|
| itertools.permutations | 順列 |
| itertools.combinations | 組み合わせ |
| itertools.combinations_with_replacement | 重複組み合わせ |
| itertools.product | 直積(入力イテラブルのデカルト積) |
| collections.Counter | |

## Extra
再起回数の上限はデフォルトで1000。DFSでは以下を設定する必要あり。
```
import sys
sys.setrecursionlimit(適当に大きい数) 
```

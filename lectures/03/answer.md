# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：
> 素のLLMでは，それっぽいことを回答していたが，エージェントを用いた回答では正解の回答を行った．
- `--trace` で見えたツール呼び出し（ツール名と引数）：
> [tool call]   search_glossary({'query': 'LoRA'})<br>
> [tool call]   search_glossary({'query': 'QLoRA'})
- 1つの質問での LLM 呼び出し回数（`requests`）：
> requests=2
- 追加したツールと、docstring に書いた説明：
> def make_quiz(lecture: int) -> str:<br>
>     """指定した回の用語から1つを選び、確認問題と答えを返す。<br>
> <br>
>     「第2回の確認問題を出して」のように、復習用の問題を求められたときに使う。<br>
>     """<br>
>     # 1. load_glossary() から lecture が一致する用語を集める<br>
>     # 2. 1つ選ぶ (random.choice)<br>
>     # 3. 問題と答えを文字列で返す (json.dumps など)<br>
>     terms = [entry for entry in load_glossary() if entry["lecture"] == lecture]<br>
>     if not terms:<br>
>         return f"第{lecture}回の用語が見つかりませんでした。"<br>
> <br>
>     term = random.choice(terms)<br>
>     return json.dumps(<br>
>         {<br>
>             "question": f"「{term['term']}」の意味は？",<br>
>             "answer": term["definition"],<br>
>         },<br>
>         ensure_ascii=False,<br>
>     )<br>

## 宿題

- 取り組んだレベル：基礎 / 実装 / 発展
- やったこと：
- 結果：
- 気づき・疑問：

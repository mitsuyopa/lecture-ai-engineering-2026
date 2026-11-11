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

- 取り組んだレベル：
> 実装
- やったこと：
> 学習記録を保存するツールを作成した．
- 結果：
> プロンプト内で「学習記録を保存して」といった言葉を入れたときに，学習記録を保存するツールが動作し，ユーザーに「次の保存を実行しますか？」と保存の確認をしたうえで，ユーザーが"y"や"yes"などとコマンド入力すると記録が保存された．
- 気づき・疑問：
> コマンドプロンプトなどで何かをインストールする際にユーザーの確認を取ってからインストールされる挙動と非常に近いものを実装することができた．これをさらに改良することで，最近のAIエージェントのようにコマンドの実行を許可するかどうかなどの確認を取ったうえで実行するというような挙動についても実装できると考えた．
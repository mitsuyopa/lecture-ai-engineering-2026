# benchmark_gemini.py
import csv
import os
import time
from datetime import datetime, timezone

from google import genai

MODELS = [
    "gemini-3.5-flash-lite",
    "gemini-3.5-flash",
]

QUESTIONS = [
    ("q1", "LoRAとは何ですか？"),
    ("q2", "RAGとファインチューニングの違いを説明してください。"),
    ("q3", "Pythonでリストの重複を除去する方法を説明してください。"),
    ("q4", "AIE2026の講座の宿題にある「3レベル」とは何ですか？"),
    ("q5", "AIE2026の講座で使う「lecNN-start タグ」とは何ですか？"),
    ("q6", "AIE2026の第2回では何を学びますか？"),
]

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

with open("gemini_benchmark.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "timestamp",
            "model",
            "question_id",
            "latency_seconds",
            "prompt_tokens",
            "output_tokens",
            "total_tokens",
            "status",
            "error",
        ],
    )
    writer.writeheader()

    for model in MODELS:
        for question_id, question in QUESTIONS:
            started = time.perf_counter()
            status = "ok"
            error = ""
            prompt_tokens = ""
            output_tokens = ""
            total_tokens = ""

            try:
                response = client.models.generate_content(
                    model=model,
                    contents=question,
                )

                usage = response.usage_metadata
                prompt_tokens = usage.prompt_token_count or 0
                output_tokens = usage.candidates_token_count or 0
                total_tokens = getattr(usage, "total_token_count", None)
                if total_tokens is None:
                    total_tokens = prompt_tokens + output_tokens

            except Exception as exc:
                status = "error"
                error = f"{type(exc).__name__}: {exc}"

            latency = time.perf_counter() - started

            writer.writerow(
                {
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "model": model,
                    "question_id": question_id,
                    "latency_seconds": f"{latency:.3f}",
                    "prompt_tokens": prompt_tokens,
                    "output_tokens": output_tokens,
                    "total_tokens": total_tokens,
                    "status": status,
                    "error": error,
                }
            )
            f.flush()

            print(
                model,
                question_id,
                f"latency={latency:.3f}s",
                f"input={prompt_tokens}",
                f"output={output_tokens}",
                f"total={total_tokens}",
                status,
            )

            # 短時間に無料枠へ集中させないための待ち時間
            time.sleep(10)
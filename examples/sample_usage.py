#!/usr/bin/env python3
"""
Whisper文字起こしの使用例
"""

import sys
import os

# 親ディレクトリをPythonパスに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from transcribe import transcribe_audio, save_result

def main():
    """サンプル実行関数"""
    # 音声ファイルのパス（このパスは実際のファイルに置き換えてください）
    audio_file = "path/to/your/audio/file.mp3"
    
    # 日本語の音声をtinyモデルで文字起こし
    result = transcribe_audio(
        file_path=audio_file,
        model_name="tiny",  # tiny, base, small, medium, large
        language="ja"       # 言語コード（省略可）
    )
    
    # 結果を標準出力に表示
    save_result(result)
    
    # 結果をファイルに保存
    save_result(result, "output.txt")
    
    # セグメント（タイムスタンプ）を表示
    print("\n--- セグメント情報 ---")
    for i, segment in enumerate(result["segments"]):
        print(f"セグメント {i+1}:")
        print(f"  開始時間: {segment['start']:.2f}秒")
        print(f"  終了時間: {segment['end']:.2f}秒")
        print(f"  テキスト: {segment['text']}")

if __name__ == "__main__":
    main()

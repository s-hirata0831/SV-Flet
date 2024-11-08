from datetime import datetime

# 現在の時刻をフォーマットして取得（ミリ秒を省略）
formatted_time = datetime.now().strftime("%H:%M")
print("時刻（フォーマット済み）:", formatted_time)

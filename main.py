import os
import cx_Oracle
import pandas as pd

# --- 設定項目 ---
os.environ["NLS_LANG"] = "JAPANESE_JAPAN.JA16SJISTILDE" # 文字化け防止

HOST = ""
PORT = 
SVS = ""
USER = ""
PASS = ""

sql_query = """
SELECT * FROM "スキーマ名"."テーブル名"
WHERE ROWNUM <= 300　#上から300レコードを取得
"""


# dfを初期化（エラー時に備える）
df = pd.DataFrame()
conn = None
try:
    # 2. データベース接続
    dsn = cx_Oracle.makedsn(HOST, PORT, service_name=SVS)
    conn = cx_Oracle.connect(USER, PASS, dsn)
    
    # 3. データ読み込み
    df = pd.read_sql(sql_query, conn)
    print("データの取得に成功しました。")

except Exception as e:
    print(f"エラーが発生しました: {e}")

finally:
    # 4. 接続を必ず閉じる
    if conn:
        conn.close()

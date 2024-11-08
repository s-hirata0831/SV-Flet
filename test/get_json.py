#------
#JSONファイル取得用プログラム
#------

import asyncio
import websockets
import json

async def receive_json():
    uri = "ws://153.121.41.11:8765"  # VPSのWebSocketサーバーのURI

    try:
        async with websockets.connect(uri) as websocket:
            # サーバーに接続してメッセージを送信
            await websocket.send("Requesting data")

            # サーバーからのJSONデータを受信
            response = await websocket.recv()
            data = json.loads(response)
            item=data[0]['id']
            
            # リスト内の最初の要素から id を取得
            if isinstance(data, list) and len(data) > 0 and 'id' in data[0]:
                print(item)
            else:
                print("ID not found in the response")
                
    except Exception as e:
        print(f"Error: {e}")

# 非同期でクライアントを起動
asyncio.run(receive_json())

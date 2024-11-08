import flet as ft
import threading
import asyncio
import websockets
import json
from datetime import datetime

#表示画面の定義
global widnow
window = 0

#------
#メイン関数
#------
def main(page: ft.Page):
    #------
    #画面サイズ変数
    #------
    #macBookは1470*956
    WIDTH = 1920
    HEIGHT = 1080
    BAR_HEIGHT = HEIGHT * 0.2

    page.title = "SV-Flet for +PLAZA FES"
    page.window_minimizable = False
    page.window_maximizable = True
    page.window_resizable = True
    page.window_full_screen = True
    page.window_always_on_top = True
    page.fonts = {
        "font": "DotGothic16-Regular.ttf",
        "maru": "MPLUSRounded1c-Regular.ttf"
    }

    #------
    #表示内容
    #------
    
    # 時刻表示用のTextオブジェクトを定義
    current_time_text = ft.Text(
        "NowTime",
        font_family="font",
        color=ft.colors.BLACK,
        size=BAR_HEIGHT * 0.25,
        weight=ft.FontWeight.W_900
    )

    SE_yorozuya=[
        ft.VideoMedia("assets\SE01_yorozuya.mp4")
    ]

    #bottomAppbar[標準]
    page.bottom_appbar = ft.BottomAppBar(
        height=BAR_HEIGHT,
        bgcolor=ft.colors.BLUE_100,
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row([
            ft.Column(
                [
                    ft.Image(src="vote.png", height=BAR_HEIGHT*0.7)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                spacing=0,
            ),
            ft.Column(
                [
                    ft.Image(src="live.gif", height=BAR_HEIGHT*0.4),
                    current_time_text
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            ft.Text(
                "+PLAZA FES ライブ配信中",
                font_family="font",
                color=ft.colors.BLACK,
                size=40,
                weight=ft.FontWeight.W_900
            ),
            ft.Column(
                [
                    ft.Text(
                        "2024/11/8",
                        font_family="font",
                        color=ft.colors.BLACK,
                        size=BAR_HEIGHT*0.4,
                        weight=ft.FontWeight.W_900
                    ),
                    ft.Text(
                        "11:11",
                        font_family="font",
                        color=ft.colors.BLACK,
                        size=20,
                        weight=ft.FontWeight.W_900
                    )
                ]
            )
        ],spacing=0)
    )

    #画面表示
    def route_change(e):
        page.views.clear()

        #トップページ
        page.views.append(
            ft.View(
                "/",
                [
                    ft.Container(
                        content=ft.Column([
                            ft.Row([
                                ft.Image(src="SV-Flet.png", height=HEIGHT*0.6, width=WIDTH*0.4),
                                ft.Image(src="plazafes.png", height=HEIGHT*0.6, width=WIDTH*0.4)
                            ],alignment=ft.MainAxisAlignment.CENTER, spacing=0),
                            ft.Row([
                                ft.ElevatedButton(
                                    content=ft.Text(
                                        "Start",
                                        size=60,
                                        font_family="font"
                                    ),
                                    #on_click=open_1
                                )
                            ],alignment=ft.MainAxisAlignment.CENTER, spacing=0),
                            ft.Row([
                                ft.Text(
                                    "v1.0.0",
                                    font_family="font",
                                    color=ft.colors.BLACK,
                                    size=HEIGHT*0.04   ,
                                    weight=ft.FontWeight.W_900
                                )
                            ],alignment=ft.MainAxisAlignment.CENTER, spacing=0),
                        ], alignment=ft.MainAxisAlignment.START, spacing=0),
                        width=WIDTH,
                        height=HEIGHT
                    )
                ],
                bgcolor=ft.colors.BLUE_300
            )
        )

        #ライブ基本画面
        if page.route == "/1":
            page.bottom_appbar = ft.BottomAppBar(
                height=BAR_HEIGHT,
                bgcolor=ft.colors.BLUE_100,
                shape=ft.NotchShape.CIRCULAR,
                content=ft.Row([
                    ft.Column([
                        ft.Image(src="vote.png", height=BAR_HEIGHT*0.7)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    spacing=0
                    ),
                    ft.Column(
                        [
                            ft.Image(src="live.gif", height=BAR_HEIGHT*0.4),
                            current_time_text
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=0
                    ),                    
                ])
            )
            page.views.append(
                ft.View(
                    "/1",
                    [
                        page.bottom_appbar
                    ],
                    bgcolor=ft.colors.BLUE_300
                )
            )

        #SE_よろずや
        if page.route == "/2":
            page.views.append(
                ft.View(
                    "/2",
                    [                      
                        ft.Container(
                            content=ft.Column([
                                ft.Row([
                                    ft.Video(
                                        expand=True,
                                        playlist=SE_yorozuya,
                                        playlist_mode=ft.PlaylistMode.NONE,
                                        aspect_ratio=16/9,
                                        volume=100,
                                        autoplay=True,
                                        filter_quality=ft.FilterQuality.HIGH,
                                        muted=False,
                                        on_loaded=lambda e: print("よろずやSE再生"),
                                        height=HEIGHT,
                                        width=WIDTH,
                                        show_controls=False
                                    )
                                ], alignment=ft.MainAxisAlignment.CENTER, spacing=0)
                            ], alignment=ft.MainAxisAlignment.CENTER, spacing=0)
                        )
                    ],
                    bgcolor=ft.colors.BLACK
                )
            )

        #Art:よろずや
        if page.route == "/3":
            page.bottom_appbar = ft.BottomAppBar(
                height=BAR_HEIGHT,
                bgcolor=ft.colors.BLUE_100,
                shape=ft.NotchShape.CIRCULAR,
                content=ft.Row([
                    ft.Column([
                        ft.Image(src="vote.png", height=BAR_HEIGHT*0.7)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    spacing=0
                    ),
                    ft.Column(
                        [
                            ft.Image(src="live.gif", height=BAR_HEIGHT*0.4),
                            current_time_text
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=0
                    ),
                    ft.Image(src="Art_yorozuya.png"),
                    ft.Column(
                        [
                            ft.Text(
                                "<<Artist>>",
                                font_family="maru",
                                color=ft.colors.BLACK,
                                size=40,
                                weight=ft.FontWeight.W_900
                            ),
                            ft.Text(
                                "よろずや",
                                font_family="maru",
                                color=ft.colors.BLACK,
                                size=BAR_HEIGHT*0.4,
                                weight=ft.FontWeight.W_900
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        spacing=0
                    ),
                    
                ])
            )

            page.views.append(
                ft.View(
                    "/3",
                    [
                        page.bottom_appbar,
                        ft.Container(
                            content=ft.Column([
                                ft.Row([
                                    ft.Image(src="plazafes.png")
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,)
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                        )
                    ],
                    bgcolor=ft.colors.BLUE_300
                )
            )

        page.update()

    #------
    #画面遷移
    #------
    #現在のページを削除して前のページへ戻る
    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    #TOPページへ戻る
    def open_0():
        page.views.pop()
        top_view=page.views[0]
        page.go(top_view.route)

    #ライブ基本画面
    def open_1():
        page.go("/1")

    #SE_よろずや
    def open_2():
        page.go("/2")

    #Art:よろずや
    def open_3():
        page.go("/3")

    
    # 現在時刻を更新する関数
    def update_time():
        # 現在の時刻を取得してフォーマット
        current_time = datetime.now().strftime("%H:%M")
        current_time_text.value = current_time
        if current_time_text.page:
            current_time_text.update()

    #------ WebSocketデータ更新の関数
    async def update_data():
        global window
        uri = "ws://153.121.41.11:8765"
        try:
            async with websockets.connect(uri) as websocket:
                await websocket.send("Requesting data")
                response = await websocket.recv()
                data = json.loads(response)
                item = data[0]['id']
                print(f"データ受信: {item}")
                #時刻取得
                update_time()

                # idがある場合にページ遷移
                if isinstance(data, list) and len(data) > 0 and 'id' in data[0]:
                    if int(item) == 1 and window != 1:
                        print("１を表示します")
                        window = 1
                        open_1()
                    elif int(item) == 2 and window != 2:
                        print("2を表示します")
                        window = 2
                        open_2()
                    elif int(item) == 3 and window != 3:
                        print("3を表示します")
                        window = 3
                        open_3()
                else:
                    print("受信データなし")

        except Exception as e:
            print(f"Error: {e}")

    #------ 定期的にデータ更新
    async def periodic_update():
        while True:
            await update_data()
            await asyncio.sleep(0.5)

    def run_loop():
            loop = asyncio.new_event_loop()  # 新しいイベントループを作成
            asyncio.set_event_loop(loop)  # 現在のスレッドにイベントループを設定
            loop.run_until_complete(periodic_update())  # 非同期タスクを実行

    # 別スレッドで非同期タスクを実行
    threading.Thread(target=run_loop, daemon=True).start()

    #------
    #イベントの登録
    #------
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    #------
    #起動後の処理
    #------
    page.go(page.route)

    periodic_update()
    
#アプリの開始
ft.app(target=main)
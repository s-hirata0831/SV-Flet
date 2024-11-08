import flet as ft
import threading
import asyncio
import websockets
import json

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
        "font": "DotGothic16-Regular.ttf"
    }

    #------
    #表示内容
    #------
    tmp = ft.Text("--°C", font_family="font", color="ft.colors.BLACK", size=35)
    hum = ft.Text("--%", font_family="font", color="ft.colors.BLACK", size=35)

    media=[
        ft.VideoMedia("assets\SE01_yorozuya.mp4")
    ]

    #温度計を表示
    tmpIm = ft.Image(
        src="tmp.png",
        height=HEIGHT*0.3,
        width=WIDTH*0.1,
        fit=ft.ImageFit.CONTAIN
    )

    #bottomkAppbar
    page.bottom_appbar = ft.BottomAppBar(
        height=BAR_HEIGHT,
        bgcolor=ft.colors.BLUE_100,
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row([
            ft.Column(
                [
                    ft.Image(src="live.gif", height=BAR_HEIGHT*0.4),
                    ft.Text(
                        "10:20",
                        font_family="font",
                        color=ft.colors.BLACK,
                        size=BAR_HEIGHT*0.25,
                        weight=ft.FontWeight.W_900
                    )
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
        ])
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
                                    on_click=open_1
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

        #登場動画
        if page.route == "/1":
            page.views.append(
                ft.View(
                    "/1",
                    [                      
                        ft.Container(
                            content=ft.Column([
                                ft.Row([
                                    ft.Video(
                                        expand=True,
                                        playlist=media,
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

        #ライブ配信画面
        if page.route == "/2":
            page.views.append(
                ft.View(
                    "/2",
                    [
                        page.bottom_appbar
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
    def open_0(e):
        page.views.pop()
        top_view=page.views[0]
        page.go(top_view.route)

    #動画
    def open_1():
        page.go("/1")

    #ライブ画面
    def open_2():
        page.go("/2")

    def update_data():
        async def receive_json():
            uri= "ws://153.121.41.11:8765"
            try:
                async with websockets.connect(uri) as websocket:
                    await websocket.send("Requesting data")

                    response = await websocket.recv()
                    data = json.loads(response)
                    item = data[0]['id']

                    if isinstance(data, list) and len(data) > 0 and 'id' in data[0]:
                        f"open_{item}"
                    else:
                        print("受信データなし")

            except Exception as e:
                print(f"Error: {e}")
                
        #ページを更新
        page.update()

    #0.5秒ごとにデータを更新
    def periodic_update():
        update_data()
        threading.Timer(0.5, periodic_update).start()

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
import flet as ft
import threading

#------
#メイン関数
#------
def main(page: ft.Page):
    #------
    #画面サイズ変数
    #------
    #macBookは1470*956_従来は1920*1080
    WIDTH = 1470
    HEIGHT = 956
    BAR_HEIGHT = HEIGHT * 0.2

    page.title = "SV-Flet for +PLAZA FES"
    page.window_minimizable = False
    page.window_maximizable = True
    page.window_resizable = True
    page.window_full_screen = True
    page.window_always_on_top = True
    page.fonts = {
        "font": "/Users/hiratasoma/Documents/linuxEx/Chapter3/DotGothic16-Regular.ttf"
    }

    #------
    #表示内容
    #------
    tmp = ft.Text("--°C", font_family="font", color="ft.colors.BLACK", size=35)
    hum = ft.Text("--%", font_family="font", color="ft.colors.BLACK", size=35)

    media=[
        ft.VideoMedia("/Users/hiratasoma/Documents/SV-Flet/assets/live.mp4")
    ]

    # LIVE
    video = ft.Video(
        expand=True,
        playlist=media,
        playlist_mode=ft.PlaylistMode.LOOP,
        aspect_ratio=16/9,
        volume=100,
        autoplay=True,
        filter_quality=ft.FilterQuality.HIGH,
        muted=False,
        on_loaded=lambda e: print("Video loaded successfully!"),
        on_enter_fullscreen=lambda e: print("Video entered fullscreen"),
        on_exit_fullscreen=lambda e: print("Video exited fullscreen")
    )

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
                                ft.Image(src="SV-Flet.png", height=HEIGHT*0.7, width=WIDTH*0.4),
                                ft.Image(src="plazafes.png", height=HEIGHT*0.7, width=WIDTH*0.4)
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
                        ], alignment=ft.MainAxisAlignment.CENTER, spacing=0),
                        width=WIDTH,
                        height=HEIGHT
                    )
                ],
                bgcolor=ft.colors.BLUE_300
            )
        )
        #ページ更新
        page.update()

        #ライブ画面
        if page.route == "/1":
            page.views.append(
                ft.View(
                    "/1",
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

    #ライブ画面
    def open_1(e):
        page.go("/1")

    def update_data():

        #ページを更新
        page.update()

    #6秒ごとにデータを更新
    def periodic_update():
        update_data()
        threading.Timer(6, periodic_update).start()

    #------
    #イベントの登録
    #------
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    #------
    #起動後の処理
    #------
    page.go(page.route)
   #periodic_update()
    
#アプリの開始
ft.app(target=main)
import flet as ft
import threading

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
        "font": "/Users/hiratasoma/Documents/linuxEx/Chapter3/DotGothic16-Regular.ttf"
    }

    #------
    #表示内容
    #------
    tmp = ft.Text("--°C", font_family="font", color="ft.colors.BLACK", size=35)
    hum = ft.Text("--%", font_family="font", color="ft.colors.BLACK", size=35)

    #温度計を表示
    tmpIm = ft.Image(
        src="tmp.png",
        height=HEIGHT*0.3,
        width=WIDTH*0.1,
        fit=ft.ImageFit.CONTAIN
    )

    #Appbar
    page.bottom_appbar = ft.BottomAppBar(
        height=BAR_HEIGHT,
        bgcolor=ft.colors.BLUE_100,
        content=ft.Row([
            ft.Image(src="tmp.png", height=BAR_HEIGHT * 0.6),
            ft.Text(
                "+PLAZA FES ライブ配信中",
                font_family="font",
                color=ft.colors.BLACK,
                size=40,
                weight=ft.FontWeight.W_900
            )
        ])
    )

    #画面表示
    def route_change(e):
        page.views.clear()

        page.views.append(
            ft.View(
                "/",
                [
                    page.bottom_appbar
                ],
                bgcolor=ft.colors.BLUE_300
            )
        )
        #ページ更新
        page.update()

    #------
    #画面遷移
    #------
    def open_0():
        top_view=page.views[0]
        page.go(top_view.route)

    def update_data():
        t = docTmp.get().to_dict()
        h = docHmd.get().to_dict()
        t_num = t.get('tmpNum', 0)
        h_num = h.get('hmdNum', 0)

        tmp.value = f"{t_num}°C"
        hum.value = f"{h_num}%"
        print("getData")

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

    #------
    #起動後の処理
    #------
    page.go(page.route)
   #periodic_update()
    
#アプリの開始
ft.app(target=main)
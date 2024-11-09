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

        SE_shokotan=[ft.VideoMedia("assets\SE02_shokotan.mp4")]
        #SE_榊原粧子(しょこたん)
        if page.route == "/4":
            page.views.append(
                ft.View(
                    "/4",
                    [                      
                        ft.Container(
                            content=ft.Column([
                                ft.Row([
                                    ft.Video(
                                        expand=True,
                                        playlist=SE_shokotan,
                                        playlist_mode=ft.PlaylistMode.NONE,
                                        aspect_ratio=16/9,
                                        volume=100,
                                        autoplay=True,
                                        filter_quality=ft.FilterQuality.HIGH,
                                        muted=False,
                                        on_loaded=lambda e: print("しょこたんSE再生"),
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

        #Art:しょこたん
        if page.route == "/5":
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
                    ft.Image(src="Art_shokotan.png"),
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
                                "榊原粧子/しょこたん",
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
                    "/5",
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

        SE_arufort=[ft.VideoMedia("assets\SE03_arufort.mp4")]
        #SE_あるふぉ～と
        if page.route == "/6":
            page.views.append(
                ft.View(
                    "/6",
                    [                      
                        ft.Container(
                            content=ft.Column([
                                ft.Row([
                                    ft.Video(
                                        expand=True,
                                        playlist=SE_arufort,
                                        playlist_mode=ft.PlaylistMode.NONE,
                                        aspect_ratio=16/9,
                                        volume=100,
                                        autoplay=True,
                                        filter_quality=ft.FilterQuality.HIGH,
                                        muted=False,
                                        on_loaded=lambda e: print("あるふぉ～とSE再生"),
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

        #Art:あるふぉ～と
        if page.route == "/7":
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
                    ft.Image(src="Art_arufort.png"),
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
                                "あるふぉ～と",
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
                    "/7",
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

        SE_novullets=[ft.VideoMedia("assets\SE04_novullets.mp4")]
        #SE_Novullets
        if page.route == "/8":
            page.views.append(
                ft.View(
                    "/8",
                    [                      
                        ft.Container(
                            content=ft.Column([
                                ft.Row([
                                    ft.Video(
                                        expand=True,
                                        playlist=SE_novullets,
                                        playlist_mode=ft.PlaylistMode.NONE,
                                        aspect_ratio=16/9,
                                        volume=100,
                                        autoplay=True,
                                        filter_quality=ft.FilterQuality.HIGH,
                                        muted=False,
                                        on_loaded=lambda e: print("Novullets SE再生"),
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

        #Art:Novullets
        if page.route == "/9":
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
                    ft.Image(src="Art_novullets.png"),
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
                                "Novullets",
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
                    "/9",
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

        SE_quiet=[ft.VideoMedia("assets\SE05_quiet!.mp4")]
        #SE_Quiet!
        if page.route == "/10":
            page.views.append(
                ft.View(
                    "/10",
                    [                      
                        ft.Container(
                            content=ft.Column([
                                ft.Row([
                                    ft.Video(
                                        expand=True,
                                        playlist=SE_quiet,
                                        playlist_mode=ft.PlaylistMode.NONE,
                                        aspect_ratio=16/9,
                                        volume=100,
                                        autoplay=True,
                                        filter_quality=ft.FilterQuality.HIGH,
                                        muted=False,
                                        on_loaded=lambda e: print("Quiet! SE再生"),
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

        #Art:Quiet!
        if page.route == "/11":
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
                    ft.Image(src="Art_quiet!.png"),
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
                                "Quiet!",
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
                    "/11",
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

        SE_nakajima=[ft.VideoMedia("assets\SE06_nakajima.mp4")]
        #SE_中島清和
        if page.route == "/12":
            page.views.append(
                ft.View(
                    "/12",
                    [                      
                        ft.Container(
                            content=ft.Column([
                                ft.Row([
                                    ft.Video(
                                        expand=True,
                                        playlist=SE_nakajima,
                                        playlist_mode=ft.PlaylistMode.NONE,
                                        aspect_ratio=16/9,
                                        volume=100,
                                        autoplay=True,
                                        filter_quality=ft.FilterQuality.HIGH,
                                        muted=False,
                                        on_loaded=lambda e: print("Quiet! SE再生"),
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

        #Art:中島清和
        if page.route == "/13":
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
                    ft.Image(src="Art_nakajima.png"),
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
                                "中島清和",
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
                    "/13",
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

        SE_littlecrown=[ft.VideoMedia("assets\SE07_littlecrown.mp4")]
        #SE_LittleCrown
        if page.route == "/14":
            page.views.append(
                ft.View(
                    "/14",
                    [                      
                        ft.Container(
                            content=ft.Column([
                                ft.Row([
                                    ft.Video(
                                        expand=True,
                                        playlist=SE_littlecrown,
                                        playlist_mode=ft.PlaylistMode.NONE,
                                        aspect_ratio=16/9,
                                        volume=100,
                                        autoplay=True,
                                        filter_quality=ft.FilterQuality.HIGH,
                                        muted=False,
                                        on_loaded=lambda e: print("LittleCrown SE再生"),
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

        #Art:LittleCrown
        if page.route == "/15":
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
                    ft.Image(src="Art_littlecrown.png"),
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
                                "LittleCrown",
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
                    "/15",
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

        SE_holic=[ft.VideoMedia("assets\SE08_holic.mp4")]
        #SE_HOLIC
        if page.route == "/16":
            page.views.append(
                ft.View(
                    "/16",
                    [                      
                        ft.Container(
                            content=ft.Column([
                                ft.Row([
                                    ft.Video(
                                        expand=True,
                                        playlist=SE_holic,
                                        playlist_mode=ft.PlaylistMode.NONE,
                                        aspect_ratio=16/9,
                                        volume=100,
                                        autoplay=True,
                                        filter_quality=ft.FilterQuality.HIGH,
                                        muted=False,
                                        on_loaded=lambda e: print("HOLIC SE再生"),
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

        #Art:HOLIC
        if page.route == "/17":
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
                    ft.Image(src="Art_holic.png"),
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
                                "HOLIC",
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
                    "/17",
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

        SE_nose=[ft.VideoMedia("assets\SE09_nose.mp4")]
        #SE_nose
        if page.route == "/18":
            page.views.append(
                ft.View(
                    "/18",
                    [                      
                        ft.Container(
                            content=ft.Column([
                                ft.Row([
                                    ft.Video(
                                        expand=True,
                                        playlist=SE_nose,
                                        playlist_mode=ft.PlaylistMode.NONE,
                                        aspect_ratio=16/9,
                                        volume=100,
                                        autoplay=True,
                                        filter_quality=ft.FilterQuality.HIGH,
                                        muted=False,
                                        on_loaded=lambda e: print("nose SE再生"),
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

        #Art:HOLIC
        if page.route == "/19":
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
                    ft.Image(src="Art_nose.png"),
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
                                "野瀬尚史",
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
                    "/19",
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

        SE_murakami=[ft.VideoMedia("assets\SE10_murakami.mp4")]
        #SE_murakami
        if page.route == "/20":
            page.views.append(
                ft.View(
                    "/20",
                    [                      
                        ft.Container(
                            content=ft.Column([
                                ft.Row([
                                    ft.Video(
                                        expand=True,
                                        playlist=SE_murakami,
                                        playlist_mode=ft.PlaylistMode.NONE,
                                        aspect_ratio=16/9,
                                        volume=100,
                                        autoplay=True,
                                        filter_quality=ft.FilterQuality.HIGH,
                                        muted=False,
                                        on_loaded=lambda e: print("murakami SE再生"),
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

        #Art:HOLIC
        if page.route == "/21":
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
                    ft.Image(src="Art_murakami.png"),
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
                                "村上春樹",
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
                    "/21",
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

        SE_rotasu=[ft.VideoMedia("assets\SE11_rotasu.mp4")]
        #SE_rotasu
        if page.route == "/22":
            page.views.append(
                ft.View(
                    "/22",
                    [                      
                        ft.Container(
                            content=ft.Column([
                                ft.Row([
                                    ft.Video(
                                        expand=True,
                                        playlist=SE_rotasu,
                                        playlist_mode=ft.PlaylistMode.NONE,
                                        aspect_ratio=16/9,
                                        volume=100,
                                        autoplay=True,
                                        filter_quality=ft.FilterQuality.HIGH,
                                        muted=False,
                                        on_loaded=lambda e: print("rotasu SE再生"),
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

        #Art:rotasu
        if page.route == "/23":
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
                    ft.Image(src="Art_rotasu.png"),
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
                                "ロータス",
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
                    "/23",
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

        #noMusic:crash
        if page.route == "/24":
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
                    ft.Image(src="Dan_crash.png"),
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
                                "CRASH",
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
                    "/24",
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

    #SE_しょこたん
    def open_4():
        page.go("/4")

    #Art:しょこたん
    def open_5():
        page.go("/5")

    #SE_あるふぉ～と
    def open_6():
        page.go("/6")

    #Art:あるふぉ～と
    def open_7():
        page.go("/7")

    #SE_Novullets
    def open_8():
        page.go("/8")

    #Art:Novullets
    def open_9():
        page.go("/9")

    #SE_Quiet!
    def open_10():
        page.go("/10")

    #Art:Quiet!
    def open_11():
        page.go("/11")

    #SE_中島清和
    def open_12():
        page.go("/12")

    #Art:中島清和
    def open_13():
        page.go("/13")

    #SE_LittleCrown
    def open_14():
        page.go("/14")

    #Art:LittleCrown
    def open_15():
        page.go("/15")

    #SE_HOLIC
    def open_16():
        page.go("/16")

    #Art:HOLIC
    def open_17():
        page.go("/17")
        
    #SE_nose
    def open_18():
        page.go("/18")

    #Art:nose
    def open_19():
        page.go("/19")

    #SE_murakami
    def open_20():
        page.go("/20")

    #Art:murakami
    def open_21():
        page.go("/21")
        
    #SE_rotasu
    def open_22():
        page.go("/22")

    #Art:rotasu
    def open_23():
        page.go("/23")

    #noMusic:crash
    def open_24():
        page.go("/24")
    
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
                    elif int(item) == 4 and window != 4:
                        print("4を表示します")
                        window = 4
                        open_4()
                    elif int(item) == 5 and window != 5:
                        print("5を表示します")
                        window = 5
                        open_5()
                    elif int(item) == 6 and window != 6:
                        print("6を表示します")
                        window = 6
                        open_6()
                    elif int(item) == 7 and window != 7:
                        print("7を表示します")
                        window = 7
                        open_7()
                    elif int(item) == 8 and window != 8:
                        print("8を表示します")
                        window = 8
                        open_8()
                    elif int(item) == 9 and window != 9:
                        print("9を表示します")
                        window = 9
                        open_9()
                    elif int(item) == 10 and window != 10:
                        print("10を表示します")
                        window = 10
                        open_10()
                    elif int(item) == 11 and window != 11:
                        print("11を表示します")
                        window = 11
                        open_11()
                    elif int(item) == 12 and window != 12:
                        print("12を表示します")
                        window = 12
                        open_12()
                    elif int(item) == 13 and window != 13:
                        print("13を表示します")
                        window = 13
                        open_13()
                    elif int(item) == 14 and window != 14:
                        print("14を表示します")
                        window = 14
                        open_14()
                    elif int(item) == 15 and window != 15:
                        print("15を表示します")
                        window = 15
                        open_15()
                    elif int(item) == 16 and window != 16:
                        print("16を表示します")
                        window = 16
                        open_16()
                    elif int(item) == 17 and window != 17:
                        print("17を表示します")
                        window = 17
                        open_17()
                    elif int(item) == 18 and window != 18:
                        print("18を表示します")
                        window = 18
                        open_18()
                    elif int(item) == 19 and window != 19:
                        print("19を表示します")
                        window = 19
                        open_19()
                    elif int(item) == 20 and window != 20:
                        print("20を表示します")
                        window = 20
                        open_20()
                    elif int(item) == 21 and window != 21:
                        print("21を表示します")
                        window = 21
                        open_21()
                    elif int(item) == 22 and window != 22:
                        print("22を表示します")
                        window = 22
                        open_22()
                    elif int(item) == 23 and window != 23:
                        print("23を表示します")
                        window = 23
                        open_23()
                    elif int(item) == 24 and window != 24:
                        window = 24
                        open_24()
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
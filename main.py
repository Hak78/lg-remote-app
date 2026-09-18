import asyncio
import json
import flet as ft

class LGRemoteApp:
    def __init__(self):
        self.tv_ip = "192.168.1.50"
        self.is_connected = False
        self.status_text = ft.Text("الحالة: غير متصل 🔴", color="red", weight=ft.FontWeight.BOLD)

    def build_ui(self, page: ft.Page):
        page.title = "LG Smart Remote"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.theme_mode = ft.ThemeMode.DARK
        page.padding = 20

        # حقل إدخال عنوان IP للتلفاز
        ip_input = ft.TextField(
            label="عنوان IP للتلفاز (TV IP)",
            value=self.tv_ip,
            width=300,
            text_align=ft.TextAlign.CENTER
        )

        def update_ip(e):
            self.tv_ip = ip_input.value

        ip_input.on_change = update_ip

        # زر الاتصال
        def connect_tv(e):
            self.status_text.value = f"الحالة: جاري الاتصال بـ {self.tv_ip}..."
            self.status_text.color = "orange"
            page.update()
            
            # محاكاة الاتصال الفعلي (سيتم ربطه بـ WebSockets لاحقاً)
            page.run_task(self.simulate_connection)

        connect_btn = ft.ElevatedButton(
            text="اتصال بالواي فاي (Connect)",
            icon=ft.icons.WIFI,
            color=ft.colors.WHITE,
            bgcolor=ft.colors.BLUE_700,
            on_click=connect_tv,
            width=250
        )

        # أزرار التحكم (الطاقة، الصوت)
        def send_command(cmd_name):
            if not self.is_connected:
                self.status_text.value = "الحالة: يرجى الاتصال بالتلفاز أولاً!"
                self.status_text.color = "red"
            else:
                self.status_text.value = f"الحالة: تم إرسال الأمر [{cmd_name}] بنجاح ✅"
                self.status_text.color = "green"
            page.update()

        power_btn = ft.IconButton(
            icon=ft.icons.POWER_SETTINGS_NEW,
            icon_color="red",
            icon_size=35,
            tooltip="تشغيل / إيقاف (Power)",
            on_click=lambda e: send_command("POWER")
        )

        vol_up_btn = ft.IconButton(
            icon=ft.icons.VOLUME_UP,
            icon_color="white",
            icon_size=30,
            tooltip="رفع الصوت (Vol+)",
            on_click=lambda e: send_command("VOL_UP")
        )

        vol_down_btn = ft.IconButton(
            icon=ft.icons.VOLUME_DOWN,
            icon_color="white",
            icon_size=30,
            tooltip="خفض الصوت (Vol-)",
            on_click=lambda e: send_command("VOL_DOWN")
        )

        mute_btn = ft.IconButton(
            icon=ft.icons.VOLUME_OFF,
            icon_color="yellow",
            icon_size=30,
            tooltip="كتم الصوت (Mute)",
            on_click=lambda e: send_command("MUTE")
        )

        # ترتيب الواجهة في عناصر بصرية متناسقة
        page.add(
            ft.Text("📱 ريموت تلفاز LG الذكي", size=22, weight=ft.FontWeight.BOLD),
            ft.Divider(height=10, color=ft.colors.TRANSPARENT),
            ip_input,
            connect_btn,
            ft.Divider(height=15, color=ft.colors.TRANSPARENT),
            self.status_text,
            ft.Divider(height=20, color=ft.colors.TRANSPARENT),
            ft.Row([power_btn, mute_btn], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
            ft.Row([vol_up_btn, vol_down_btn], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
        )

    async def simulate_connection(self):
        await asyncio.sleep(1.5)
        self.is_connected = True
        self.status_text.value = "الحالة: متصل بنجاح 🟢"
        self.status_text.color = "green"


def main(page: ft.Page):
    app = LGRemoteApp()
    app.build_ui(page)

if __name__ == "__main__":
    ft.app(target=main)

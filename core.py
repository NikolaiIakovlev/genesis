class App:
    def __init__(self, title):
        self.title = title
        self.platform = self.detect_platform()
        self.root_widget = None

    def detect_platform(self):
        # Определяем платформу (Android или iOS)
        import sys
        if 'android' in sys.platform:
            from .platforms.android import AndroidPlatform
            return AndroidPlatform()
        elif 'ios' in sys.platform:
            from .platforms.ios import IOSPlatform
            return IOSPlatform()
        else:
            raise Exception("Платформа не поддерживается")

    def run(self):
        # Запуск приложения
        self.platform.run_app(self)

    def set_root_widget(self, widget):
        # Устанавливаем корневой виджет
        self.root_widget = widget
        self.platform.render_widget(widget)
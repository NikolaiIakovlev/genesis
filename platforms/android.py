# platforms/android.py
class AndroidPlatform:
    def run_app(self, app):
        print("Запуск приложения на Android")
        self.render_widget(app.root_widget)

    def render_widget(self, widget):
        widget.render(self)

    def create_button(self, text, on_press):
        from jnius import autoclass
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Button = autoclass('android.widget.Button')
        button = Button(PythonActivity.mActivity)
        button.setText(text)
        button.setOnClickListener(lambda view: on_press())
        PythonActivity.mActivity.addContentView(button)

# platforms/ios.py
class IOSPlatform:
    def run_app(self, app):
        print("Запуск приложения на iOS")
        self.render_widget(app.root_widget)

    def render_widget(self, widget):
        widget.render(self)

    def create_button(self, text, on_press):
        from rubicon.objc import ObjCClass
        UIButton = ObjCClass('UIButton')
        button = UIButton.buttonWithType_(0)
        button.setTitle_forState_(text, 0)
        button.addTarget_action_forControlEvents_(on_press, None, 1 << 6)
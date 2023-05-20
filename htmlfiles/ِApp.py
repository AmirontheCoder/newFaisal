import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 2
    #Add widgets
        self.add_widget(Label(text = "Name :"))
    #Add input widgets
        self.name = TextInput(multiline = False)
        self.add_widget(self.name)

        if self.name != str:
            self.name.text = "Invalid input retry"

        self.add_widget(Label(text = "Last Name :"))
    #Add input widgets
        self.Lastname = TextInput(multiline = False, input_filter = "str")
        self.add_widget(self.Lastname)

        self.add_widget(Label(text = "Age :"))
    #Add input widgets
        self.age = TextInput(multiline = False , input_filter = "int")
        self.add_widget(self.age)

        self.submit = Button(text = "Submit" , font_size = 25 )

        self.submit.bind(on_press = self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text 
        Lastname = self.Lastname.text
        Age = self.age.text

        print(f" Hello {name} {Lastname}, You are {Age} years old!")
        self.add_widget(Label(text=f"Hello {name} {Lastname},You are {Age} years old!"))

        self.name.text = ""
        self.Lastname.text = ""
        self.age.text = ""



class HelloKivyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__' :
    HelloKivyApp().run()


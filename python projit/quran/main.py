from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
import arabic_reshaper
from bidi.algorithm import get_display
import webbrowser as wb
import kivy


Window.size = 350, 600


Builder.load_file("design.kv")

class StartScreen(Screen, Widget):
    bidi_text = StringProperty('')

    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
        reshpaed_text = arabic_reshaper.reshape(u"بسم الله الرحمن الرحيم")
        self.bidi_text1 =get_display(reshpaed_text)
        reshpaed_text = arabic_reshaper.reshape(u"المسبحة الرقمية")
        self.bidi_text2 = get_display(reshpaed_text)
        reshpaed_text = arabic_reshaper.reshape(u"القران الكريم")
        self.bidi_text3 = get_display(reshpaed_text)
        reshpaed_text = arabic_reshaper.reshape(u"كتب السنة النبوية الشريفة ")
        self.bidi_text4 = get_display(reshpaed_text)
        reshpaed_text = arabic_reshaper.reshape(u"  بسم الله الرحمن الرحيم")
        self.bidi_text5 = get_display(reshpaed_text)

    def mpage(self):
        self.manager.current = "masbha_page"

    def qbook(self):
        self.manager.current = "quran_book"

    def sbook(self):
        self.manager.current = "sonna_book_screen"

class RootWidget(ScreenManager):
    pass

class MasbhaPage(Screen, Widget):
    bidi_text6 = StringProperty('')
    bidi_text7 = StringProperty('')
    bidi_text14 = StringProperty('')
    bidi_text15 = StringProperty('')

    def out(self):
        self.manager.current = "start_screen"

    def __init__(self, **kwargs):
        super(MasbhaPage, self).__init__(**kwargs)

        reshpaed_text = arabic_reshaper.reshape(u"<< رجوع للخلف")
        self.bidi_text6 = get_display(reshpaed_text)
        reshpaed_text = arabic_reshaper.reshape(u"عداد السبحة")
        self.bidi_text7 = get_display(reshpaed_text)
        reshpaed_text = arabic_reshaper.reshape(u"اضغط ")
        self.bidi_text14 = get_display(reshpaed_text)
        reshpaed_text = arabic_reshaper.reshape(u"التصفير الرقم")
        self.bidi_text15 = get_display(reshpaed_text)

    def n_plus(self):
        value = self.ids.lbl.text
        self.ids.lbl.text = str(int(value)+1)

    def zero(self):
        value= self.ids.lbl.text
        self.ids.lbl.text = "0"


class QuranBook(Screen, Widget):
    bidi_text9 = StringProperty('')
    bidi_text7 = StringProperty('')
    bidi_text17 = StringProperty('')

    def out1(self):
        self.manager.current= "start_screen"

    def __init__(self, **kwargs):
        super(QuranBook, self).__init__(**kwargs)
        reshpaed_text = arabic_reshaper.reshape(u"القران الكريم")
        self.bidi_text9 = get_display(reshpaed_text)
        reshpaed_text = arabic_reshaper.reshape(u"<< رجوع للخلف")
        self.bidi_text7 = get_display(reshpaed_text)
        reshpaed_text = arabic_reshaper.reshape(u"بسم الله الرحمن الرحيم")
        self.bidi_text17 = get_display(reshpaed_text)

    def readg(self):
        wb.open_new(r'Quran.pdf')


class SonnaBookScreen(Screen, Widget):
    bidi_text8 = StringProperty('')
    bidi_text10 = StringProperty('')
    bidi_text11 = StringProperty('')
    bidi_text12 = StringProperty('')
    bidi_text13 = StringProperty('')

    def out3(self):
        self.manager.current = "start_screen"

    def __init__(self, **kwargs):
        super(SonnaBookScreen, self).__init__(**kwargs)
        reshpaed_text = arabic_reshaper.reshape(u"<< رجوع للخلف")
        self.bidi_text8 = get_display(reshpaed_text)
        reshpaed_text = arabic_reshaper.reshape(u"الصحيح من احاديت السيرة النبوية")
        self.bidi_text10 = get_display(reshpaed_text)
        reshpaed_text = arabic_reshaper.reshape(u"السنة النبوية في الشريعة الاسلامية")
        self.bidi_text11 = get_display(reshpaed_text)
        reshpaed_text = arabic_reshaper.reshape(u"زبدة السيرة النبوية")
        self.bidi_text12 = get_display(reshpaed_text)
        reshpaed_text = arabic_reshaper.reshape(u"السنة النبوية بين اهل الفقه واهل الحديث")
        self.bidi_text13 = get_display(reshpaed_text)

    def reads1(self):
        wb.open_new(r'sahih_ahadis.pdf')

    def reads2(self):
        wb.open_new(r'syra_nabwya1.pdf')

    def reads3(self):
        wb.open_new(r'syra_nabwya2.pdf')

    def reads4(self):
        wb.open_new(r'syra_nabwya3.pdf')


class Main(App):
    def build(self):
        self.title ="Quran"
        return RootWidget()


if __name__=="__main__":
    Main().run()

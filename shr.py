from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.textinput import TextInput
from kivy.uix.switch import Switch
import threading
import os
import random
class ShifApp(App):
    def callback(self,instance, value):
        if self.ghi==0:
            self.ghi=1
        elif self.ghi==1:
            self.ghi=0
    def sg(self,args):
        alfaw=['A','B','C','D','E','F','G','L','J','K','I','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','l','j','k','i','m','n','o','p','q','r','s','t','u','v','w','x','y','z','А','Б','В','Г','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я','а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',' ',',','.','<','>',':',';','?','/','!','@','#','№','$','|','%','&','*','(',')','-','+','_','=','^','0','1','2','3','4','5','6','7','8','9']
        j=self.t.text
        kwo=len(alfaw)
        try:
            j=int(j)
            if j>1000:
                threading.Thread(target=lambda: os.system('ош1.py')).start()
            elif j>0 and j<1001:
                skr=0
                y=''
                ir=""
                for gh in range(kwo):
                    ir=alfaw[skr]
                    file=open('Shif/'+str(skr)+'.txt','w')
                    file.close()
                    for e in range(j):
                        q=random.randint(0, kwo-1)
                        y=alfaw[q]
                        file=open('Shif/'+str(skr)+'.txt','a')
                        file.write(str(y))
                        file.close()
                    skr+=1
                threading.Thread(target=lambda: os.system('увед.py')).start()
            elif j<0 or j==0:
                threading.Thread(target=lambda: os.system('ошm.py')).start()
            else:
                threading.Thread(target=lambda: os.system('ош.py')).start()
        except:
            threading.Thread(target=lambda: os.system('ош2.py')).start()
    def ssh(self,args):
        alfawsh=['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
        alfaw=['A','B','C','D','E','F','G','L','J','K','I','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','l','j','k','i','m','n','o','p','q','r','s','t','u','v','w','x','y','z','А','Б','В','Г','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я','а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',' ',',','.','<','>',':',';','?','/','!','@','#','№','$','|','%','&','*','(',')','-','+','_','=','^','0','1','2','3','4','5','6','7','8','9']
        kwo=len(alfaw)
        st=0
        br=0
        bz=0
        dn=""
        for i in range(kwo):
            file=open('Shif/'+str(st)+".txt","r")
            dn=file.read()
            file.close()
            alfawsh[st]=dn
            st+=1
        ft=self.ti.text
        zr=len(ft)
        file=open("зашифровано.txt","w")
        file.close()
        for iz in range(zr):
            br=0
            for e in range(kwo):
                if ft[bz]==alfaw[br]:
                    file=open("зашифровано.txt","a")
                    file.write(alfawsh[br])
                    file.close()
                    break
                br+=1
            bz+=1
        file=open("зашифровано.txt","r")
        self.tp.text=file.read()
        file.close()
        self.tp.text 
    def ssr(self,args):
        alfawsh=['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
        alfaw=['A','B','C','D','E','F','G','L','J','K','I','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','l','j','k','i','m','n','o','p','q','r','s','t','u','v','w','x','y','z','А','Б','В','Г','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я','а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',' ',',','.','<','>',':',';','?','/','!','@','#','№','$','|','%','&','*','(',')','-','+','_','=','^','0','1','2','3','4','5','6','7','8','9']
        kwo=len(alfaw)
        st=0
        bn=0
        dn=""
        pahz=""
        yz=""
        hj=0
        for i in range(kwo):
            file=open('Shif/'+str(st)+".txt","r")
            dn=file.read()
            file.close()
            alfawsh[st]=dn
            st+=1
        fz=self.ti.text
        file=open('Shif/'+"128.txt","r")
        tr=file.read()
        file.close()
        ul=len(tr)
        gh=len(fz)/ul
        for i in range(int(gh)):
            for hu in range(ul):
                yz+=fz[hj]
                hj+=1
            for i in range(0,kwo):
                if yz==alfawsh[i]:
                    pahz+=alfaw[i]
                    break
            yz=""
        file=open("раскодировано.txt","w")
        file.write(pahz)
        file.close()
        file=open("раскодировано.txt","r")
        self.tp.text=file.read()
        file.close()
    def build(self):
        self.ghi=0
        bl=BoxLayout(orientation="vertical")
        gr=GridLayout(cols=7,size_hint=(1,.1))
        self.t=TextInput(text="")
        gr.add_widget(self.t)
        gr.add_widget(Button(text="Cгенерировать",on_press=self.sg,size_hint=(1.1,.05)))
        gr.add_widget(Button(text="сохранить"))
        gr.add_widget(Button(text="зашифровать",on_press=self.ssh))
        gr.add_widget(Button(text="расшифровать",on_press=self.ssr,size_hint=(1.1,.05)))
        bl.add_widget(gr)
        self.ti=TextInput()
        self.tp=TextInput()
        bl.add_widget(self.ti)
        bl.add_widget(self.tp)
        return bl
if __name__=="__main__":
    ShifApp().run()

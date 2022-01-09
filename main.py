
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.popup import Popup
import socket
import select
import sys
from threading import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class MainWindow(App):
    def build(self):

        # main window color setting
        Window.clearcolor=(0, 0.6, 0.8, 0.1)

        # grid parameters
        self.window=GridLayout()
        self.window.cols=1
        self.window.padding=(100,100)
        self.window.spacing=(20,20)

        # server IP input textbox (first read IP from server UI)
        self.serverIpAddres=TextInput(multiline=False, text='192.168.1.14',halign="center",font_size='80')
        self.serverIpAddres.height=(10)
        self.window.add_widget(self.serverIpAddres)

        # bed number (to change the number you need to restart the client)
        self.bedNumber = TextInput(multiline=False, text= 'Wprowadź numer łóżka',halign="center",font_size='80')
        self.window.add_widget(self.bedNumber)

        # login button settings
        self.loginButton = Button(text='POŁĄCZ')
        self.loginButton.background_color=[1,1,1,1]
        self.loginButton.background_color=[1,1,1,.6]
        self.loginButton.bind(on_press=self.ConnectToServer)
        self.window.add_widget(self.loginButton)

        # N priority button settings
        self.nPriorityButton = Button(text='NORMALNY')
        self.nPriorityButton.background_color=[0,1,0,1]
        self.nPriorityButton.bind(on_press=self.nPriorityButtonOnClick)
        self.window.add_widget(self.nPriorityButton)
        self.nPriorityButton.disabled = True

        # P priority button settings
        self.pPriorityButton = Button(text='PILNY')
        self.pPriorityButton.background_color=[1,0.5,0,1]
        self.pPriorityButton.bind(on_press=self.pPriorityButtonOnClick)
        self.pPriorityButton.disabled = True
        self.window.add_widget(self.pPriorityButton)

        # PP priority button settings
        self.ppPriorityButton = Button(text='BARDZO PILNY')
        self.ppPriorityButton.background_color=[1,0,0,1]
        self.ppPriorityButton.bind(on_press=self.ppPriorityButtonOnClick)
        self.ppPriorityButton.disabled = True
        self.window.add_widget(self.ppPriorityButton)



        return self.window

    # loginButton OnClick method (here app connects to server by using IP addres from serverIpAddres input)
    def ConnectToServer(self,instance):
        ipAddres = self.serverIpAddres.text
        server.connect((str(ipAddres), 8081))
        self.serverIpAddres.disabled = True
        self.bedNumber.disabled = True
        self.loginButton.disabled = True
        self.nPriorityButton.disabled = False
        self.pPriorityButton.disabled = False
        self.ppPriorityButton.disabled = False



    def nPriorityButtonOnClick(self,instance):
        message=self.bedNumber.text+";"+"N"
        server.send(bytes(message,'utf-8'))

    def pPriorityButtonOnClick(self,instance):
        message=self.bedNumber.text+";"+"P"
        server.send(bytes(message,'utf-8'))

    def ppPriorityButtonOnClick(self,instance):
        message=self.bedNumber.text+";"+"PP"
        server.send(bytes(message,'utf-8'))



# Run message listener in separate thread (IMPORTANT)
#def ListenerToThread():
#    t1 = Thread(target=MessageListener)
  #  t1.start()

#def MessageListener():

 #   while True:
     #   sockets_list = [sys.stdin, server]
       # read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])
        #for socks in read_sockets:
         #   if socks == server:
        #        message = socks.recv(8)
       #         if str.__contains__(message.decode('utf-8'),'OK'):
      #              popup = Popup(title='Sukces',
     #                             content=Label(text='POMOC JUŻ W DRODZE!'),
    #                              separator_color=[0, 1, 1, 0.9],
   #                               background_color=[1, 1, 1, 0.3],
  #                                size_hint=(None, None), size=(500, 500))
 #                   popup.open()
#
        #        if str.__contains__(message.decode('utf-8'),'Conne'):
       #             # popup
      #              popup2 = Popup(title='Sukces',
     #                             content=Label(text='Nawiązano łączność z serwerem!'),
    #                              separator_color=[0, 1, 1, 0.9],
   #                               background_color=[1, 1, 1, 0.3],
  #                                size_hint=(None, None), size=(500, 500))
 #                   popup2.open()
#
#    server.close()


#ListenerToThread()
MainWindow().run()

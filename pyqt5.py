
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CHATTING APP MADE BY GEEKS")
        self.setGeometry(0,0,2000,1000) #here 4  arguements needed to  be passed, x and y refer to the coordinates 
#where we want the window to appear and then followed by height,width for the dimensions of the window.0,0 corresponds to the top
        self.setWindowIcon(QIcon("C:\Users\User\Desktop\Screenshot (624)"))


        
def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()


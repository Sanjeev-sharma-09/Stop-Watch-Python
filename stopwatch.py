import sys 
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QApplication, QPushButton
from PyQt5.QtCore import Qt, QTimer, QTime

class StopWatch(QWidget):

    def __init__(self):

        super().__init__()
        self.timeLabel= QLabel("00:00:00.00", self)
        self.time= QTime(0, 0, 0, 0)
        self.timer= QTimer(self)
        
        #Buttons
        self.startButton= QPushButton("Start", self)
        self.stopButton= QPushButton("Stop", self)
        self.resetButton= QPushButton("Reset", self)

        self.initUI()

    #Design Windows UI
    def initUI(self):
        #Window Settings
        self.setWindowTitle("Stop Watch")
        self.setGeometry(700, 350, 600, 350)

        vbox= QVBoxLayout()
        vbox.addWidget(self.timeLabel)
        self.setLayout(vbox)

        hbox= QHBoxLayout()
        hbox.addWidget(self.startButton)
        hbox.addWidget(self.stopButton)
        hbox.addWidget(self.resetButton)
        #Align Buttons vertically to 
        vbox.addLayout(hbox)

        #Alignment
        self.timeLabel.setAlignment(Qt.AlignCenter)

        #Setting Button object name for Styling
        self.startButton.setObjectName("StartButton")
        self.stopButton.setObjectName("StopButton")
        self.resetButton.setObjectName("ResetButton")

        #Design the UI
        self.setStyleSheet("""
            QPushButton, QLabel{
                padding: 20px;               
            }
            QPushButton{
                font-size: 35px;
                font-weight: bold;
                border: 2.5px solid black;
                border-radius: 20px                 
            }
            QPushButton#StartButton{
                background-color: hsl(110, 90%, 55%);               
            }
            QPushButton#StartButton:hover{
                background-color: hsl(110, 90%, 75%);               
            }
            QPushButton#StopButton{
                background-color: hsl(0, 100%, 38%);               
            }
            QPushButton#StopButton:hover{
                background-color: hsl(0, 100%, 58%);               
            }
            QPushButton#ResetButton{
                background-color: hsl(208, 100%, 38%);               
            }
            QPushButton#ResetButton:hover{
                background-color: hsl(208, 100%, 58%);               
            }
            QLabel{
                font-size: 80px;
                color: #2bd65e;
                background-color: #252626;
                border: 2.5px solid black;
                border-radius: 20px               
            }
        """)

        #Function performed when Button is clicked
        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)
        self.resetButton.clicked.connect(self.reset)
        self.timer.timeout.connect(self.updateDisplay)


    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time= QTime(0, 0, 0, 0)
        self.timeLabel.setText(self.formatTime(self.time))

    def updateDisplay(self):
        self.time= self.time.addMSecs(10)
        self.timeLabel.setText(self.formatTime(self.time))

    def formatTime(self, time):
        hours= time.hour()
        minutes= time.minute()
        seconds= time.second()
        milliseconds= time.msec() // 10 #To show only two digits 
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

def main():
    
    app= QApplication(sys.argv)
    stopwatch= StopWatch()
    #Shows the window 
    stopwatch.show()
    #Executes the window
    sys.exit(app.exec_())

if __name__== "__main__":
    main()
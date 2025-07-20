import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QPushButton, QLabel, QListWidget, 
                             QStackedWidget, QMessageBox)

class ChatApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Chat Application')
        self.setGeometry(100, 100, 400, 500)
        
        # Stacked widgets to handle different views
        self.stackedLayout = QStackedWidget()
        
        # Sign In Page (default view)
        self.signInPage = QWidget()
        self.setupSignIn()
        self.stackedLayout.addWidget(self.signInPage)
        
        # Sign Up Page
        self.signUpPage = QWidget()
        self.setupSignUp()
        self.stackedLayout.addWidget(self.signUpPage)
        
        # Contacts Page
        self.contactsPage = QWidget()
        self.setupContacts()
        self.stackedLayout.addWidget(self.contactsPage)
        
        # Main layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.stackedLayout)
        self.setLayout(mainLayout)
    
    def setupSignIn(self):
        layout = QVBoxLayout()
        
        header = QLabel("Welcome to ChatApp")
        header.setStyleSheet("font-size: 20px; font-weight: bold;")
        
        self.usernameInput = QLineEdit()
        self.usernameInput.setPlaceholderText("Username")
        
        self.passwordInput = QLineEdit()
        self.passwordInput.setPlaceholderText("Password")
        self.passwordInput.setEchoMode(QLineEdit.Password)
        
        signInButton = QPushButton("Sign In")
        signInButton.clicked.connect(self.handleSignIn)
        
        signUpButton = QPushButton("Create Account")
        signUpButton.clicked.connect(lambda: self.stackedLayout.setCurrentIndex(1))  # Go to sign-up
        
        layout.addWidget(header)
        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.usernameInput)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.passwordInput)
        layout.addWidget(signInButton)
        layout.addWidget(signUpButton)
        
        self.signInPage.setLayout(layout)
    
    def setupSignUp(self):
        layout = QVBoxLayout()
        
        header = QLabel("Create New Account")
        header.setStyleSheet("font-size: 20px; font-weight: bold;")
        
        self.newUsername = QLineEdit()
        self.newUsername.setPlaceholderText("Username")
        
        self.newPassword = QLineEdit()
        self.newPassword.setPlaceholderText("Password")
        self.newPassword.setEchoMode(QLineEdit.Password)
        
        self.confirmPassword = QLineEdit()
        self.confirmPassword.setPlaceholderText("Confirm Password")
        self.confirmPassword.setEchoMode(QLineEdit.Password)
        
        signUpButton = QPushButton("Submit")
        signUpButton.clicked.connect(self.handleSignUp)
        
        backButton = QPushButton("Back to Sign In")
        backButton.clicked.connect(lambda: self.stackedLayout.setCurrentIndex(0))
        
        layout.addWidget(header)
        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.newUsername)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.newPassword)
        layout.addWidget(QLabel("Confirm Password:"))
        layout.addWidget(self.confirmPassword)
        layout.addWidget(signUpButton)
        layout.addWidget(backButton)
        
        self.signUpPage.setLayout(layout)
    
    def setupContacts(self):
        layout = QVBoxLayout()
        
        self.contactsList = QListWidget()
        self.contactsList.addItems(["Alice", "Bob", "Charlie", "David"])
        
        logoutButton = QPushButton("Logout")
        logoutButton.clicked.connect(lambda: self.stackedLayout.setCurrentIndex(0))
        
        layout.addWidget(QLabel("Your Contacts:"))
        layout.addWidget(self.contactsList)
        layout.addWidget(logoutButton)
        
        self.contactsPage.setLayout(layout)
    
    def handleSignIn(self):
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        
        # Simple validation (replace with database check)
        if username and password:
            self.stackedLayout.setCurrentIndex(2)  # Go to contacts
        else:
            QMessageBox.warning(self, "Error", "Please enter both username and password")
    
    def handleSignUp(self):
        username = self.newUsername.text()
        password = self.newPassword.text()
        confirm = self.confirmPassword.text()
        
        if not username or not password:
            QMessageBox.warning(self, "Error", "Username and password are required")
        elif password != confirm:
            QMessageBox.warning(self, "Error", "Passwords do not match")
        else:
            QMessageBox.information(self, "Success", "Account created successfully!")
            self.stackedLayout.setCurrentIndex(0)  # Return to sign-in
            self.newUsername.clear()
            self.newPassword.clear()
            self.confirmPassword.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChatApp()
    window.show()
    sys.exit(app.exec_())

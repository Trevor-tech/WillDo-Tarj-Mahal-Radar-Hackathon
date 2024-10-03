import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QMessageBox

class WillCreator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WillDo - Online Will Creator")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Name input
        name_layout = QHBoxLayout()
        name_label = QLabel("Full Name:")
        self.name_input = QLineEdit()
        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_input)
        layout.addLayout(name_layout)

        # Will content
        will_label = QLabel("Enter your will:")
        self.will_content = QTextEdit()
        layout.addWidget(will_label)
        layout.addWidget(self.will_content)

        # Submit button
        submit_button = QPushButton("Submit Will to Blockchain")
        submit_button.clicked.connect(self.submit_will)
        layout.addWidget(submit_button)

    def submit_will(self):
        name = self.name_input.text()
        will = self.will_content.toPlainText()

        if not name or not will:
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
            return

        # Mock blockchain submission
        success = self.submit_to_blockchain(name, will)

        if success:
            QMessageBox.information(self, "Success", "Your will has been submitted to the blockchain.")
            self.name_input.clear()
            self.will_content.clear()
        else:
            QMessageBox.critical(self, "Error", "Failed to submit will to the blockchain. Please try again.")

    def submit_to_blockchain(self, name, will):
        # This is a mock function. In a real application, you would implement
        # actual blockchain submission logic here.
        print(f"Submitting will for {name} to the blockchain:")
        print(will)
        return True  # Always return True for this mock implementation

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WillCreator()
    window.show()
    sys.exit(app.exec_())

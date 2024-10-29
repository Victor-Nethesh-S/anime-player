import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QHBoxLayout, QLabel, QPushButton, QTextEdit, QListWidget)


class AnimeSyncUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Anime Sync Tool")
        self.setGeometry(100, 100, 800, 600)
        
        # Main layout
        main_layout = QVBoxLayout()
        
        # Playback area
        playback_label = QLabel("Playback Area")
        playback_label.setFixedHeight(300)
        playback_label.setStyleSheet("background-color: #202020; color: white; font-size: 16px;")
        main_layout.addWidget(playback_label)
        
        # Control panel
        controls_layout = QHBoxLayout()
        play_button = QPushButton("Play")
        pause_button = QPushButton("Pause")
        sync_button = QPushButton("Sync")
        volume_button = QPushButton("Volume")
        controls_layout.addWidget(play_button)
        controls_layout.addWidget(pause_button)
        controls_layout.addWidget(sync_button)
        controls_layout.addWidget(volume_button)
        
        main_layout.addLayout(controls_layout)
        
        # Chat and Queue panel
        bottom_layout = QHBoxLayout()
        
        # Chat window
        chat_box = QTextEdit()
        chat_box.setPlaceholderText("Chat here...")
        chat_box.setFixedWidth(300)
        bottom_layout.addWidget(chat_box)
        
        # Queue list
        queue_list = QListWidget()
        queue_list.addItem("Upcoming Video 1")
        queue_list.addItem("Upcoming Video 2")
        queue_list.setFixedWidth(200)
        bottom_layout.addWidget(queue_list)
        
        main_layout.addLayout(bottom_layout)

        # Set central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)


# Run the application
app = QApplication(sys.argv)
window = AnimeSyncUI()
window.show()
sys.exit(app.exec())

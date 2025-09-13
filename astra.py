# chat_window.py
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QLabel, QScrollArea, QFrame
)
from PyQt5.QtCore import QObject, QThread, pyqtSignal, Qt, QTimer
from PyQt5.QtGui import QFont, QPixmap, QColor, QPainter, QBrush, QPen

from agent import run_agent_command


# Worker thread for agent calls
class Worker(QObject):
    finished = pyqtSignal(str)

    def __init__(self, text: str):
        super().__init__()
        self.text = text

    def run(self):
        try:
            response = run_agent_command(self.text)
        except Exception as e:
            response = f"Error: {e}"
        self.finished.emit(response)


# Helper: Create circular avatar pixmap
def make_avatar(initials: str, size=32, color="#0078D7"):
    pix = QPixmap(size, size)
    pix.fill(Qt.transparent)
    p = QPainter(pix)
    p.setRenderHint(QPainter.Antialiasing)
    p.setBrush(QBrush(QColor(color)))
    p.setPen(Qt.NoPen)
    p.drawEllipse(0, 0, size, size)
    p.setPen(QPen(Qt.white))
    font = QFont("Segoe UI", int(size * 0.45), QFont.Bold)
    p.setFont(font)
    fm = p.fontMetrics()
    tw = fm.horizontalAdvance(initials)
    th = fm.ascent()
    # 👇 cast to int so PyQt accepts it
    p.drawText(int((size - tw) / 2), int((size + th) / 2), initials)
    p.end()
    return pix



# Chat bubble widget
class ChatBubble(QFrame):
    def __init__(self, text: str, is_user: bool, avatar: QPixmap, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background: transparent;")
        layout = QHBoxLayout(self)
        layout.setContentsMargins(8, 4, 8, 4)
        layout.setSpacing(6)

        avatar_label = QLabel()
        avatar_label.setPixmap(avatar)
        avatar_label.setFixedSize(32, 32)

        msg = QLabel(text)
        msg.setWordWrap(True)
        msg.setFont(QFont("Segoe UI", 10))
        msg.setStyleSheet(
            "padding: 8px 12px; border-radius: 12px;"
            f"background-color: {'#0b7285' if is_user else '#1f2937'};"
            "color: white;"
        )
        msg.setTextInteractionFlags(Qt.TextSelectableByMouse)

        if is_user:
            layout.addStretch()
            layout.addWidget(msg)
            layout.addWidget(avatar_label)
        else:
            layout.addWidget(avatar_label)
            layout.addWidget(msg)
            layout.addStretch()


# Main Chat Window
class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desktop Automation Agent")
        self.resize(500, 600)
        self.setStyleSheet("background-color: #121212;")

        self.user_avatar = make_avatar("U", color="#0b7285")
        self.agent_avatar = make_avatar("AI", color="#0078D7")

        # Layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(6)

        # Scroll area for chat
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("border: none;")

        self.chat_container = QFrame()
        self.chat_layout = QVBoxLayout(self.chat_container)
        self.chat_layout.setAlignment(Qt.AlignTop)
        self.scroll_area.setWidget(self.chat_container)
        main_layout.addWidget(self.scroll_area)

        # Typing indicator
        self.typing_label = QLabel("")
        self.typing_label.setStyleSheet("color: #aaa; font-style: italic;")
        main_layout.addWidget(self.typing_label)

        # Input area
        input_layout = QHBoxLayout()
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Type your command...")
        self.input_box.setStyleSheet(
            "padding: 10px; border-radius: 15px; border: 1px solid #333;"
            "background-color: #1e1e1e; color: #eee;"
        )
        self.input_box.returnPressed.connect(self.send_message)

        self.send_button = QPushButton("Send")
        self.send_button.setStyleSheet(
            "background-color: #0078D7; color: white; padding: 10px 18px;"
            "border-radius: 15px;"
        )
        self.send_button.clicked.connect(self.send_message)

        input_layout.addWidget(self.input_box)
        input_layout.addWidget(self.send_button)
        main_layout.addLayout(input_layout)

        # Typing animation
        self._typing_dots = 0
        self._typing_timer = QTimer()
        self._typing_timer.timeout.connect(self._update_typing)

    def add_message(self, text: str, is_user: bool):
        bubble = ChatBubble(text, is_user, self.user_avatar if is_user else self.agent_avatar)
        self.chat_layout.addWidget(bubble)
        QTimer.singleShot(50, self.scroll_to_bottom)

    def scroll_to_bottom(self):
        self.scroll_area.verticalScrollBar().setValue(
            self.scroll_area.verticalScrollBar().maximum()
        )

    def send_message(self):
        user_text = self.input_box.text().strip()
        if not user_text:
            return
        self.add_message(user_text, is_user=True)
        self.input_box.clear()

        self._set_typing(True)

        # Worker thread
        self.send_button.setEnabled(False)
        self._thread = QThread()
        self.worker = Worker(user_text)
        self.worker.moveToThread(self._thread)
        self._thread.started.connect(self.worker.run)
        self.worker.finished.connect(self._on_agent_response)
        self.worker.finished.connect(self._thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self._thread.finished.connect(self._thread.deleteLater)
        self._thread.start()

    def _on_agent_response(self, response: str):
        self._set_typing(False)
        self.add_message(response, is_user=False)
        self.send_button.setEnabled(True)

    def _set_typing(self, enabled: bool):
        if enabled:
            self._typing_timer.start(400)
        else:
            self._typing_timer.stop()
            self.typing_label.setText("")

    def _update_typing(self):
        self._typing_dots = (self._typing_dots + 1) % 4
        self.typing_label.setText("Agent is thinking" + "." * self._typing_dots)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec_())

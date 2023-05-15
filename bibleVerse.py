import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt


class BibleVerseApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bible Verse App")
        self.setGeometry(100, 100, 400, 400)  # Set the window geometry (x, y, width, height)

        self.verses = [
            {
                "reference": "Psalm 139:1-3",
                "text": "O Lord, you have searched me and known me! You know when I sit down and when I rise up; you discern my thoughts from afar. You search out my path and my lying down and are acquainted with all my ways."
            }
        ]

        self.current_verse_index = 0
        self.display_verse()

        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)  # Enable focus for the main window

    def display_verse(self):
        verse = self.verses[self.current_verse_index]
        verse_text = verse['text']
        reference_text = verse['reference']
        # print(reference_text)

        # Randomly bold 30% of the words
        words = verse_text.split()
        num_words_to_bold = int(len(words) * 0.3)
        bold_indices = random.sample(range(len(words)), num_words_to_bold)
        for index in bold_indices:
            words[index] = f"<b>{words[index]}</b>"

        # Reconstruct the verse text
        verse_text = ' '.join(words)
        
        verse_label = QLabel(verse_text, self)
        verse_label.setGeometry(20, 20, 360, 280)  # Set the label geometry (x, y, width, height)
        verse_label.setWordWrap(True)
        verse_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        verse_label.setStyleSheet("font-size: 24px; font-family: Arial;")

        self.setCentralWidget(verse_label)  # Set the verse label as the central widget

        # Update reference_label or create a new one if it doesn't exist
        if hasattr(self, 'reference_label'):
            self.reference_label.setText(reference_text)
        else:
            reference_label = QLabel(reference_text, self)
            reference_label.setGeometry(20, 310, 360, 30)  # Set the label geometry (x, y, width, height)
            reference_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            reference_label.setStyleSheet("font-size: 18px; font-family: Arial;")
            self.reference_label = reference_label

        self.repaint()  # Refresh the window to display the new verse

    def switch_verse(self, index):
        self.current_verse_index = index
        self.display_verse()
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:  # Switch to the next verse on Space key press
            next_index = (self.current_verse_index + 1) % len(self.verses)
            self.switch_verse(next_index)

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            next_index = (self.current_verse_index + 1) % len(self.verses)
            self.switch_verse(next_index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BibleVerseApp()
    window.show()
    sys.exit(app.exec())

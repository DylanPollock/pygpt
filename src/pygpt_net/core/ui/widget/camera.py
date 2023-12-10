from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout


# video output container (with scroll
from ...utils import trans


class VideoContainer(QWidget):
    def __init__(self, window=None):
        """
        Video container with scroll

        :param window: main window
        """
        super(VideoContainer, self).__init__()
        self.window = window
        self.setStyleSheet("background-color: #000000;")

        self.label = QLabel(trans("vision.capture.label"))
        self.label.setMaximumHeight(15)
        self.label.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.video = VideoLabel(window=self.window)
        self.video.setStyleSheet("background-color: #000000;")
        self.layout.addWidget(self.video)
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)

    # on resize
    def resizeEvent(self, event):
        """
        On resize event

        :param event: resize event
        """
        # self.update_pos()
        super(VideoContainer, self).resizeEvent(event)


# video output label
class VideoLabel(QLabel):
    def __init__(self, text=None, window=None):
        """
        Video output label

        :param text: text
        :param window: main window
        """
        super(VideoLabel, self).__init__(text)
        self.window = window

    def mousePressEvent(self, event):
        """
        Mouse click

        :param event: mouse event
        """
        if event.button() == Qt.LeftButton:
            self.window.controller.camera.capture_frame()
            print('captured frame')
        elif event.button() == Qt.RightButton:
            pass
        elif event.button() == Qt.MiddleButton:
            pass

    def mouseDoubleClickEvent(self, event):
        """
        Mouse double click

        :param event: mouse event
        """
        if event.button() == Qt.LeftButton:
            pass
        elif event.button() == Qt.RightButton:
            pass
        elif event.button() == Qt.MiddleButton:
            pass

    def mouseReleaseEvent(self, event):
        """
        Mouse release

        :param event: mouse event
        """
        if event.button() == Qt.LeftButton:
            pass
        elif event.button() == Qt.RightButton:
            pass
        elif event.button() == Qt.MiddleButton:
            pass

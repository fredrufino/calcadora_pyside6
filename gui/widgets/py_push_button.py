#IMPORTS
import os

#IMPORT QT CORE
from qt_core import *

class PyPushButton(QPushButton):
    def __init__(
        self,
        text = "",
        font = "14pt \"Arial\"",
        maximum_width = 30,
        minimum_width = 30,
        minimum_heigth = 44,
        margin = 1,
        text_color = "#FFFFFF",
        text_btn_hover = "#000000",
        icon_path = "",
        icon_color = "#FFFFFF",
        btn_color = "#E5E5E5",
        btn_hover = "#BDC9DE",
        btn_pressed = "#0007B8",
        set_width = False
    ):
        super().__init__()

        self.setText(text)
        self.setMinimumHeight(minimum_heigth)
        self.setContentsMargins(margin,margin,margin,margin)
        self.setCursor(Qt.PointingHandCursor)

        self.minimum_heigth = minimum_heigth
        self.minimum_width = minimum_width
        self.maximum_width = maximum_width
        self.margin = margin
        self.font = font
        self.text_color = text_color
        self.text_btn_hover = text_btn_hover
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.set_max_width = maximum_width
        
        #SET MAXIMUM WIDTH
        if set_width:
            self.setMinimumWidth(minimum_width)
            self.setMaximumWidth(maximum_width)
        else:
            pass

        self.set_style (
            font = self.font,
            text_color = self.text_color,
            text_btn_hover = self.text_btn_hover,
            margin = self.margin,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            )

    def set_style(
        self,
        font = "14pt \"Arial\"",
        text_color = "#C3CCDF",
        text_btn_hover = "#000000",
        margin = 1,
        btn_color = "#44475A",
        btn_hover = "#4F5368",
        btn_pressed = "#282A36",
    ):
        style_margin = f"""
        QPushButton {{
            margin: {margin}px {margin}px {margin}px {margin}px;
            border-radius: 5px;
        }}
        """

        style = f"""
        QPushButton {{
            color: {text_color};
            background-color: {btn_color};
            text-align: center;
            border: none;
            font: {font};
        }}
         QPushButton:hover {{
            background-color: {btn_hover};
            color: {text_btn_hover};
        }}
        QPushButton:pressed {{
            background-color: {btn_pressed};
            color: {text_btn_hover};
        }}
        """

        self.setStyleSheet(style + style_margin)
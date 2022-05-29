#IMPORTAÇÃO QT CORE
from qt_core import *

#IMPORTAÇÃO DAS CUSTUMIZAÇÕES DOS WIDGETS
from gui.widgets.py_push_button import PyPushButton

#MAIN WINDOW 
class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")


            #CONFIGURANDO OS PARAMETROS INICIAIS DA TELA
            parent.resize(300, 470)
            parent.setMinimumSize(320,470)

            #CRIANDO O FRAME CENTRAL
            self.central_frame = QFrame()
            self.central_frame.setStyleSheet("background-color:  #244EBB;")

            #CRIANDO O LAYOUT PRINCIPAL
            self.main_layout = QVBoxLayout(self.central_frame)
            self.main_layout.setContentsMargins(0,0,0,0)
            self.main_layout.setSpacing(0)


            #CRIANDO O FRAME DA BARRA SUPERIOR
            self.top_bar = QFrame()
            self.top_bar.setMinimumHeight(35)
            self.top_bar.setMaximumHeight(35)
            self.top_bar.setObjectName("top_bar")

            #CRIANDO O LAYOUT DA BARRA SUPERIOR
            self.top_bar_layout = QHBoxLayout(self.top_bar)
            self.top_bar_layout.setContentsMargins(0,0,0,0)
            self.top_bar_layout.setSpacing(0)

            #CRIANDO OS BOTÕES SUPERIORES
            self.toggle_btn = PyPushButton(
                text= "|||",
                btn_color= "",
                btn_hover= "#244EBB",
                btn_pressed= "#244EBB",
                maximum_width= 30,
                minimum_width= 30,
                minimum_heigth=30,
                set_width= True
            )
            self.historic_btn = PyPushButton(
                text= "H",
                btn_color= "",
                btn_hover= "#244EBB",
                btn_pressed= "#244EBB",
                maximum_width= 30,
                minimum_width= 30,
                minimum_heigth=30,
                set_width= True
            )

            self.Spacer_top_bar = QSpacerItem(0,0, QSizePolicy.Expanding, QSizePolicy.Maximum)
        

            self.top_bar_layout.addWidget(self.toggle_btn)
            self.top_bar_layout.addItem(self.Spacer_top_bar)
            self.top_bar_layout.addWidget(self.historic_btn)

            #CRIANDO O FRAME DA ÁREA DE CONTEÚDO
            self.content = QFrame()
            self.content.setMinimumHeight(105)
            self.content.setObjectName("content")

            #CRIANDO O LAYOUT DA ÁREA DE CONTEÚDO
            self.content_layout = QHBoxLayout(self.content)
            self.content_layout.setContentsMargins(0,0,0,0)
            self.content_layout.setSpacing(0)


            #CRIANDO O GRUPO SUPERIOR DE BOTÕES
            self.buttons_top = QFrame()
            self.buttons_top.setMaximumHeight(26)
            self.buttons_top.setObjectName("buttons_top")

            #CRIANDO O LAYOUT DO GRUPO SUPERIOR DE BOTÕES
            self.buttons_top_layout = QHBoxLayout(self.buttons_top)
            self.buttons_top_layout.setContentsMargins(3,0,3,0)
            self.buttons_top_layout.setSpacing(1)

            #CRIANDO OS BOTÕES SUPERIORES
            self.mc_btn = PyPushButton(
                text = "MC",
                text_color= "black",
                minimum_heigth=26
            )
            self.mr_btn = PyPushButton(
                text = "MR",
                text_color= "black",
                minimum_heigth=26
            )
            self.m_more_btn = PyPushButton(
                text = "M+",
                text_color= "black",
                minimum_heigth=26
            )
            self.m_less_btn = PyPushButton(
                text = "M-",
                text_color= "black",
                minimum_heigth=26
            )
            self.ms_btn = PyPushButton(
                text = "MS",
                text_color= "black",
                minimum_heigth=26
            )
            self.m_down_btn = PyPushButton(
                text = "M˅",
                text_color= "black",
                minimum_heigth=26
            )
            
            #ADICIONANDO BOTÕES AO LAYOUT
            self.buttons_top_layout.addWidget(self.mc_btn)
            self.buttons_top_layout.addWidget(self.mr_btn)
            self.buttons_top_layout.addWidget(self.m_more_btn)
            self.buttons_top_layout.addWidget(self.m_less_btn)
            self.buttons_top_layout.addWidget(self.ms_btn)
            self.buttons_top_layout.addWidget(self.m_down_btn)

            #CRIANDO O LAYOUT DO GRUPO INFERIOR DE BOTÕES
            self.buttons_bottom_layout = QGridLayout()
            self.buttons_bottom_layout.setContentsMargins(3,3,3,3)
            self.buttons_bottom_layout.setSpacing(1)

            sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)

            self.percentage_btn = PyPushButton(
                text = "%",
                minimum_heigth=44,
                btn_color= "#0007B8",
                btn_hover = "#E5E5E5",
                btn_pressed = "#E5E5E5"
            )
            sizePolicy.setHeightForWidth(self.percentage_btn.sizePolicy().hasHeightForWidth())
            self.percentage_btn.setSizePolicy(sizePolicy)
            self.ce_btn = PyPushButton(
                text = "CE",
                minimum_heigth=44,
                btn_color= "#0007B8",
                btn_hover = "#E5E5E5",
                btn_pressed = "#E5E5E5"
            )
            sizePolicy.setHeightForWidth(self.ce_btn.sizePolicy().hasHeightForWidth())
            self.ce_btn.setSizePolicy(sizePolicy)
            self.c_btn = PyPushButton(
                text = "C",
                minimum_heigth=44,
                btn_color= "#0007B8",
                btn_hover = "#E5E5E5",
                btn_pressed = "#E5E5E5"
            )
            sizePolicy.setHeightForWidth(self.c_btn.sizePolicy().hasHeightForWidth())
            self.c_btn.setSizePolicy(sizePolicy)
            self.delete_btn = PyPushButton(
                text = "X",
                minimum_heigth=44,
                btn_color= "#0007B8",
                btn_hover = "#E5E5E5",
                btn_pressed = "#E5E5E5"
            )
            sizePolicy.setHeightForWidth(self.delete_btn.sizePolicy().hasHeightForWidth())
            self.delete_btn.setSizePolicy(sizePolicy)
            self.one_over_x_btn = PyPushButton(
                text = "⅟ₓ",
                minimum_heigth=44,
                btn_color= "#0007B8",
                btn_hover = "#E5E5E5",
                btn_pressed = "#E5E5E5"
            )
            sizePolicy.setHeightForWidth(self.one_over_x_btn.sizePolicy().hasHeightForWidth())
            self.one_over_x_btn.setSizePolicy(sizePolicy)
            self.squared_btn = PyPushButton(
                text = "x²",
                minimum_heigth=44,
                btn_color= "#0007B8",
                btn_hover = "#E5E5E5",
                btn_pressed = "#E5E5E5"
            )
            sizePolicy.setHeightForWidth(self.squared_btn.sizePolicy().hasHeightForWidth())
            self.squared_btn.setSizePolicy(sizePolicy)
            self.square_root_btn = PyPushButton(
                text = "√x",
                minimum_heigth=44,
                btn_color= "#0007B8",
                btn_hover = "#E5E5E5",
                btn_pressed = "#E5E5E5"
            )
            sizePolicy.setHeightForWidth(self.square_root_btn.sizePolicy().hasHeightForWidth())
            self.square_root_btn.setSizePolicy(sizePolicy)
            self.division_btn = PyPushButton(
                text = "÷",
                minimum_heigth=44,
                btn_color= "#0007B8",
                btn_hover = "#E5E5E5",
                btn_pressed = "#E5E5E5"
            )
            sizePolicy.setHeightForWidth(self.division_btn.sizePolicy().hasHeightForWidth())
            self.division_btn.setSizePolicy(sizePolicy)
            self.seven_btn = PyPushButton(
                text = "7",
                minimum_heigth=44,
                text_color= "#000000",
                text_btn_hover= "#FFFFFF"
            )
            sizePolicy.setHeightForWidth(self.seven_btn.sizePolicy().hasHeightForWidth())
            self.seven_btn.setSizePolicy(sizePolicy)
            self.eight_btn = PyPushButton(
                text = "8",
                minimum_heigth=44,
                text_color= "#000000",
                text_btn_hover= "#FFFFFF"
            )
            sizePolicy.setHeightForWidth(self.eight_btn.sizePolicy().hasHeightForWidth())
            self.eight_btn.setSizePolicy(sizePolicy)
            self.nine_btn = PyPushButton(
                text = "9",
                minimum_heigth=44,
                text_color= "#000000",
                text_btn_hover= "#FFFFFF"
            )
            sizePolicy.setHeightForWidth(self.nine_btn.sizePolicy().hasHeightForWidth())
            self.nine_btn.setSizePolicy(sizePolicy)
            self.multiplication_btn = PyPushButton(
                text = "x",
                minimum_heigth=44,
                btn_color= "#0007B8",
                btn_hover = "#E5E5E5",
                btn_pressed = "#E5E5E5"
            )
            sizePolicy.setHeightForWidth(self.multiplication_btn.sizePolicy().hasHeightForWidth())
            self.multiplication_btn.setSizePolicy(sizePolicy)
            self.four_btn = PyPushButton(
                text = "4",
                minimum_heigth=44,
                text_color= "#000000",
                text_btn_hover= "#FFFFFF"
            )
            sizePolicy.setHeightForWidth(self.four_btn.sizePolicy().hasHeightForWidth())
            self.four_btn.setSizePolicy(sizePolicy)
            self.five_btn = PyPushButton(
                text = "5",
                minimum_heigth=44,
                text_color= "#000000",
                text_btn_hover= "#FFFFFF"
            )
            sizePolicy.setHeightForWidth(self.five_btn.sizePolicy().hasHeightForWidth())
            self.five_btn.setSizePolicy(sizePolicy)
            self.six_btn = PyPushButton(
                text = "6",
                minimum_heigth=44,
                text_color= "#000000",
                text_btn_hover= "#FFFFFF"
            )
            sizePolicy.setHeightForWidth(self.six_btn.sizePolicy().hasHeightForWidth())
            self.six_btn.setSizePolicy(sizePolicy)
            self.addition_btn = PyPushButton(
                text = "+",
                minimum_heigth=44,
                btn_color= "#0007B8",
                btn_hover = "#E5E5E5",
                btn_pressed = "#E5E5E5"
            )
            sizePolicy.setHeightForWidth(self.addition_btn.sizePolicy().hasHeightForWidth())
            self.addition_btn.setSizePolicy(sizePolicy)
            self.one_btn = PyPushButton(
                text = "1",
                minimum_heigth=44,
                text_color= "#000000",
                text_btn_hover= "#FFFFFF"
            )
            sizePolicy.setHeightForWidth(self.one_btn.sizePolicy().hasHeightForWidth())
            self.one_btn.setSizePolicy(sizePolicy)
            self.two_btn = PyPushButton(
                text = "2",
                minimum_heigth=44,
                text_color= "#000000",
                text_btn_hover= "#FFFFFF"
            )
            sizePolicy.setHeightForWidth(self.two_btn.sizePolicy().hasHeightForWidth())
            self.two_btn.setSizePolicy(sizePolicy)
            self.three_btn = PyPushButton(
                text = "3",
                minimum_heigth=44,
                text_color= "#000000",
                text_btn_hover= "#FFFFFF"
            )
            sizePolicy.setHeightForWidth(self.three_btn.sizePolicy().hasHeightForWidth())
            self.three_btn.setSizePolicy(sizePolicy)
            self.subtraction_btn = PyPushButton(
                text = "-",
                minimum_heigth=44,
                btn_color= "#0007B8",
                btn_hover = "#E5E5E5",
                btn_pressed = "#E5E5E5"
            )
            sizePolicy.setHeightForWidth(self.subtraction_btn.sizePolicy().hasHeightForWidth())
            self.subtraction_btn.setSizePolicy(sizePolicy)
            self.more_or_less_btn = PyPushButton(
                text = "⁺⁄₋",
                minimum_heigth=44,
                text_color= "#000000",
                text_btn_hover= "#FFFFFF"
            )
            sizePolicy.setHeightForWidth(self.more_or_less_btn.sizePolicy().hasHeightForWidth())
            self.more_or_less_btn.setSizePolicy(sizePolicy)
            self.zero_btn = PyPushButton(
                text = "0",
                minimum_heigth=44,
                text_color= "#000000",
                text_btn_hover= "#FFFFFF"
            )
            sizePolicy.setHeightForWidth(self.zero_btn.sizePolicy().hasHeightForWidth())
            self.zero_btn.setSizePolicy(sizePolicy)
            self.comma_btn = PyPushButton(
                text = ",",
                minimum_heigth=44,
                text_color= "#000000",
                text_btn_hover= "#FFFFFF"
            )
            sizePolicy.setHeightForWidth(self.comma_btn.sizePolicy().hasHeightForWidth())
            self.comma_btn.setSizePolicy(sizePolicy)
            self.equal_btn = PyPushButton(
                text = "=",
                minimum_heigth=44,
                text_color= "#000000",
                btn_color= "#8FB5FF",
                btn_hover = "#E5E5E5",
                btn_pressed = "#E5E5E5"
            )
            sizePolicy.setHeightForWidth(self.equal_btn.sizePolicy().hasHeightForWidth())
            self.equal_btn.setSizePolicy(sizePolicy)


            self.buttons_bottom_layout.addWidget(self.percentage_btn, 0, 0, 1, 1)
            self.buttons_bottom_layout.addWidget(self.ce_btn, 0, 1, 1, 1)
            self.buttons_bottom_layout.addWidget(self.c_btn, 0, 2, 1, 1)
            self.buttons_bottom_layout.addWidget(self.delete_btn, 0, 3, 1, 1)

            self.buttons_bottom_layout.addWidget(self.one_over_x_btn, 1, 0, 1, 1)
            self.buttons_bottom_layout.addWidget(self.squared_btn, 1, 1, 1, 1)
            self.buttons_bottom_layout.addWidget(self.square_root_btn, 1, 2, 1, 1)
            self.buttons_bottom_layout.addWidget(self.division_btn, 1, 3, 1, 1)

            self.buttons_bottom_layout.addWidget(self.seven_btn, 2, 0, 1, 1)
            self.buttons_bottom_layout.addWidget(self.eight_btn, 2, 1, 1, 1)
            self.buttons_bottom_layout.addWidget(self.nine_btn, 2, 2, 1, 1)
            self.buttons_bottom_layout.addWidget(self.multiplication_btn, 2, 3, 1, 1)

            self.buttons_bottom_layout.addWidget(self.four_btn, 3, 0, 1, 1)
            self.buttons_bottom_layout.addWidget(self.five_btn, 3, 1, 1, 1)
            self.buttons_bottom_layout.addWidget(self.six_btn, 3, 2, 1, 1)
            self.buttons_bottom_layout.addWidget(self.addition_btn, 3, 3, 1, 1)

            self.buttons_bottom_layout.addWidget(self.one_btn, 4, 0, 1, 1)
            self.buttons_bottom_layout.addWidget(self.two_btn, 4, 1, 1, 1)
            self.buttons_bottom_layout.addWidget(self.three_btn, 4, 2, 1, 1)
            self.buttons_bottom_layout.addWidget(self.subtraction_btn, 4, 3, 1, 1)

            self.buttons_bottom_layout.addWidget(self.more_or_less_btn, 5, 0, 1, 1)
            self.buttons_bottom_layout.addWidget(self.zero_btn, 5, 1, 1, 1)
            self.buttons_bottom_layout.addWidget(self.comma_btn, 5, 2, 1, 1)
            self.buttons_bottom_layout.addWidget(self.equal_btn, 5, 3, 1, 1)

            #ADICIONANDO WIDGETS AO APP
            self.main_layout.addWidget(self.top_bar)
            self.main_layout.addWidget(self.content)
            self.main_layout.addWidget(self.buttons_top)
            self.main_layout.addLayout(self.buttons_bottom_layout)

            #SET CENTRAL WIDGET
            parent.setCentralWidget(self.central_frame)


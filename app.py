import pandas as pd
import xlwings as xw
from PySide6.QtGui import QIntValidator
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QListWidgetItem, QDialog, QTableWidgetItem, \
    QHeaderView, QItemDelegate, QLineEdit
from qt_material import apply_stylesheet

from class_record import ClassSheet
from class_record import randomizer
from ui.InputGradesDialog import Ui_InputGradesDialog
from ui.MainWindow import Ui_MainWindow
from ui.OptionDialog import Ui_OptionDialog
from ui.EditGradesDialog import Ui_EditGradesDialog
from ui.AboutDialog import Ui_AboutDialog
from version import __version__

RANDOMIZER_MAX_LOOP = 100_000
RANDOMIZER_THRESHOLD = 1.6


class IntDelegate(QItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        editor.setValidator(QIntValidator())
        return editor


class AboutDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)

        self.ui.labelAuthor.setText('jedymatt')
        self.ui.versionLabel.setText(__version__)


class EditGradesDialog(QDialog):
    def __init__(self, parent, cs):
        super().__init__(parent)
        self.ui = Ui_EditGradesDialog()
        self.ui.setupUi(self)

        self.cs = cs

        self.ui.pushButton.clicked.connect(self.generate)

    def generate(self):
        offset_value = self.ui.spinBox.value()
        for sr in self.cs.student_records:
            expected_average = sr.transmuted_average + offset_value
            overwrite_all = self.ui.checkBox.isChecked()
            randomizer.randomize_student_record(sr, expected_average, self.cs.head_components,
                                                max_loop=RANDOMIZER_MAX_LOOP,
                                                threshold=RANDOMIZER_THRESHOLD,
                                                overwrite_all=overwrite_all)

        # save scores to excel
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.cs.save_sheet()
        QApplication.restoreOverrideCursor()
        self.close()


class InputGradesDialog(QDialog):
    def __init__(self, parent, cs: ClassSheet):
        super().__init__(parent)
        self.ui = Ui_InputGradesDialog()
        self.ui.setupUi(self)

        self.cs = cs

        df = pd.DataFrame([[student.name, ''] for student in self.cs.student_records])
        self.df = df
        self.ui.tableWidget.setRowCount(df.shape[0])
        self.ui.tableWidget.setColumnCount(df.shape[1])

        self.ui.checkBox.setChecked(True)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Learner's Names", "New Average"])

        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.ui.tableWidget.setItemDelegateForColumn(1, IntDelegate())

        for row in range(self.ui.tableWidget.rowCount()):
            for col in range(self.ui.tableWidget.columnCount()):
                item = QTableWidgetItem(str(self.df.iloc[row, col]))

                self.ui.tableWidget.setItem(row, col, item)

        self.ui.tableWidget.cellChanged[int, int].connect(self.update_df)
        self.ui.pushButton.clicked.connect(self.generate)

    def update_df(self, row, column):
        text = self.ui.tableWidget.item(row, column).text()
        self.df.iloc[row, column] = text

    def generate(self):
        for row in self.df.iterrows():
            row_idx, values = row
            if values[1] is not None and values[1] != '':
                value = str(self.df.iloc[row_idx, 1])
                overwrite_all = bool(self.ui.checkBox.checkState())
                randomizer.randomize_student_record(self.cs.student_records[row_idx], int(value),
                                                    self.cs.head_components, max_loop=RANDOMIZER_MAX_LOOP,
                                                    overwrite_all=overwrite_all, threshold=RANDOMIZER_THRESHOLD)

        # save scores to excel
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.cs.save_sheet()
        QApplication.restoreOverrideCursor()
        self.close()


class OptionDialog(QDialog):
    def __init__(self, parent, title, cs: ClassSheet):
        super().__init__(parent)
        self.ui = Ui_OptionDialog()
        self.ui.setupUi(self)
        self.setWindowTitle(title)

        self.cs = cs
        self.input_grades = None
        self.edit_grades = None

        self.ui.buttonNewAverage.clicked.connect(self.create_new_average)
        self.ui.buttonExistingAverage.clicked.connect(self.edit_existing_average)

    def create_new_average(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.input_grades = InputGradesDialog(self, self.cs)
        QApplication.restoreOverrideCursor()
        self.input_grades.show()

    def edit_existing_average(self):
        self.edit_grades = EditGradesDialog(self, self.cs)
        self.edit_grades.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Class Genie')

        self.ui.listWidget.hide()
        self.ui.pushButton.hide()

        self.app = xw.App(visible=False, add_book=False)
        self.wb = None
        self.cs = None
        self.dialog = None
        self.about = AboutDialog(self)

        self.ui.actionOpen.triggered.connect(self.open_workbook)
        self.ui.actionAbout.triggered.connect(lambda: self.about.show())
        self.ui.pushButton.clicked.connect(self.edit_selected)

    def open_workbook(self):
        url = QFileDialog.getOpenFileName(self, filter='Excel Files (*.xlsx)')
        if url[0]:
            if self.app.books:
                print('has active')
                self.app.books.active.close()
                self.ui.listWidget.clear()

            QApplication.setOverrideCursor(Qt.WaitCursor)
            self.wb: xw.Book = self.app.books.open(url[0], update_links=False)
            QApplication.restoreOverrideCursor()

            self.ui.listWidget.show()
            self.ui.pushButton.show()
            for sheet in self.wb.sheets:
                item = QListWidgetItem(sheet.name)
                item.setData(1, sheet)
                self.ui.listWidget.addItem(sheet.name)

    def edit_selected(self):
        index: QListWidgetItem = self.ui.listWidget.currentItem()
        if index is None:
            return

        sheet = self.wb.sheets[index.text()]
        self.cs = ClassSheet(sheet)
        self.dialog = OptionDialog(self, index.text(), self.cs)
        self.dialog.show()

    def closeEvent(self, event):
        self.wb.close()
        self.app.quit()


if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()

    main_window.show()

    apply_stylesheet(app, 'dark_red.xml')

    app.exec()

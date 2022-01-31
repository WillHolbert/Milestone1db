import sys
import PyQt5.QtWidgets
import PyQt5
import psycopg2

qtCreaterFile = "milestone1App.ui"

Ui_MainWindow, QtbaseClass = uic.loadUiType(qtCreaterFile)

class milestone1(QMainWindow):
    def ___init___(self):
        super(milestone1, self).___init___()
        self.ui = Ui_MainWindow()
        self.Ui.setupUi(self)
        self.loadStateList()

    def executeQuery(self):
        try:
            conn = psycpog2.connect("dbname = 'milestone1db' user = 'postgres' host = 'localhost' password = 'Dobby2022!!!'")
        except:
            print("unable to connect to databse!")
        cur = conn.cursor()
        cur.execute(sql_str)
        conn.commit()
        result = cur.fetchall()
        conn.close()
        return result

    def loadStateList(self):
        sql_str = "SELECT distinct state FROM business ORDER BY state;"
        try:
            results = self.executeQuery(sql_str)
            for row in results:
                self.ui.stateList.addItem(row[0])
            print(results)
        except:
            print("Query failed!")
        self.ui.stateList.setCurrentIndex(-1)
        self.ui.stateList.clearEditText()

    def stateChanged(self):
        state = self.ui.stateList.currentText()
        city = self.ui.cityList.currentText()
        sql_str = "SELECT distinct state FROM business WHERE state =" + state + " ORDER BY city;"
        try:
            results = self.executeQuery(sql_str)
            for row in results:
                self.ui.stateList.addItem(row[0])
            print(results)
        except:
            print("Query failed!")

        sql_str = "SELECT name, state, city, business_id FROM business WHERE city = " + city + " AND state= " + state + " ORDER BY name;"
        try:
            results = self.executeQuery(sql_str)
            style = "::section {background-color: $f3f3f3; }"
            self.ui.businessTable.horizontalHeader().setStyleSheet(style)
            self.ui.businessTable.setColumnCount(len(results[0]))
            self.ui.businessTable.setRowCount(len(results))
            self.ui.businessTable.horizontalHeaderLabels(['Business Name', 'City', 'State'])
            currentRowCount = 0
            colCount = 0
            for row in results:
                self.ui.businessTable.setItem(currentRowCount,colCount,QTableWidgetItem(row[colCount]))
                currentRowCount +=1
            print(results)
        except:
            print("Query failed!")

if ___name___ == "___main___":
    app = QApplication(sys.argv)
    window = milestone1()
    window.show()
    sys.exit(app.exec_())

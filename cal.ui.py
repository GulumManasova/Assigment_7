<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>300</width>
    <height>450</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QLineEdit" name="lineEdit">
      <property name="font">
       <font>
        <pointsize>40</pointsize>
        <bold>true</bold>
       </font>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QGridLayout" name="gridLayout">
      <item row="0" column="0">
       <widget class="QPushButton" name="pushButton_7">
        <property name="text">
         <string>7</string>
        </property>
       </widget>
      </item>
      <item row="0" column="1">
       <widget class="QPushButton" name="pushButton_8">
        <property name="text">
         <string>8</string>
        </property>
       </widget>
      </item>
      <item row="0" column="2">
       <widget class="QPushButton" name="pushButton_9">
        <property name="text">
         <string>9</string>
        </property>
       </widget>
      </item>
      <item row="0" column="3">
       <widget class="QPushButton" name="pushButton_divide">
        <property name="text">
         <string>/</string>
        </property>
       </widget>
      </item>
      <!-- Repeat for other numbers, operators, and buttons -->
      <item row="3" column="0">
       <widget class="QPushButton" name="pushButton_clear">
        <property name="text">
         <string>C</string>
        </property>
       </widget>
      </item>
      <item row="3" column="3">
       <widget class="QPushButton" name="pushButton_equal">
        <property name="text">
         <string>=</string>
        </property>
       </widget>
      </item>
    </widget>
   </item>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>

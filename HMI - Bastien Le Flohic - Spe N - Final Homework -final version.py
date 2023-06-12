# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 11:53:02 2023
@author: Bastien Le Flohic
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton, QCheckBox, QTextEdit, QPushButton, QMessageBox

# Create a subclass of QWidget to build the form widget
class FormWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Form")
        layout = QVBoxLayout()  # Create a vertical layout to hold the form elements

        # Single Choice Question
        single_choice_label = QLabel("Who painted the \"Mona Lisa\"?")
        layout.addWidget(single_choice_label)  # Add the question label to the layout
        self.single_choice_radio_buttons = []  # Create a list to hold the radio buttons
        single_choice_options = [
            {"option": "Michelangelo", "correction": False},
            {"option": "Leonardo da Vinci", "correction": True},
            {"option": "Mirò", "correction": False}
        ]
        for option in single_choice_options:
            radio_button = QRadioButton(option["option"])  # Create a radio button for each option
            radio_button.correct = option["correction"]  # Store the correct answer as an attribute of the radio button
            self.single_choice_radio_buttons.append(radio_button)  # Add the radio button to the list
            layout.addWidget(radio_button)  # Add the radio button to the layout

        # Multiple Choice Question
        multiple_choice_label = QLabel("Who are the two philosophers who are credited with laying the foundation for Western philosophy?")
        layout.addWidget(multiple_choice_label)
        self.multiple_choice_checkboxes_2 = []
        multiple_choice_options_2 = [
            {"option": "Socrates", "correction": True},
            {"option": "Plato", "correction": True},
            {"option": "Confucius", "correction": False},
            {"option": "Kant", "correction": False},
        ]
        for option in multiple_choice_options_2:
            checkbox = QCheckBox(option["option"])  # Create a checkbox for each option
            checkbox.correct = option["correction"]  # Store the correct answer as an attribute of the checkbox
            self.multiple_choice_checkboxes_2.append(checkbox)  # Add the checkbox to the list
            layout.addWidget(checkbox)  # Add the checkbox to the layout

        # Text Answer
        text_answer_label = QLabel("What is the largest country in the world by area?")
        layout.addWidget(text_answer_label)
        self.text_answer_textedit = QTextEdit()  # Create a QTextEdit widget for the text answer
        self.text_answer_textedit.setMaximumHeight(50)  # Set the maximum height of the text zone
        layout.addWidget(self.text_answer_textedit)  # Add the QTextEdit widget to the layout

        # Multiple Choice Question
        multiple_choice_label = QLabel("Which mathematicians are known for their work on calculus and are often credited with its development?")
        layout.addWidget(multiple_choice_label)
        self.multiple_choice_checkboxes_1 = []
        multiple_choice_options_1 = [
            {"option": "Euler", "correction": True},
            {"option": "Newton", "correction": True},
            {"option": "Gauss", "correction": False},
            {"option": "Hilbert", "correction": False},
            {"option": "Leibniz", "correction": True}
        ]
        for option in multiple_choice_options_1:
            checkbox = QCheckBox(option["option"])  # Create a checkbox for each option
            checkbox.correct = option["correction"]  # Store the correct answer as an attribute of the checkbox
            self.multiple_choice_checkboxes_1.append(checkbox)  # Add the checkbox to the list
            layout.addWidget(checkbox)  # Add the checkbox to the layout

        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submitForm)  # Connect the submitForm method to the button click event
        layout.addWidget(submit_button)  # Add the submit button to the layout

        self.setLayout(layout)  # Set the layout for the widget
        self.show()  # Show the widget on the screen

    def submitForm(self):
        # Process the form data
        correct_answers = []  # List to store correct answers
        incorrect_answers = []  # List to store incorrect answers
        partially_correct_answers = []  # List to store partially correct answers

        # Process single choice question
        single_choice_answer = ""
        single_choice_correct = False
        for radio_button in self.single_choice_radio_buttons:
            if radio_button.isChecked():  # Check if the radio button is selected
                single_choice_answer = radio_button.text()  # Get the selected option
                single_choice_correct = radio_button.correct  # Get the correct attribute of the radio button
                if single_choice_correct:
                    correct_answers.append(single_choice_answer)  # Add the correct answer to the list
                else:
                    incorrect_answers.append(single_choice_answer)  # Add the incorrect answer to the list
                break

        # Process multiple choice question 2
        multiple_choice_answers_2 = []
        multiple_choice_correct_2 = []
        for checkbox in self.multiple_choice_checkboxes_2:
            if checkbox.isChecked():  # Check if the checkbox is selected
                multiple_choice_answers_2.append(checkbox.text())  # Add the selected option to the list
                multiple_choice_correct_2.append(checkbox.correct)  # Add the correct attribute of the checkbox to the list
                if checkbox.correct:
                    correct_answers.append(checkbox.text())  # Add the correct answer to the list
                else:
                    incorrect_answers.append(checkbox.text())  # Add the incorrect answer to the list

        # Process text answer
        text_answer = self.text_answer_textedit.toPlainText()  # Get the entered text answer
        text_answer_correct = (text_answer.lower() == "russia")  # Check if the answer is correct
        if text_answer_correct:
            correct_answers.append(text_answer)  # Add the correct answer to the list
        else:
            incorrect_answers.append(text_answer)  # Add the incorrect answer to the list

        # Process multiple choice question 1
        multiple_choice_answers_1 = []
        multiple_choice_correct_1 = []
        for checkbox in self.multiple_choice_checkboxes_1:
            if checkbox.isChecked():  # Check if the checkbox is selected
                multiple_choice_answers_1.append(checkbox.text())  # Add the selected option to the list
                multiple_choice_correct_1.append(checkbox.correct)  # Add the correct attribute of the checkbox to the list
                if checkbox.correct:
                    correct_answers.append(checkbox.text())  # Add the correct answer to the list
                else:
                    incorrect_answers.append(checkbox.text())  # Add the incorrect answer to the list

        # Provide feedback
        feedback = ""
        feedback += "Single Choice Question: Answer: {}\n".format(single_choice_answer)
        if single_choice_correct:
            feedback += "Correct!\n"
        else:
            feedback += "Incorrect\nHint: He was born at Vinci, which is a small town near Florence\n"

        feedback += "---------------------------------------------------------------------\n"

        feedback += "Multiple Choice Answers 2: {}\n".format(", ".join(multiple_choice_answers_2))
        if all(multiple_choice_correct_2):
            feedback += "Correct!\n"
        elif any(multiple_choice_correct_2):
            partially_correct_answers.extend([option for option, correct in zip(multiple_choice_answers_2, multiple_choice_correct_2) if correct])
            incorrect_answers.extend([option for option, correct in zip(multiple_choice_answers_2, multiple_choice_correct_2) if not correct])
            feedback += "Partially Correct!\n"
        else:
            feedback += "Incorrect\nHint: They were ancient Greek philosophers.\n"

        feedback += "---------------------------------------------------------------------\n"

        feedback += "Text Answer: {}\n".format(text_answer)
        if text_answer_correct:
            feedback += "Correct!\n"
        else:
            feedback += "Incorrect\nHint: The country's capital is Moscow\n"

        feedback += "---------------------------------------------------------------------\n"

        feedback += "Multiple Choice Answers 1: {}\n".format(", ".join(multiple_choice_answers_1))
        if all(multiple_choice_correct_1):
            feedback += "Correct!\n"
        elif any(multiple_choice_correct_1):
            partially_correct_answers.extend([option for option, correct in zip(multiple_choice_answers_1, multiple_choice_correct_1) if correct])
            incorrect_answers.extend([option for option, correct in zip(multiple_choice_answers_1, multiple_choice_correct_1) if not correct])
            feedback += "Partially Correct!\n"
        else:
            feedback += "Incorrect\nHint: Newton discovered the laws of gravity, and Leibniz wrote about the Monad.\n"

        feedback += "---------------------------------------------------------------------\n"

        feedback += "Correct Answers:\n"
        feedback += "-----------------\n"
        feedback += "\n".join(correct_answers) + "\n"

        feedback += "---------------------------------------------------------------------\n"

        feedback += "Incorrect Answers:\n"
        feedback += "-------------------\n"
        feedback += "\n".join(incorrect_answers) + "\n"

        feedback += "---------------------------------------------------------------------\n"

        feedback += "Partially Correct Answers:\n"
        feedback += "-------------------------\n"
        feedback += "\n".join(partially_correct_answers) + "\n"

        qMessageBox = QMessageBox()
        qMessageBox.setWindowTitle("Feedback")
        qMessageBox.setText(feedback)  # Set the feedback text
        qMessageBox.exec()  # Display the feedback message box

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form_widget = FormWidget()  # Create an instance of the FormWidget
    sys.exit(app.exec_())  # Start the application event loop
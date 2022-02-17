"""
# CS465-W22-IRproject-Group4-FrontEnd.py
#
# CS465/665, W22, and Project #1
# Martin Miglio and Johnathan Max Tomlin
#
# This file will handle the graphical user interface of this information retrieval program
"""
import PySimpleGUI as sg

# TODO, create graphical user interface


# TODO, allow user to make queires, process the queries to work with the backend
# TODO, display results of the queries
# TODO, make static queries to retrieve statistics about the documents (see readme for more info)

def run(window):
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        print('You entered ', values[0])


if __name__ == "__main__":
    default_folder = 'documents/'
    title_row = [sg.Text("CS465 W22 IR Project Group 4")]
    query_row = [sg.Text("Query:"), sg.InputText(), sg.Button('Run Query')]
    statistics_row = [sg.Text("Statistics:"), sg.Table(values=[
        ['stat1', 'stat2', 'stat3']], headings=['statName1', 'statName2', 'statName3'])]
    exit_row = [sg.Button("Exit")]

    # layout for window
    layout = [
        title_row,
        query_row,
        statistics_row,
        exit_row]
    # create the window
    window = sg.Window("CS465 W22 IR Project Group 4", layout)
    # run window
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    # close window
    window.close()

"""
# CS465-W22-IRproject-Group4-FrontEnd.py
#
# CS465/665, W22, and Project #1
# Martin Miglio and Johnathan Max Tomlin
#
# This file will handle the graphical user interface of this information retrieval program
"""
import sys

import PySimpleGUI as sg

from CS465_W22_IRproject_Group4_BackEnd import (
    initialize, perform_query, specified_word_frequencies)


def run_document_window(window):
    """
    # runs a sg window, handles events
    # -mm
    """
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event in ["Read Documents"]:
            return initialize(values[0])
        if event in ["Exit", sg.WIN_CLOSED]:
            return None


def run_main_window(window, index_to_query):
    """
    # runs a sg window, handles events
    # -mm
    """
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event in ['Run Query']:
            query_results = perform_query(index_to_query, values[0])
            query_results_popup(values[0], query_results)
        if event in ["Exit", sg.WIN_CLOSED]:
            break


def query_results_popup(query_text, query_results):
    """
    # creates a popup window for displaying query results
    # -mm
    """
    popup_title_row = [sg.Text("CS465 W22 IR Project Group 4")]
    popup_query_row = [sg.Text(f"DocID Results for \"{query_text}\":")]
    popup_results_row = [sg.Listbox(
        values=query_results, pad=5, expand_y=True, expand_x=True)]
    popup_layout = [popup_title_row, popup_query_row, popup_results_row]
    popup_window = sg.Window("CS465 W22 IR Project Group 4", popup_layout)
    while True:
        event, _ = popup_window.read()
        if event in [sg.WIN_CLOSED]:
            break


if __name__ == "__main__":
    """
    # runs program, connecting gui with backend
    # -mm
    """
    # region run document selection gui
    DEFAULT_FOLDER = 'documents/'

    # define gui layout
    document_title_row = [sg.Text("CS465 W22 IR Project Group 4")]
    information_row = [sg.Text("Enter a directory of documents to parse")]
    document_row = [sg.InputText(
        default_text=DEFAULT_FOLDER), sg.Button('Read Documents')]
    document_layout = [document_title_row, information_row, document_row]
    document_window = sg.Window(
        "CS465 W22 IR Project Group 4", document_layout)

    # get index from document gui
    index = run_document_window(document_window)
    if index is None:
        sys.exit()  # if no documents were found close program
    document_window.close()
    # endregion

    # region begin index processing
    word_frequency_rank_100 = specified_word_frequencies(index, 100)
    word_frequency_rank_500 = specified_word_frequencies(index, 500)
    word_frequency_rank_1000 = specified_word_frequencies(index, 1000)
    # endregion

    # region run main gui
    # define gui layout
    main_title_row = [sg.Text("CS465 W22 IR Project Group 4")]
    query_row = [sg.Text("Query:"), sg.InputText(), sg.Button('Run Query')]
    statistics_row = [
        sg.Text("Term Frequencies:"),
        sg.Table(
            headings=[
                '100th Most Frequent',
                '500th Most Frequent',
                '1000th Most Frequent'
            ],
            values=[[
                f"{word_frequency_rank_100[0]}, Count: {word_frequency_rank_100[1]}",
                f"{word_frequency_rank_500[0]}, Count: {word_frequency_rank_500[1]}",
                f"{word_frequency_rank_1000[0]}, Count: {word_frequency_rank_1000[1]}"
            ]],
            num_rows=1
        )
    ]
    exit_row = [sg.Button("Exit")]
    main_layout = [
        main_title_row,
        query_row,
        statistics_row,
        exit_row]
    main_window = sg.Window("CS465 W22 IR Project Group 4", main_layout)
    # run window
    run_main_window(main_window, index)
    # close window
    main_window.close()
    # endregion

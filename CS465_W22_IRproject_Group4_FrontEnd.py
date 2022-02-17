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

from CS465_W22_IRproject_Group4_BackEnd import (all_term_frequencies,
                                                distinct_terms,
                                                distinct_terms_doc, initialize,
                                                perform_query,
                                                specified_word_frequencies)


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
    (file_list, index) = run_document_window(document_window)
    if index is None:
        sys.exit()  # if no documents were found close program
    document_window.close()
    # endregion

    # region collect statistics on index
    # Report the number of distinct words observed in each document,
    #  and the total number of words encountered.
    distinct_terms_headers = []
    distinct_terms_values = []
    for docID in range(len(file_list)):
        distinct_terms_headers.append(f"Doc{docID}'s Distinct Terms")
        distinct_terms_values.extend([distinct_terms_doc(index, docID)])
    distinct_terms_headers.append("All Documents' Distinct Terms")
    distinct_terms_values.extend([distinct_terms(index)])
    distinct_terms_row = [
        sg.Text("Distinct Term Frequencies:"),
        sg.Table(
            headings=distinct_terms_headers,
            values=[distinct_terms_values],
            num_rows=1,
            expand_x=True
        )
    ]

    # Report the top 100th, 500th, and 1000th most-frequent word
    #  and their frequencies of occurrence.
    word_frequency_rank_100 = specified_word_frequencies(index, 100)
    word_frequency_rank_500 = specified_word_frequencies(index, 500)
    word_frequency_rank_1000 = specified_word_frequencies(index, 1000)
    specific_frequencies_row = [
        sg.Text("Specific Term Frequencies:"),
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
            num_rows=1,
            expand_x=True       
        )
    ]
    # Report the total number of times each word is seen (term frequency)
    #  and the document IDs where the word occurs (Output the posting list for a term).
    every_term_frequency = all_term_frequencies(index)
    term_rank = 1
    for term_frequency in every_term_frequency:
        term_frequency.append(term_rank)
        term_rank = term_rank + 1
    all_frequencies_row = [
        sg.Text("All Term Frequencies:"),
        sg.Table(
            headings=[
                'Term',
                'Count',
                'Frequency Rank'
            ],
            values=every_term_frequency,
            expand_x=True,
            expand_y=True,
            alternating_row_color = 'Grey'
        )
    ]
    # endregion

    # region run main gui
    # define gui layout
    main_title_row = [sg.Text("CS465 W22 IR Project Group 4")]
    query_row = [
        sg.Text("Query:"),
        sg.InputText(),
        sg.Button('Run Query'),
        sg.Text(
            "Use '&' for AND, '|' for OR. User can use multiple operands in one query.",
            expand_x=True,
            justification='left'
        )
    ]

    exit_row = [sg.Button("Exit"), sg.Sizegrip()]
    main_layout = [
        main_title_row,
        query_row,
        distinct_terms_row,
        specific_frequencies_row,
        all_frequencies_row,
        exit_row]
    main_window = sg.Window(
        "CS465 W22 IR Project Group 4",
        auto_size_text=False,
        default_element_size=(25, 1),
        text_justification='right',
        resizable=True
    ).Layout(main_layout)
    # run window
    run_main_window(main_window, index)
    # close window
    main_window.close()
    # endregion

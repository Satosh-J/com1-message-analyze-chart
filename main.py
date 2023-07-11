# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import csv
import plotly.graph_objects as go
import numpy

filename = 'message_data.csv'

message = []
message_date = []
date_detail = {}


def preprocess():
    # Use a breakpoint in the code line below to debug your script.
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            message.append(row)

            if message_date.__contains__(row[2].split(' ')[0]) is False:
                author_count = {}
                message_date.append(row[2].split(' ')[0])
                author_count.__setitem__(row[1], 1)
                date_detail.__setitem__(row[2].split(' ')[0], author_count)

            elif message_date.__contains__(row[2].split(' ')[0]) is True:
                if author_count.keys().__contains__(row[1]):
                    author_count[row[1]] += 1
                else:
                    author_count.__setitem__(row[1], 1)

                date_detail[row[2].split(' ')[0]] = author_count

    statistic(date_detail)


def statistic(data):
    print(data)
    date_sum = []

    for date in message_date:
        sum = 0
        authors = data[date].keys()
        for author in authors:
            sum += data[date][author]
        date_sum.append(sum)

        for author in authors:
            data[date][author] = data[date][author] / sum * 100

    # You can select date you want
    selected = '2022-05-21'
    selected_date_draw(data, selected)


def selected_date_draw(data, selected_date):
    authors = numpy.array(list(data[selected_date].keys()))
    percent = numpy.array(list(data[selected_date].values()))

    # Create the histogram
    fig = go.Figure(data=[go.Stream(x=authors, y=percent)])

    # Customize axes labels and title
    fig.update_layout(
        xaxis_title='X-axis',
        yaxis_title='Y-axis',
        title='Message Statistical Chart'
    )

    # Display the chart
    fig.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    preprocess()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

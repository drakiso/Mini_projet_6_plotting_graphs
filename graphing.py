from matplotlib import pyplot


def create_scatter(values_to_plot, name):
    x_data, y_data = values_to_plot

    figure = pyplot.figure()  # tell to pyplot create a new figure before creating the chart
    pyplot.scatter(x_data, y_data)
    figure.savefig(name)


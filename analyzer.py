import datetime

import numpy as np
import matplotlib.pyplot as plt


BAR_WIDTH = 20

class Analyzer(object):
  def __init__(self, datafile):
    self.datafile = datafile
    self.time_differences = []

  def _convert_from_unix_timestamp(self, timestamp):
    return datetime.datetime.fromtimestamp(int(timestamp))

  def _get_time_difference(self, time1, time2):
    return (self._convert_from_unix_timestamp(time2) - \
              self._convert_from_unix_timestamp(time1)).total_seconds()

  def _plot(self):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    x_strech = [i * BAR_WIDTH + (BAR_WIDTH / 2) for i, x  in \
                  enumerate(self.time_differences)]
    ax.plot(x_strech, self.time_differences, 'r-', linewidth=1)

    for i, data_point in enumerate(self.time_differences):
      ax.bar(i * BAR_WIDTH, data_point, width=BAR_WIDTH, alpha=.5,
             color='#223434', linewidth=1, edgecolor='#342222')

    plt.show()

  def run(self):
    previous_line = ''

    with open(self.datafile) as infile:
      for line in infile:
        # Skip blank lines and the first, empty, `difference'
        if line != '' and previous_line != '':
          line = line.strip('\n')
          self.time_differences.append(self._get_time_difference(
              line, previous_line))
        previous_line = line

    from pprint import pprint # DEBUG
    pprint(self.time_differences)  # DEBUG

    self._plot()


if __name__ == '__main__':
  # analyzer = Analyzer('./data/unixTimestamps')     # Comment/Uncomment
  analyzer = Analyzer('./data/unixTimestampsSample') # Comment/Uncomment
  analyzer.run()

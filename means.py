from statistics import median, mean, geometric_mean, harmonic_mean
import math
import random
import matplotlib.pyplot as plt



# various metrics
def mid_range(vals):
  return mean([max(vals), min(vals)])

def root_mean_square(vals):
  return math.sqrt(sum([v ** 2 for v in vals])/len(vals))


# general functions
def calc_all(vals):
  return {
    "mean": mean(vals),
    "gmean": geometric_mean(vals),
    "hmean": harmonic_mean(vals),
    "median": median(vals),
    "mid-range": mid_range(vals),
    "rms": root_mean_square(vals),
  }


def iterate(vals, n):
  history = []
  for i in range(n):
    labeled_vals = calc_all(vals)
    history.append(labeled_vals)
    vals = labeled_vals.values()
  return history


def check_convergence(history, epsilon=0.01):
  assert len(history) > 0

  for i in range(len(history)):
    row = history[i]
    if (max(row.values()) - min(row.values()) < epsilon):
      return i + 1

  return len(history)


def run_and_truncate(seed, n):
  history = iterate(seed, n)
  conv_point = check_convergence(history)
  return history[:conv_point]


def create_plot(history, plot=plt, show=True):
  assert len(history) > 0
  xs = range(len(history))
  lines = []

  for c in history[0]:
    line, = plot.plot(xs, [row[c] for row in history], label=c)
    lines.append(line)

  if show:
    plot.legend(handles=lines)
    plot.show()
  return plot


def generate_random_seed(min_seed_length, max_seed_length, min_value, max_value):
  length = random.randint(min_seed_length, max_seed_length)
  return [random.randint(min_value, max_value) for _ in range(length)]


def plot_many_seeds(n, max_seed_length, min_value=1, max_value=100):
  width = 8
  height = 8
  fig, plots = plt.subplots(width, height)
  for r in range(height):
    for c in range(width):
      seed = generate_random_seed(1, max_seed_length, min_value, max_value)
      history = run_and_truncate(seed, n)
      create_plot(history, plot=plots[r][c], show=False)

      # get legend
      if (r == 0 and c == 0):
        handles, labels = plots[0][0].get_legend_handles_labels()
        fig.legend(handles, labels)

  fig.set_size_inches(20, 10)
  plt.show()


def plot_seed_length_vs_convergence(max_length, seeds_per_length, n, epsilon=0.001, plot=plt, show=True):
  lengths = []
  conv_points = []

  for length in range(2, max_length):
    vals = []
    for i in range(2, seeds_per_length):
      seed = generate_random_seed(length, length, 1, 100)
      history = iterate(seed, n)
      conv_point = check_convergence(history, epsilon=epsilon)
      vals.append(conv_point)

    lengths.append(length)
    conv_points.append(mean(vals))


  plot.plot(lengths, conv_points)
  if show:
    plot.show()




# seed = [1, 2, 4, 5, 8, 123, 123]
# n = 10
# history = run_and_truncate(seed, n)
# create_plot(history)

# plot_many_seeds(10, 25)

plot_seed_length_vs_convergence(100, 100, 40)


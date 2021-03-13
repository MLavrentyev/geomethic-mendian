from statistics import median, mean, geometric_mean, harmonic_mean
import matplotlib.pyplot as plt


def calc_all(vals):
  return {"mean": mean(vals), "gmean": geometric_mean(vals), "hmean": harmonic_mean(vals), "median": median(vals)}


def iterate(vals, n):
  history = []
  for i in range(n):
    labeled_vals = calc_all(vals)
    history.append(labeled_vals)
    vals = labeled_vals.values()
  return history


def check_convergence(history, epsilon=0.001):
  assert len(history) > 0

  for i in range(len(history)):
    row = history[i]
    if (max(row.values()) - min(row.values()) < epsilon):
      return i

  return len(history)


def show_plot(history):
  assert len(history) > 0
  xs = range(len(history))
  lines = []

  for c in history[0]:
    line, = plt.plot(xs, [row[c] for row in history], label=c)
    lines.append(line)

  plt.legend(handles=lines)
  plt.show()


seed = [1, 5, 8, 4, 123, 123, 2]
n = 10
history = iterate(seed, n)
conv_point = check_convergence(history)
history = history[:conv_point]
show_plot(history)



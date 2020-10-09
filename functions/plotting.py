import matplotlib.pyplot as plt
import seaborn as sns


# Objects included in this file:

# Functions included in this file:
# # plot_empty (mpl)
# # plot_heatmap (sns)


def plot_empty(xlabel=None, ylabel=None,
               title=None,
               figsize=(8, 5)):
    """Initialize fig object for seaborns objects that do not include fig by default
    """
    fig = plt.figure(figsize=figsize, dpi=80)

    ax = fig.gca()
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_title(title, fontsize=16)

    return fig, ax


def plot_heatmap(df, xlabel=None, ylabel=None, title=None,
                 color='coolwarm', annot=False, fmt=None,
                 xticklabels=None, yticklabels=None,
                 order=None, figsize=(8, 5), dpi=240):
    """Heatmap is the same dimensions as input table
    """
    fig = plt.figure(figsize=figsize, dpi=dpi)

    if order:
        df = df[order]
    
    # annotations
    if fmt:
        sns.heatmap(df, xticklabels=xticklabels, yticklabels=yticklabels, cmap=color, annot=annot, fmt=fmt)
    else:
        sns.heatmap(df, xticklabels=xticklabels, yticklabels=yticklabels, cmap=color, annot=annot)

    ax = fig.gca()
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_title(title, fontsize=16)
    
    return fig, ax

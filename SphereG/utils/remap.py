def remap(value, old_range: tuple, new_range: tuple):
    percentage = value / (old_range[0] + old_range[1])
    return new_range[0] + (new_range[1] - new_range[0]) * percentage

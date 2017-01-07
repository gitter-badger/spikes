# coding=utf-8
def spike_data(data, rows):
    spiked = list()
    for _ in range(0, rows):
        spiked.append(list())

    for s in data:
        full_rows = s/8
        fraction_val = s - (full_rows * 8)

        for full_row in range(0, full_rows):
            spiked[full_row].append(8)
        if full_rows < rows:
            spiked[full_rows].append(fraction_val)
        for rest_row in range(full_rows+1, rows):
            spiked[rest_row].append(0)

    return spiked


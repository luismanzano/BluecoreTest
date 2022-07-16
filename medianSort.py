

def median_sort(array):
    highest_median = 0
    index_to_sort = 0

    for idx, element in enumerate(array):
        if isinstance(element, list):
            avg = sum(element) / len(element)
            element.append(avg)
        else:
            avg = element
            array[idx] = [element, avg]

        if avg > highest_median:
            highest_median = avg
            index_to_sort = idx

    sorted_array = array[index_to_sort:]
    sorted_array.sort(key=lambda median: median[-1])

    if index_to_sort > 0:
        sorted_array = array[0:index_to_sort] + sorted_array
        sorted_array = remove_means(sorted_array)
        return sorted_array

    sorted_array = remove_means(sorted_array)
    return sorted_array


def remove_means(array):
    for element in array:
        element.pop()
    return array


if __name__ == '__main__':
    test1 = [[2.4, 0.2, 9.8], 0, [-1], [-9, -4]]

    print(median_sort(test1))

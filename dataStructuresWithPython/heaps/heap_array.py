class HeapStructure(object):
    def __init__(self, heap_type='max'):
        """
        :param heap_type: max/min heap
        """
        self.heap_elements = []
        self.heap_type = heap_type

    def _insert(self, element):
        l = len(self.heap_elements)
        self.heap_elements.append(element)
        self._percolate_up(l)

    def _delete(self, element):
        idx = self.heap_elements.index(element)
        idx_last_element = len(self.heap_elements) - 1
        self._swap_heap_elements(idx, idx_last_element)
        self.heap_elements.pop(idx_last_element)
        self._percolate_down(idx)

    def _maximum_in_heap(self):
        maximum = float("-inf")
        for i in self.heap_elements:
            if i > maximum:
                maximum = i
        return maximum

    def _minimum_in_heap(self):
        minimum = float("inf")
        for i in self.heap_elements:
            if i < minimum:
                minimum = i
        return minimum

    def _get_max(self):
        if self.heap_type == 'max':
            return self.heap_elements[0]
        else:
            return self._maximum_in_heap()

    def _get_min(self):
        if self.heap_type == 'min':
            return self.heap_elements[0]
        else:
            return self._minimum_in_heap()

    def _percolate_up(self, current_index):
        parent_index = current_index // 2
        while parent_index:
            if self.heap_type == 'max':
                if self.heap_elements[parent_index] < self.heap_elements[current_index]:
                    self._swap_heap_elements(index1=parent_index, index2=current_index)
                parent_index //= 2
            else:
                if self.heap_elements[parent_index] > self.heap_elements[current_index]:
                    self._swap_heap_elements(index1=parent_index, index2=current_index)

                parent_index //= 2

    def _swap_heap_elements(self, index1, index2):
        tmp = self.heap_elements[index1]
        self.heap_elements[index1] = self.heap_elements[index2]
        self.heap_elements[index2] = tmp

    def _percolate_down(self, idx):
        left_child = 2 * idx + 1
        right_child = 2 * idx + 2
        if len(self.heap_elements) < left_child or len(self.heap_elements) < right_child:
            return
        if self.heap_type == 'max':
            max_element = max(self.heap_elements[idx],
                                   self.heap_elements[left_child],
                                   self.heap_elements[right_child])
            replacable_idx = self.heap_elements.index(max_element)
        else:
            min_element = min(self.heap_elements[idx],
                                   self.heap_elements[left_child],
                                   self.heap_elements[right_child])
            replacable_idx = self.heap_elements.index(min_element)

        if replacable_idx == idx: return

        self._swap_heap_elements(idx, replacable_idx)
        self._percolate_down(replacable_idx)

    def _show_heap(self):
        for i in self.heap_elements:
            print(i, end=' ')
        print()

# Example of HEAP

heap = HeapStructure()
heap._insert(6)
heap._insert(5)
heap._insert(2)
heap._insert(1)
heap._insert(4)
heap._insert(3)

heap._show_heap()

print('Maximum - ', heap._get_max())
print('Minimum - ', heap._get_min())

heap._delete(2)

heap._show_heap()

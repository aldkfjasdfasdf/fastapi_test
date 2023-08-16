import time


class SortTime:
    @staticmethod
    def bubble_sort(arr: list):
        start_time = time.time()
        n = len(arr)

        for i in range(n):
            for j in range(0, n - i - 1):
                if str(arr[j]) > str(arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        end_time = time.time()
        elapsed_time = end_time - start_time
        return arr, elapsed_time

    @staticmethod
    def quick_sort(arr: list):
        start_time = time.time()

        if len(arr) <= 1:
            end_time = time.time()
            elapsed_time = end_time - start_time
            return arr, elapsed_time

        pivot = arr[len(arr) // 2]
        left = [x for x in arr if str(x) < str(pivot)]
        middle = [x for x in arr if str(x) == str(pivot)]
        right = [x for x in arr if str(x) > str(pivot)]

        left_sorted, left_time = SortTime.quick_sort(left)
        right_sorted, right_time = SortTime.quick_sort(right)

        sorted_arr = left_sorted + middle + right_sorted

        end_time = time.time()
        elapsed_time = end_time - start_time + left_time + right_time
        return sorted_arr, elapsed_time

    @staticmethod
    def book_sort(arr: list):
        start_time = time.time()

        shelf = []

        for book in arr:
            inserted = False
            for i in range(len(shelf)):
                if str(book) < str(shelf[i]):
                    shelf.insert(i, book)
                    inserted = True
                    break

            if not inserted:
                shelf.append(book)

        end_time = time.time()

        elapsed_time = end_time - start_time

        return shelf, elapsed_time

    @staticmethod
    def alphabet_sort(arr: list):
        start_time = time.time()

        arr.sort(key=lambda x: str(x))

        end_time = time.time()

        elapsed_time = end_time - start_time
        return arr, elapsed_time

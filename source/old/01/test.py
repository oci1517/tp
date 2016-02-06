from time import time

from compute import job, count
from data import a_list, n_list, test_results

def timeit(process, n=10):
    total_time = 0

    for _ in range(n):
        t0 = time()
        process()
        t1 = time()

        total_time += t1 - t0

    return total_time / n


def assert_list_equal(list1, list2):
    assert len(list1) == len(list2)
    for i in range(len(list1)):
        try:
            assert list1[i] == list2[i]
        except Exception as e:
            print(e)
            print("lists differ at index:", i, "==> (", list1[i], "!=", list2[i], ")")


def test():
    # test correctness
    results = job(a_list, n_list)
    print(results)
    assert_list_equal(results, test_results)


    compute_time = timeit(lambda: job(a_list, n_list), n=10)
    print("Compute time : ", compute_time)


if __name__ == '__main__':
    test()

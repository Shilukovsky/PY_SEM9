from DZ1_SEM3 import get_sum


def test_sum():
    a = [4, 7, 9, 4, 3, 0]

    b = []
    for i in range(len(a)):
        if (i % 2) != 0:
            b.append(a[i])

    assert get_sum(b)

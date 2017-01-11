from core.utils.coord import convert_to_number


def test_convert_to_number_all():
    k = 0
    for i in range(3):
        for j in range(3):
            assert convert_to_number(j, i) == k
            k += 1

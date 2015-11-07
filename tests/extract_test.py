import numaster


def test_extract():
    table = [
        ("No. 1 and No. 2", ["1", "2"]),
        ("百一番", ["百一"]),
    ]
    for source, expect in table:
        assert numaster.extract(source) == expect

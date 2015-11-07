import numaster


def test_normalize():
    table = [
        (("1", None, None), "1"),
        (("一", None, None), "1"),
        (("十", None, None), "10"),
        (("一〇", None, None), "10"),
        (("十一", None, None), "11"),
        (("一一", None, None), "11"),
        (("二十", None, None), "20"),
        (("百", None, None), "100"),
        (("百一", None, None), "101"),
        (("百十一", None, None), "111"),
        (("百二十一", None, None), "121"),
        (("百二一", None, None), "121"),
        (("2百", None, None), "200"),
        (("２百", None, None), "200"),
        (("二百", None, None), "200"),
        (("一二一", None, None), "121"),
        (("千一", None, None), "1001"),
        (("千百", None, None), "1100"),
        (("二千百一", None, None), "2101"),
        (("一百万", None, None), "1000000"),
        (("一兆二千万", None, None), "1000020000000"),
        (("1,000", None, ','), "1000"),
        (("1,000,000", None, ','), "1000000"),
        (("10割", None, None), "1"),
        (("１厘", None, None), "0.001"),
        (("1%", None, None), "0.01"),
        (("100%", None, None), "1"),
        (("1.00", '.', None), "1"),
    ]
    for source, expect in table:
        assert numaster.normalize(*source) == expect, (source, expect)

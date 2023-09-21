def test_sort_string_by_frequency():
    assert sort_string_by_frequency("llloohe wrd") == "lllooeeh wrd"
    assert sort_string_by_frequency("hello world") == "lllooehdw r"
    assert sort_string_by_frequency("aaabbbccc") == "aaabbbccc"
    assert sort_string_by_frequency("abababab") == "aaaaabbb"
    assert sort_string_by_frequency("") == ""

test_sort_string_by_frequency()

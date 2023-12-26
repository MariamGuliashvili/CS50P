from twttr import shorten


def test_shorten():
    x = ["a","e","i","u","A","E","I","O","U"]
    for i in x:
        assert shorten(str(i)) == ""
    assert shorten("1") == "1"
    assert shorten("w") == "w"
    assert shorten(",") == ","

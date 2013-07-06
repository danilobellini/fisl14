def t9(msg):
  table = {
    "a": "2",
    "b": "22",
    "c": "222",
    "d": "3",
  }
  try:
    return table[msg]
  except KeyError:
    result = [t9(char) for char in msg]
    for idx, blk in enumerate(result[:-1]):
      next_blk = result[idx + 1]
      if blk[0] == next_blk[0]:
        result[idx] = blk + "_"
    return "".join(result)

def test_a():
  assert t9("a") == "2"

def test_d():
  assert t9("d") == "3"

def test_b():
  assert t9("b") == "22"

def test_c():
  assert t9("c") == "222"

def test_abc():
  assert t9("abc") == "2_22_222"

def test_abcd():
  assert t9("abcd") == "2_22_2223"

def test_danilo():
  assert t9("Danilo") == "3266444555666"

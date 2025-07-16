def test(name, func):
    try:
        func()
        print(f"[PASS] {name}")
    except Exception as e:
        print(f"[FAIL] {name}: {type(e).__name__}: {e}")

def run_tests_on(StackClass):
    def test_stack_operations():
        s = StackClass()
        assert s.is_empty()
        assert len(s) == 0

        s.push(10)
        s.push(20)
        s.push(30)

        assert not s.is_empty()
        assert len(s) == 3
        assert s.size() == 3
        assert s.peek() == 30
        assert s.top() == 30
        assert s.pop() == 30
        assert s.pop() == 20
        assert s.pop() == 10
        assert s.is_empty()

    def test_add_and_iadd():
        a = StackClass([1, 2])
        b = StackClass([3, 4])
        c = a + b
        assert isinstance(c, StackClass)
        assert list(c) == [4, 3, 2, 1]

        a += b
        assert list(a) == [4, 3, 2, 1]

    def test_equality_and_getitem():
        a = StackClass([1, 2, 3])
        b = StackClass([1, 2, 3])
        c = StackClass([3, 2, 1])
        assert a == b
        assert a != c
        assert a[0] == 1
        assert a[-1] == 3

    def test_clear_and_contains():
        s = StackClass([5, 10, 15])
        assert 10 in s
        s.clear()
        assert s.is_empty()
        assert len(s) == 0

    def test_iter_and_repr():
        s = StackClass([1, 2, 3, 4, 5, 6])
        assert list(s) == [6, 5, 4, 3, 2, 1]
        r = repr(s)
        assert "Stack" in r

    def test_exceptions():
        s = StackClass()
        try:
            s.pop()
            raise AssertionError("Expected IndexError not raised")
        except IndexError:
            pass

        try:
            s.peek()
            raise AssertionError("Expected AttributeError not raised")
        except AttributeError:
            pass

        try:
            _ = s + [1, 2]
            raise AssertionError("Expected TypeError not raised in __add__")
        except TypeError:
            pass

        try:
            s += [1, 2]
            raise AssertionError("Expected TypeError not raised in __iadd__")
        except TypeError:
            pass

    # Run all tests
    test("Basic push/pop/peek", test_stack_operations)
    test("Add and IAdd behavior", test_add_and_iadd)
    test("Equality and GetItem", test_equality_and_getitem)
    test("Clear and Contains", test_clear_and_contains)
    test("Iteration and Repr", test_iter_and_repr)
    test("Exception Handling", test_exceptions)

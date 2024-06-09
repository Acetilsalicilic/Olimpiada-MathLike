from unittest import TestCase, main
#from solucion import find_sublists as find_sublists_sol
from find_sublist import find_sublists

result_sol = {
    
}

def check_sublist_correctness(L: list[int], t: int) -> None:
    #result_sol = find_sublists_sol(L, t)
    result = find_sublists(L, t)
    for sublist in result:
        sublist.sort()
        assert sublist in result_sol, f"Error: {sublist} is wrong"
    for sublist_sol in result_sol:
        sublist_sol.sort()
        assert sublist_sol in result, f"Error: {sublist_sol} not found"

def there_is_value_error(L: list[int], t: int) -> bool:
    try:
        find_sublists(L, t)
    except ValueError:
        return True
    return False



class TestFindSublists(TestCase):
    def test_1(self):
        L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        t = 10
        check_sublist_correctness(L, t)
    
    def test_2(self):
        L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        t = 20
        check_sublist_correctness(L, t)
    
    def test_3(self):
        L = [1, 1, 2, 3, 5, 8, 11, 11, 13, 17, 19, 55]
        t = 55
        check_sublist_correctness(L, t)
    
    def test_4(self):
        L = [1, 1, 2, 3, 5, 8, 11, 11, 13, 17, 19, 55]
        t = 110
        check_sublist_correctness(L, t)
    
    def test_5(self):
        L = []
        t = 1
        check_sublist_correctness(L, t)
    
    def test_6(self):
        L = [-1.2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        t = 10
        assert there_is_value_error(L, t) is True, "Error: there should be a ValueError"
    
    def test_7(self):
        L = [1, 1, 1]
        t = 1
        check_sublist_correctness(L, t)


if __name__ == '__main__':
    main()

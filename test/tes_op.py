from src.maths import add,sub




def test_add():
    assert add(3,5) == 8
   
    assert add (1,-1) == 0

  

def test_sub():
    assert sub (5,1) == 4
    assert sub (1,1) == 0
    
    
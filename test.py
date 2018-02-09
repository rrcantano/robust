from workshop_assert import mean4

#TEST standard behaviour of my function mean

def test_ints():
    #test behaviour of my code: gets what you expect
    num_list = [1,2,3,4,5]
    obs = mean4(num_list)
    exp = 3
    assert obs == exp



def test_double():
    #test if takes double values, not just integer
    num_list = [1.,2.,3.,4.]
    obs = mean4(num_list)
    exp = 2.5
    assert obs == exp


def test_long():
    #check big number are accepted
    big = 10000000
    obs = mean4(range(1,big))
    exp = big/2.
    assert obs == exp

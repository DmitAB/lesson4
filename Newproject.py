

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function() # так мы её не можем запустить отдельно, только вместе с test_function()

#inner_function() # так не видно этой функции потому что она \
                    # относится не к глобальному, а к локальному пространству

test_function()
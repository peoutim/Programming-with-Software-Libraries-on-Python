# using_our_indicators.py
#
# ICS 32 Winter 2013
# Code Example
#
# A quick example of using our indicators, including using them within
# functions that are not aware of which kind of indicators they're
# being given.

import example_indicators



def quick_indicator_test():
    # Note, first, how the indicator generators each behave differently.
    # A ZeroIndicator gives back nothing but zeros.  The two
    # OddEvenIndicators, on the other hand, each give back different
    # "X" values (the first gives +3 and -3, the second gives +5 and -5)
    # based on a value passed to their constructors.

    print('quick_indicator_test')
    
    zi = example_indicators.ZeroIndicator()
    print(zi.execute([10, 9, 8, 7, 6]))

    oei1 = example_indicators.OddEvenIndicator(3)
    print(oei1.execute([1, 2, 3, 4, 5]))

    oei2 = example_indicators.OddEvenIndicator(5)
    print(oei2.execute([7, 8, 9, 10, 11]))

    print()
    print()



def print_all_indicators(indicators):
    '''This function accepts a list of indicators as a parameter.
    It calls each of the indicators, in the order they appear in
    the list, against the same list of prices, printing out the
    indicator values generated by each indicator.'''

    print('print_all_indicators')

    for indicator in indicators:
        print(indicator.execute([35, 36, 37, 38, 39, 40]))

    print()
    print()



def using_indicators_interchangeably():
    zi = example_indicators.ZeroIndicator()
    oei1 = example_indicators.OddEvenIndicator(6)
    oei2 = example_indicators.OddEvenIndicator(14)
    print_all_indicators([zi, oei1, oei2])
    print_all_indicators([oei2, zi, oei1])
    print_all_indicators([zi, zi, zi, zi])
    print_all_indicators([oei1, oei2])



if __name__ == '__main__':
    quick_indicator_test()
    using_indicators_interchangeably()
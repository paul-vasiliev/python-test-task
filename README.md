# Japanese flag

The purpose of the task is to implement a function that will accept a single input parameter N and output a string with an ASCII art of the japanese flag.

Here is an example of flags for various values of N:

    N = 2                           N = 6
    ########                        ####################
    #      #                        #                  #
    #  **  #                        #                  #
    #  **  #                        #                  #
    #      #                        #        **        #
    ########                        #       *oo*       #
                                    #      *oooo*      #
    N = 4                           #      *oooo*      #
    ##############                  #       *oo*       #
    #            #                  #        **        #
    #            #                  #                  #
    #     **     #                  #                  #
    #    *oo*    #                  #                  #
    #    *oo*    #                  ####################
    #     **     #
    #            #
    #            #
    ##############
    

    

The following is a list of requirements for the function:

- The input N shall be an integer even number
- The width of the inner area of the rectangle (excluding border) shall be 3 * N
- The height of the inner area of the rectangle (excluding border) shall be 2 * N
- The vertical distance between the circle and the border of the rectangle shall be N/2
- The horizontal distance between the circle and the border of the rectangle shall be N
- `#` symbol shall be used for rectangle border, `*` symbol shall be used for the circle border, `o` symbol shall be used for inner circle area
- The function shall return a string and use `\n` as line separators
- The function shall accept a single parameter N
- If the parameter is not a valid even integer number the `ArgumentError` exception shall be thrown
- The result of the task shall be provided a single python file named `flag.py` with a function named `flag` defined in it

"""
    Towers of hanoi problem solution with recursion.
"""

def towersOfHanoi(n, frompeg, topeg, auxpeg):
    if n == 1:
        # if only one disk make the move and return.
        print("Move disk 1 from {} to {}".format(frompeg, topeg))
        return
    # Move n-1 disks from A to B using C as auxilary
    towersOfHanoi(n-1, frompeg,auxpeg,topeg)

    # move remaining disks from A to C
    print("Move disk {} peg {} from {} peg to {}".format(n,frompeg, topeg))
    
    # Move n-1 disks from B to C using A as auxilary
    towersOfHanoi(n-1, auxpeg,topeg,frompeg)

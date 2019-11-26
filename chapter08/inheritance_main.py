#inheritance_main
from chapter08.inheritance_study import Bicycle, FoldBicycle

if __name__ == "__main__":
    myBicycle = Bicycle(wheel_size=20, color="red")
    myFoldBicycle = FoldBicycle(wheel_size=30, color="blue", state='unfolding')

    cycle_list = [myBicycle, myFoldBicycle]

    [cycle.move(30) for cycle in cycle_list]
    [cycle.stop() for cycle in cycle_list]

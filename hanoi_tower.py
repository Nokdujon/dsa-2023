"""Hanoi Tower"""


def hanoi_tower(disks: int, src: str, helper: str, dst: str) -> None:
    """Function recursive function for Hanoi Tower"""

    # Base Condition
    if disks == 1:
        print(f"Disk {disks} moves from tower {src} to tower {dst}.")
        return

    hanoi_tower(disks - 1, src, dst, helper)
    print(f"Disk {disks} moves from tower {src} to tower {dst}.")
    hanoi_tower(disks - 1, helper, src, dst)


hanoi_tower(4, "A", "B", "C")

from enum import IntEnum

class direction(IntEnum):
    UP=0
    DOWN=1
    LEFT=2
    RIGHT=3

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = [0,0]
        facing = direction.UP
        for instruction in instructions:
            if facing == direction.UP:
                if instruction == 'G':
                    pos[1]+=1
                elif instruction == 'L':
                    facing = direction.LEFT
                else:
                    facing = direction.RIGHT
            elif facing == direction.DOWN:
                if instruction == 'G':
                    pos[1]-=1
                elif instruction == 'L':
                    facing = direction.RIGHT
                else:
                    facing = direction.LEFT
            elif facing == direction.LEFT:
                if instruction == 'G':
                    pos[0]-=1
                elif instruction == 'L':
                    facing = direction.DOWN
                else:
                    facing = direction.UP
            elif facing == direction.RIGHT:
                if instruction == 'G':
                    pos[0]+=1
                elif instruction == 'L':
                    facing = direction.UP
                else:
                    facing = direction.DOWN

        return facing != direction.UP or pos[0] == pos[1] == 0


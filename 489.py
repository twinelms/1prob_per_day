class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        path = set()
        def dfs(x, y, dx, dy):
            robot.clean()
            path.add((x, y))
            for _ in range(4):
                if (x+dx, y+dy) not in path and robot.move():
                    dfs(x+dx, y+dy, dx, dy)
                robot.turnLeft()
                dx, dy = -dy, dx
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()
        dfs(0, 0, 0, 1)

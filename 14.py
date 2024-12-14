
class Robot:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

def solve_1():
    w, h = 101, 103

    robots = []
    for line in open("input.txt"):
        pos, vel = line.split(" ")
        pos = pos.replace("p=", "")
        vel = vel.replace("v=", "")
        pos = [int(v) for v in pos.split(",")]
        vel = [int(v) for v in vel.split(",")]
        robots.append(Robot(pos[0], pos[1], vel[0], vel[1]))

    for i in range(100):
        for r in robots:
            r.x += r.vx
            r.y += r.vy

            if r.x < 0:
                r.x = w - abs(r.x)
            if r.x >= w:
                r.x = r.x % w
            if r.y < 0:
                r.y = h - abs(r.y)
            if r.y >= h:
                r.y = r.y % h

    q_top_left = 0
    q_top_right = 0
    q_bottom_left = 0
    q_bottom_right = 0

    for r in robots:
        if r.x < w // 2 and r.y < h // 2:
            q_top_left += 1
        elif r.x > w // 2 and r.y < h // 2:
            q_top_right += 1
        elif r.x < w // 2 and r.y > h // 2:
            q_bottom_left += 1
        elif r.x > w // 2 and r.y > h // 2:
            q_bottom_right += 1
    
    result = q_top_left * q_top_right * q_bottom_left * q_bottom_right
    print(result)
             

def solve_2():
    w, h = 101, 103

    robots = []
    for line in open("input.txt"):
        pos, vel = line.split(" ")
        pos = pos.replace("p=", "")
        vel = vel.replace("v=", "")
        pos = [int(v) for v in pos.split(",")]
        vel = [int(v) for v in vel.split(",")]
        robots.append(Robot(pos[0], pos[1], vel[0], vel[1]))

    for i in range(20000):
        if i % 500 == 0:
            print(i)
        for r in robots:
            r.x += r.vx
            r.y += r.vy

            if r.x < 0:
                r.x = w - abs(r.x)
            if r.x >= w:
                r.x = r.x % w
            if r.y < 0:
                r.y = h - abs(r.y)
            if r.y >= h:
                r.y = r.y % h


        q_top_left = 0
        q_top_right = 0
        q_bottom_left = 0
        q_bottom_right = 0

        for r in robots:
            if r.x < w // 2 and r.y < h // 2:
                q_top_left += 1
            elif r.x > w // 2 and r.y < h // 2:
                q_top_right += 1
            elif r.x < w // 2 and r.y > h // 2:
                q_bottom_left += 1
            elif r.x > w // 2 and r.y > h // 2:
                q_bottom_right += 1

        if i > 84 and (i - 84 + 1) % 101 == 0:
            from PIL import Image
            image = Image.new("1", (w, h), 1)  

            pixels = image.load()

            for r in robots:
                pixels[r.x, r.y] = 0 

            image.save(f"{i}.png")

if __name__ == '__main__':
    solve_1()
    solve_2()
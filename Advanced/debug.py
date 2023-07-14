# 保留最后N个元素
# 使用collections.deque()

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            # use yield can return a generator object, next time can be used in the space from the last position
            yield line, previous_lines
        previous_lines.append(line)


# Example use on a file
if __name__ == '__main__':
    with open('./test.txt') as f:
        for line, prevlines in search(f, 'txt', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item
    if (self.current + 1) == self.capacity:
      self.current = 0
    else:
      self.current += 1

  def get(self):
    arr = []
    for i in range(len(self.storage)):
      if self.storage[i] is not None:
        arr.append(self.storage[i])
    print(arr)
    return arr

    # # start at current
    # pointer2 = self.current
    # # make empty array to return
    # arr = []
    # # loop over storage array
    # while True:
    #   # check if item is None
    #   if self.storage[pointer2] is not None:
    #     # append item to array to be returned
    #     arr.append(self.storage[pointer2])
    #   # check if pointer needs to be set to 0
    #   if (pointer2 + 1) != self.capacity:
    #     pointer2 += 1
    #   else:
    #     pointer2 = 0
    #   if pointer2 == self.current:
    #     return arr
    

# TEST CASES

# buffer = RingBuffer(3)

# # buffer.get()   # should return []

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# # print(buffer.storage)

# print(buffer.get())   # should return ['a', 'b', 'c']

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# print(buffer.get())   # should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# print(buffer.get())   # should return ['d', 'e', 'f']
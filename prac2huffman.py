
import heapq
from collections import Counter

def huffman_encoding(text):
    freq = Counter(text)
    heap = [[f, [ch, ""]] for ch, f in freq.items()]
    heapq.heapify(heap)

    if not heap:
        return {}

    if len(heap) == 1:
        ch = heap[0][1][0]
        return {ch: "0"}

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        for item in left[1:]:
            item[1] = "0" + item[1]

        for item in right[1:]:
            item[1] = "1" + item[1]

        heapq.heappush(
            heap, [left[0] + right[0]] + left[1:] + right[1:]
        )

    return {ch: code for ch, code in heap[0][1:]}


text = input("Enter a string: ")
codes = huffman_encoding(text)

print("\nHuffman Codes:")
for ch, code in sorted(codes.items()):
    print(f"{repr(ch)} : {code}")

encoded = "".join(codes[ch] for ch in text)
print("\nEncoded String:", encoded)

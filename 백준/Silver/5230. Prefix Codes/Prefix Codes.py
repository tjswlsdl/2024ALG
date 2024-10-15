import sys

def main():
    lines = sys.stdin.readlines()
    T = int(lines[0])
    line_idx = 1
    for _ in range(T):
        # Skip empty lines
        while line_idx < len(lines) and lines[line_idx].strip() == '':
            line_idx += 1
        if line_idx >= len(lines):
            break
        tokens = lines[line_idx].strip().split()
        line_idx += 1
        while len(tokens) < 2:
            # Read next line
            tokens.extend(lines[line_idx].strip().split())
            line_idx += 1
        k = int(tokens[0])
        code_str = tokens[1]
        messages = tokens[2:]
        while len(messages) < k:
            # Read more messages
            if line_idx >= len(lines):
                break
            messages.extend(lines[line_idx].strip().split())
            line_idx += 1
        # Now process the test case
        # Build the tree
        N = len(code_str)
        nodes = [{} for _ in range(N)]
        for k_index in range(N):
            c = code_str[k_index]
            node = {'value': None, 'left': None, 'right': None}
            if c != '*':
                node['value'] = c
            left_index = 2 * k_index + 1
            right_index = 2 * k_index + 2
            if left_index < N:
                node['left'] = left_index
            if right_index < N:
                node['right'] = right_index
            nodes[k_index] = node
        # Decode messages
        results = []
        for message in messages[:k]:
            result = ''
            index = 0  # Start at root
            for bit in message:
                if index is None:
                    break
                if bit == '0':
                    index = nodes[index].get('left')
                elif bit == '1':
                    index = nodes[index].get('right')
                else:
                    # Invalid bit, skip
                    continue
                if index is None:
                    break  # Invalid message
                if nodes[index]['value'] is not None:
                    result += nodes[index]['value']
                    index = 0  # Reset to root
            results.append(result)
        print(' '.join(results))

if __name__ == "__main__":
    main()

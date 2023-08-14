with open('input.txt') as f:
    input_stream = f.readline().rstrip()

# PART 1
last_four = []

def start_packet_marker(input_stream, last_four = []):
    
    processed_character_count = 0

    # Go through the input stream
    while len(last_four) > len(set(last_four)) or len(last_four) < 4:

        if len(last_four) < 4:
            last_four.append(input_stream[processed_character_count])
        
        else:
            last_four.append(input_stream[processed_character_count])
            last_four.pop(0)

        processed_character_count += 1
    
    return processed_character_count, last_four

processed_character_count, last_four = start_packet_marker(input_stream)
print(processed_character_count)
print(last_four)

# PART 2
last_fourteen = []

def start_message_marker(input_stream, last_fourteen = []):
    
    processed_character_count = 0

    # Go through the input stream
    while len(last_fourteen) > len(set(last_fourteen)) or len(last_fourteen) < 14:

        if len(last_fourteen) < 14:
            last_fourteen.append(input_stream[processed_character_count])
        
        else:
            last_fourteen.append(input_stream[processed_character_count])
            last_fourteen.pop(0)

        processed_character_count += 1
    
    return processed_character_count, last_fourteen

processed_character_count, last_fourteen = start_message_marker(input_stream)
print(processed_character_count)
print(last_fourteen)


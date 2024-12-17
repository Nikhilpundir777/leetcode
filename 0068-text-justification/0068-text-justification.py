class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current_line = []
        current_line_length = 0
        
        for word in words:
            # Check if adding this word exceeds the maxWidth
            if current_line_length + len(word) + len(current_line) > maxWidth:
                # Justify the current line and add it to the result
                result.append(self.justify(current_line, maxWidth, current_line_length))
                
                # Start a new line with the current word
                current_line = [word]
                current_line_length = len(word)
            else:
                # Add the word to the current line
                current_line.append(word)
                current_line_length += len(word)
        
        # Handle the last line, which should be left-justified
        result.append(self.leftJustify(current_line, maxWidth))
        
        return result

    def justify(self, line, maxWidth, line_length):
        # If there is only one word in the line, it's left-justified
        if len(line) == 1:
            return line[0] + ' ' * (maxWidth - len(line[0]))

        # Calculate the number of spaces to distribute
        spaces_to_distribute = maxWidth - line_length
        space_between_words = spaces_to_distribute // (len(line) - 1)
        extra_spaces = spaces_to_distribute % (len(line) - 1)

        # Create the justified line
        justified_line = line[0]
        for i in range(1, len(line)):
            # Add the appropriate number of spaces
            justified_line += ' ' * (space_between_words + (1 if i <= extra_spaces else 0))
            justified_line += line[i]

        return justified_line

    def leftJustify(self, line, maxWidth):
        # Join the words with one space and then add trailing spaces to the right
        line_str = ' '.join(line)
        return line_str + ' ' * (maxWidth - len(line_str))
        
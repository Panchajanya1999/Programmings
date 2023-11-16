class Solution:
    def findDifferentBinaryString(self, binaryStrings: List[str]) -> str:
        result = []

        # Iterate through each binary string in the list
        for i in range(len(binaryStrings)):
            # Access the i-th character of the i-th binary string
            current_character = binaryStrings[i][i]

            # Append the opposite binary value to the result string
            result.append('1' if current_character == '0' else '0')

        # Return the resulting binary string
        return ''.join(result)

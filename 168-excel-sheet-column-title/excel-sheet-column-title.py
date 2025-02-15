class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        This function converts an excel column number to its corresponding title.
        For example, column number 1 corresponds to "A", column number 26 corresponds to "Z", 
        column number 27 corresponds to "AA", and so on.
        
        :type columnNumber: int
        :rtype: str
        """
        # Initialize an empty string to store the result
        result = ""
        
        # Loop until the column number is 0
        while columnNumber > 0:
            # Calculate the remainder of columnNumber divided by 26
            remainder = columnNumber % 26
            
            # If remainder is 0, set it to 26
            if remainder == 0:
                remainder = 26
                # Subtract 26 from columnNumber
                columnNumber -= 26
            
            # Convert the remainder to its corresponding character using the ASCII value
            # and add it to the result string
            result = chr(64 + remainder) + result
            
            # Update columnNumber by performing integer division by 26
            columnNumber //= 26
        
        # Return the result string
        return result

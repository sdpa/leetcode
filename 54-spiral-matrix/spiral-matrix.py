class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        r_start, c_start = 0, 0
        r_end, c_end = len(matrix) -1, len(matrix[0]) - 1
        output = []
        while(r_start <= r_end and c_start <= c_end):
            # Right
            for i in range(c_start, c_end+1):
                output.append(matrix[r_start][i])
            r_start += 1
            # print(output)

            # down
            for i in range(r_start, r_end+1):
                output.append(matrix[i][c_end])
            c_end -= 1
            # print(output)
            # reft
            if(r_start <= r_end):
                for i in range(c_end, c_start-1, -1):
                    output.append(matrix[r_end][i])
                r_end -= 1
            # print(output)
            # # Up
            if(c_start <= c_end):
                for i in range(r_end, r_start-1, -1):
                    output.append(matrix[i][c_start])
                c_start += 1
            # print(output)

            print(r_start, c_start, r_end, c_end)
        return output
            
            




        


            
            

            
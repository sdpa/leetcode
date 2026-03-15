class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def combination(cur_comb, target, index):
            if target == 0:
                res.append(list(cur_comb))

            if target < 0:
                return
            
            for i in range(index, len(candidates)):
                cur_comb.append(candidates[i])
                combination(cur_comb, target - candidates[i], i)
                cur_comb.pop()
        
        combination([], target, 0)

        return res


        
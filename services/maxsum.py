from ..utils.handler import CustomHandler
import json


class MaxSum(CustomHandler):
    async def post(self):
        body = json.loads(self.request.body)
        result = self.get_max_sum_of_subarray(body['list'])
        
        self.set_status(200)
        self.write(json.dumps({"result": result}))
        self.finish()
        
    
    def get_max_sum_of_subarray(self, array):
        """Get Max sum of subarray
        Eager algorithm to find and calculate the maximum subarray sum
        
        :param array: array of numbers 
        """
        total_max = None
        local_max = 0

        for item in array:
            local_max = local_max + item
            if total_max is None or local_max > total_max:
                total_max = local_max
            if local_max < 0:
                local_max = 0

        return total_max
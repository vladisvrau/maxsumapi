from utils.handler import CustomHandler
import json


class MaxSum(CustomHandler):
    async def post(self):
        try:
            body = json.loads(self.request.body)
            
            # Exception Management
            assert len(body.get('list', [])) > 0, "Lista inválida."
            assert all([isinstance(item, (int, float)) for item in body['list']]), "A lista deve ser composta somente por números"
            
            # Calculating Result
            result = self.get_max_sum_of_subarray(body['list'])
            
            # Delivering the payload
            self.set_status(200)
            self.write(json.dumps({"result": result}))
        
        except AssertionError as ass:
            self.set_status(400)
            self.write(json.dumps({"message": ass}))
        
        except Exception as exp:
            self.set_status(500)
            self.write(json.dumps({"message": "Erro interno no servidor"}))
        
        finally:
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
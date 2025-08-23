class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution = []
        current = 1           # producto de todos los no-cero
        zero_count = 0

        # 1) producto de no-ceros y conteo de ceros
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                current *= num

        # 2) construir resultado según # de ceros
        if zero_count >= 2:
            # dos o más ceros -> todo es 0
            return [0] * len(nums)

        for num in nums:
            if zero_count == 1:
                # un solo cero -> solo en la posición del cero va el producto de los demás
                if num == 0:
                    solution.append(current)
                else:
                    solution.append(0)
            else:
                # sin ceros -> dividir por el propio num
                # usamos // porque la división es exacta entre enteros
                solution.append(current // num)

        return solution
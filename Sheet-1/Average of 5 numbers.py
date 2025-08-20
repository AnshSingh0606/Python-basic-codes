nums = []
for i in range(5):
    n = int(input(f"Enter number {i+1}: "))
    nums.append(n)
average = sum(nums) / 5
print("Average:", average)

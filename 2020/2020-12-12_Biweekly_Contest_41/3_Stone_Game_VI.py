# import math
#
#
# def stoneGameVI(aliceValues, bobValues):
#     diff_alice = []
#     diff_bob = []
#     dim = len(aliceValues)
#     for i in range(dim):
#         diff_alice.append(aliceValues[i] - bobValues[i])
#         diff_bob.append(bobValues[i] - aliceValues[i])
#     #print(diff_alice)
#     #print(diff_bob)
#     points_A = 0
#     points_B = 0
#     count = 0
#     while count < dim:
#         next_index_Alice = diff_alice.index(max(diff_alice))
#         points_A += aliceValues[next_index_Alice]
#         aliceValues[next_index_Alice] = 0
#         bobValues[next_index_Alice] = 0
#         diff_alice[next_index_Alice] = -math.inf
#         diff_bob[next_index_Alice] = -math.inf
#
#         next_index_Bob = diff_bob.index(max(diff_bob))
#         points_B += bobValues[next_index_Bob]
#         aliceValues[next_index_Bob] = 0
#         bobValues[next_index_Bob] = 0
#         diff_alice[next_index_Bob] = -math.inf
#         diff_bob[next_index_Bob] = -math.inf
#
#         count += 1
#         #print(points_A)
#         #print(points_B)
#     return 1 if points_A > points_B else 0 if points_A == points_B else -1
#
#
# aliceValues1 = [1,3]
# bobValues1 = [2,1]
# aliceValues2 = [1,2]
# bobValues2 = [3,1]
# aliceValues3 = [2,4,3]
# bobValues3 = [1,6,7]
# print(stoneGameVI(aliceValues1, bobValues1))
# print(stoneGameVI(aliceValues2, bobValues2))
# print(stoneGameVI(aliceValues3, bobValues3))
#Initial Weight
weight = 100.00

#Cost Functions
def ground_cost(weight):
  cost = 20.00
  if weight > 10:
    cost += weight * 4.75
  elif weight > 6:
    cost += weight * 4.00
  elif weight > 2:
    cost += weight * 3.00
  else:
    cost += weight * 1.50
  return cost

def drone_cost(weight):
  cost = 0.00
  if weight > 10:
    cost += weight * 14.25
  elif weight > 6:
    cost += weight * 12.00
  elif weight > 2:
    cost += weight * 9.00
  else:
    cost += weight * 4.50
  return cost

premium_cost = 125.00

#Best Pricing
def best_pricing(weight):
  if ground_cost(weight) < drone_cost(weight) and ground_cost(weight) < premium_cost:
    print("Ground shipping is the least expensive and will cost $" + str(ground_cost(weight)) + ".")
    print("You will save $" + str(drone_cost(weight) - ground_cost(weight)) + " by not using drone shipping and $" + str(premium_cost - ground_cost(weight)) + " by not using premium shipping.")
    print("Nice savings!")
  elif drone_cost(weight) < premium_cost:
    print("Drone shipping is the least expensive and will cost $" + str(drone_cost(weight)) + ".")
    print("You will save $" + str(ground_cost(weight) - drone_cost(weight)) + " by not using ground shipping and $" + str(premium_cost - drone_cost(weight)) + " by not using premium shipping.")
    print("Nice savings!")
  else:
    print("Premium shipping is the least expensive and will cost $" + str(premium_cost) + ".")
    print("You will save $" + str(ground_cost(weight) - premium_cost) + " by not using ground shipping and $" + str(drone_cost(weight) - premium_cost) + " by not using drone shipping.")
    print("Nice savings!")

best_pricing(weight)

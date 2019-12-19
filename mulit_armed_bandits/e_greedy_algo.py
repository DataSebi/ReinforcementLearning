# init for a=1 to k:
#   Q(a) = 0
#   N(a) = 0

# WHILE TRUE
#   A = if (random(epsilon) max_a(Q(a)) else random(Actionspace))
#   R = bandit(A)
#   N(A) = N(A)+1
#   Q(A) = Q(A)+1/(N(A))*(R-Q(A))
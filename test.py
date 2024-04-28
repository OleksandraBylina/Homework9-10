def foo_c(x: float, n: int) ->float:
    current_member = -1

    for k in range(2, n + 1):
        a = 1
        k_step = k**2
        for j in range(k_step - k + 1, k_step + k + 1):
            a /= j
        # counter = 2*k
        # while counter <= k**2:
        #     a /= counter
        #     counter += 1
        current_member = current_member * (-x)*a
        yield current_member
    return current_member
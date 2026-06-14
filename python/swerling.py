def swerling(num_draws: int, murcs: float, rng: np.random.Generator) -> NDArray:
    """
    The CDF of a Swerling 2 model is X(rho) = 1 - exp(-rho/muRCS)
    The inverse CDF method draws values from the CDF, uniformly over [0,1),
    to generate values for rho. Solving for rho using the inverse CDF method gives us
    rho = -muRCS log(1-Ru), where log is base e, and Ru is a random draw from
    a uniform distribution from [0,1)

    Args:
        num_draws: integer scalar number of draws from Swerling 2 model
        murcs: real scalar value for the mean of the rcs values to be drawn in decibels
        rng: generator of randomness

    Returns
        real array of rcs values from swerling model in decibels
    """

    # using the linear values to draw deviates, convert back to decibels on return
    linear_mean = np.exp(np.euler_gamma) * 10 ** (murcs / 10)  # https://www.overleaf.com/read/hsnrsggykjpv#acf90b
    nurcs = -linear_mean * np.log(rng.uniform(0, 1, num_draws))
    return 10 * np.log10(nurcs)

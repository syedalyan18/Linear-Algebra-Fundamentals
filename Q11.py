def bayes_theorem(prior,sensitivity,specificity):
    evidence=(sensitivity*prior)+(1-specificity)*(1-prior)
    posterior=(sensitivity*prior) / evidence
    return posterior

prior=0.01
specificity=0.90
sensitivity=0.95

posterior=bayes_theorem(prior,sensitivity,specificity)
print("Probability of Disease given Positive Test : ",posterior)
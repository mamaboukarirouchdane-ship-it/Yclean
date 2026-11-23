def run(c):
    c('dissent', 2/12*100, 16.7, 0.05); c('exp', 0.85*25, 21.25, 1e-9); c('surp hausse', 25-0.85*25, 3.75, 1e-9); c('surp maintien', 0-0.85*25, -21.25, 1e-9)
    c('sim exp', 0.60*25, 15.0, 1e-9); c('sim hausse', 25-15, 10, 0); c('sim maintien', 0-15, -15, 0)
    c('ex4d', abs(-15) > abs(10), True, 0)

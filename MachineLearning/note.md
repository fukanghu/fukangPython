# linear regression (univariate linear regression)
- linear regrassion with one variable
    - e.g. hθ (x) = θ0 + θ1 x
    - e.g. [linear_regression.png]
    
# cost function 
- training set(choose a/b, so that h(x) is close to y for training)
- minimize θ0/θ1, (1/(2m)) ∑(m/(i=1)) (hθ (x i) - y i)^2
- "m" is training examples
- hθ(xi) = θ0 + θ1xi
- J(θ0,θ1) = (1/(2m)) ∑(m|(i=1)) (hθ (x i) - y i)^2, cost function(squared error function)
- [cost_function1.png]

- when θ0 = 0
- J(1) = 0
- J(0.5) = 0.58
- J(0) = 2.3
- J(-0.5) 5.15
- minimize θ1 of J(θ1)
- J(θ) [cost_function2.png]

- hypothesis: hθ (x) = θ0 + θ1 x
- parameters: θ0, θ1
- cost function: J(θ0,θ1) = (1/(2m)) ∑(m|(i=1)) (hθ (x i) - y i)^2
- goal: minimize θ0 & θ1 of J(θ0, θ1)

- contour plot/contour figure

# gradient descent 
- have some function J(θ0, θ1)
- want min θ0 & θ1 of J(θ0, θ1)
- outline:
    - start with some θ0, θ1 (say θ0 = 0, θ1 = 0)
    - keep changing θ0, θ1 to reduce J(θ0, θ1)
    until we hopefully end up at a minimum 
- gradient_descent [gradient_descent1.png]

- gradient_descent_intuition [gradient_descent2.png]
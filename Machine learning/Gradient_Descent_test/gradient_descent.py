import numpy as np
import sys

def gradient_descent(x,y):
    # m current value & b current value:
    m_curr = b_curr = 0
    # amount of iterations:
    iterations = 1000
    # define learning rate:
    learning_rate = 0.005
    # bewaart de lengte van onze x datapoint array:
    # als we terugkijken naar onze  formule dan beschrijf deze een verhouding van (2 over n) : 2/n


    n = len(x)

    print(n);





    # formule: f` = (2/n)Σ(n) - x[i] (y[i] - (mx[i] + b))
    for i in range(iterations):
        # berekent de y waarde voor de afgeleide op elk y punt in onze dataset:
        y_predicted = m_curr * x + b_curr

        # een dubbele asterix staat gelijk aan het kwadraat:
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])

        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        # verander waarde van m_curr voor de volgende iteratie:
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd



        print("m {}, b {}, cost {}, iteration {} ".format(m_curr, b_curr, cost , i))



x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

test = [3,3,3,3,3]

gradient_descent(x,y)



from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# It is important to know how the relationship between the values of the x-axis and the values of the y-axis is, 
# if there are no relationship the linear regression can not be used to predict anything.

# This relationship - the coefficient of correlation - is called r.

slope, intercept, r, p, std_err = stats.linregress(x, y)
# The r value ranges from -1 to 1, where 0 means no relationship, and 1 (and -1) means 100% related.

print(r)